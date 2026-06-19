import reflex as rx
from pydantic import ValidationError
from fastapi.security import HTTPAuthorizationCredentials
from ...utils.utils import login_title, login_description, login_meta
from ...navigation.routes import Routes
from ...api.auth import Login
from ...api.api import login, validate_token_endpoint, get_profile_endpoint


class LoginState(rx.State):
    is_loading: bool = False
    error_message: str = ""
    logged_in: bool = False
    usuario: str = ""
    token_local_storage: str | None = rx.LocalStorage(
        name="token_local_storage", sync=True
    )
    user_data: dict = {}

    @rx.event
    async def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.is_loading = True
        self.error_message = ""

        try:
            datos_log = Login(
                email=form_data.get("email"), password=form_data.get("password")
            )

            respuesta = await login(datos_log)

            if respuesta and "access_token" in respuesta:
                self.logged_in = True
                self.usuario = respuesta["user"]["email"]
                self.token_local_storage = respuesta.get("access_token")
                yield rx.toast.success("¡Bienvenido de nuevo!")
                yield rx.redirect("/")
            else:
                self.error_message = "Credenciales incorrectas"
                yield rx.toast.error(self.error_message)

        except ValidationError as e:
            error = e.errors()[0]
            self.error_message = (
                f"Dato no válido: {error.get('msg', 'Error de formato')}"
            )
            yield rx.toast.error(self.error_message)

        except Exception as e:
            self.error_message = (
                "Error en el inicio de sesión. Verifica tus credenciales."
            )
            yield rx.toast.error(self.error_message)

        finally:
            self.is_loading = False

    async def validate_token_app(self):
        """Valida el token llamando al endpoint y carga el perfil si es válido"""
        if not self.token_local_storage:
            self.logged_in = False
            return rx.redirect(Routes.LOGIN.value)

        credenciales = HTTPAuthorizationCredentials(
            scheme="Bearer", credentials=self.token_local_storage
        )
        try:
            result = await validate_token_endpoint(credentials=credenciales)
            if result.get("valid"):
                self.logged_in = True
                await self.load_user_profile()
            else:
                self.logged_in = False
                return rx.redirect(Routes.LOGIN.value)
        except Exception:
            self.logged_in = False
            return rx.redirect(Routes.LOGIN.value)

    async def load_user_profile(self):
        """Recupera el perfil del usuario desde el endpoint `/auth/me`."""
        if not self.token_local_storage:
            return
        credenciales = HTTPAuthorizationCredentials(
            scheme="Bearer", credentials=self.token_local_storage
        )
        try:
            perfil = await get_profile_endpoint(credentials=credenciales)
            self.user_data = perfil
            self.usuario = perfil.get("email", "")
        except Exception:
            pass

    @rx.event
    def logout(self):
        """Cierra sesión y borra el estado/local storage"""
        self.logged_in = False
        self.token_local_storage = None
        self.user_data = {}
        yield rx.toast.info("Sesión cerrada")
        yield rx.redirect(Routes.LOGIN.value)

    async def redirect_if_logged_in(self):
        """Redirige a index si el usuario ya está autenticado."""
        await self.validate_token_app()
        if self.logged_in:
            return rx.redirect(Routes.INDEX.value)


@rx.page(
    route=Routes.LOGIN.value,
    title=login_title,
    description=login_description,
    meta=login_meta,
    on_load=LoginState.redirect_if_logged_in,
)
def login_page() -> rx.Component:
    return (
        rx.box(
            # Contenedor principal centrado
            rx.vstack(
                rx.form(
                    # Encabezados
                    rx.vstack(
                        rx.heading(
                            "Viaje a Euskal Herria",
                            size="8",
                            class_name="font-extrabold tracking-tight text-white mb-1",
                            style={
                                "font-family": "var(--font-heading)",
                                "color": "white",
                            },
                        ),
                        rx.text(
                            "Ongi Etorri — Iniciar Sesión",
                            class_name="text-sm font-semibold text-slate-300 tracking-wide",
                            style={"font-family": "var(--font-accent)"},
                        ),
                        align="center",
                        spacing="1",
                        class_name="mb-6",
                    ),
                    # Campos de entrada
                    rx.vstack(
                        rx.vstack(
                            rx.text(
                                "Email",
                                class_name="text-xs font-bold text-slate-300 tracking-wider uppercase mb-1 w-full text-left",
                            ),
                            rx.input(
                                placeholder="[EMAIL_ADDRESS]",
                                name="email",
                                required=True,
                                type="email",
                                class_name="w-full px-2 py-1 bg-white/10 border border-white/20 rounded-xl text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-[#bc945c] focus:border-transparent transition-all",
                            ),
                            width="100%",
                            spacing="0",
                        ),
                        rx.vstack(
                            rx.text(
                                "Contraseña",
                                class_name="text-xs font-bold text-slate-300 tracking-wider uppercase mb-1 w-full text-left",
                            ),
                            rx.input(
                                placeholder="••••••••",
                                name="password",
                                required=True,
                                type="password",
                                class_name="w-full px-2 py-1 bg-white/10 border border-white/20 rounded-xl text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-[#bc945c] focus:border-transparent transition-all",
                            ),
                            width="100%",
                            spacing="0",
                            class_name="mt-4",
                        ),
                        # Mensaje de Error
                        rx.cond(
                            LoginState.error_message != "",
                            rx.box(
                                rx.hstack(
                                    rx.icon(
                                        "circle-alert",
                                        size=18,
                                        class_name="text-red-400 flex-shrink-0",
                                    ),
                                    rx.text(
                                        LoginState.error_message,
                                        class_name="text-sm text-red-200 font-medium",
                                    ),
                                    align="center",
                                    spacing="2",
                                ),
                                class_name="w-full p-3 bg-red-950/60 border border-red-500/30 rounded-xl mt-4",
                            ),
                        ),
                        # Botón Entrar
                        rx.button(
                            "Entrar",
                            class_name="w-full mt-6 font-bold py-3 rounded-xl shadow-lg hover:opacity-90 active:scale-95 transition-all cursor-pointer flex justify-center items-center border-none",
                            style={
                                "background_color": "var(--primary-color)",
                                "color": "#ffffff",
                            },
                        ),
                        width="100%",
                    ),
                    # Estilo de tarjeta Glassmorphism
                    class_name="w-full max-w-md p-8 rounded-3xl shadow-2xl z-10",
                    style={
                        "background_color": "rgba(27, 38, 44, 0.75)",
                        "border": "1px solid rgba(255, 255, 255, 0.15)",
                        "backdrop_filter": "blur(12px)",
                    },
                    on_submit=LoginState.handle_submit,
                    align="center",
                ),
                class_name="flex flex-col items-center justify-center min-h-screen w-full p-6",
            ),
            class_name="relative min-h-screen w-full overflow-hidden",
            style={
                "background_image": "url('/bg_ikurrina.png')",
                "background_size": "cover",
                "background_position": "center",
            },
        ),
    )
