import reflex as rx

from ...utils.utils import login_title, login_description, login_meta
from ...navigation.routes import Routes


class LoginState(rx.State):
    email: str = ""
    password: str = ""
    error_message: str = ""
    is_loading: bool = False

    def set_email(self, email: str):
        self.email = email

    def set_password(self, password: str):
        self.password = password

    def handle_login(self):
        self.error_message = ""
        self.is_loading = True
        
        # Validaciones básicas de entrada
        if not self.email or not self.password:
            self.error_message = "Por favor, completa todos los campos."
            self.is_loading = False
            return
            
        if "@" not in self.email:
            self.error_message = "Por favor, introduce un correo electrónico válido."
            self.is_loading = False
            return
            
        # Credenciales de demostración
        # TODO(security): Estas credenciales demo son solo para entorno local de prueba y no deben usarse en producción.
        if self.email == "admin@email.com" and self.password == "admin123":
            self.is_loading = False
            self.email = ""
            self.password = ""
            return rx.redirect(Routes.INDEX.value)
        else:
            # Mensaje de error genérico para prevenir enumeración de usuarios
            self.error_message = "Email o contraseña incorrectos."
            self.is_loading = False
            return


@rx.page(route=Routes.LOGIN.value, 
    title=login_title, 
    description=login_description, 
    meta=login_meta)   
def login_page() -> rx.Component:
    return rx.box(
        # Capa superpuesta oscura para legibilidad
        rx.box(
            class_name="absolute inset-0 bg-black/50 z-0",
        ),
        # Contenedor principal centrado
        rx.vstack(
            rx.vstack(
                # Botón de regreso a Home
                rx.hstack(
                    rx.link(
                        rx.hstack(
                            rx.icon("arrow-left", size=16),
                            rx.text("Volver al inicio", size="2", class_name="font-medium"),
                            align="center",
                            spacing="1",
                        ),
                        href=Routes.INDEX.value,
                        class_name="text-white/70 hover:text-white transition-colors mb-4 flex items-center self-start",
                    ),
                    width="100%",
                ),
                # Encabezados
                rx.vstack(
                    rx.heading(
                        "Basque Adventure",
                        size="8",
                        class_name="font-extrabold tracking-tight text-white mb-1",
                        style={"font-family": "var(--font-heading)"}
                    ),
                    rx.text(
                        "Ongi Etorri — Iniciar Sesión",
                        class_name="text-sm font-semibold text-slate-300 tracking-wide",
                        style={"font-family": "var(--font-accent)"}
                    ),
                    align="center",
                    spacing="1",
                    class_name="mb-6",
                ),
                
                # Campos de entrada
                rx.vstack(
                    rx.vstack(
                        rx.text(
                            "Correo Electrónico",
                            class_name="text-xs font-bold text-slate-300 tracking-wider uppercase mb-1 w-full text-left"
                        ),
                        rx.input(
                            placeholder="tu@email.com",
                            type="email",
                            value=LoginState.email,
                            on_change=LoginState.set_email,
                            class_name="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-xl text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-[#bc945c] focus:border-transparent transition-all",
                        ),
                        width="100%",
                        spacing="0",
                    ),
                    
                    rx.vstack(
                        rx.text(
                            "Contraseña",
                            class_name="text-xs font-bold text-slate-300 tracking-wider uppercase mb-1 w-full text-left"
                        ),
                        rx.input(
                            placeholder="••••••••",
                            type="password",
                            value=LoginState.password,
                            on_change=LoginState.set_password,
                            class_name="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-xl text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-[#bc945c] focus:border-transparent transition-all",
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
                                rx.icon("circle-alert", size=18, class_name="text-red-400 flex-shrink-0"),
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
                        rx.cond(
                            LoginState.is_loading,
                            rx.spinner(size="2"),
                            rx.text("Entrar a la Aventura"),
                        ),
                        on_click=LoginState.handle_login,
                        disabled=LoginState.is_loading,
                        class_name="w-full mt-6 font-bold py-3 rounded-xl shadow-lg hover:opacity-90 active:scale-95 transition-all cursor-pointer flex justify-center items-center border-none",
                        style={
                            "background_color": "var(--secondary-color)",
                            "color": "#ffffff"
                        }
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