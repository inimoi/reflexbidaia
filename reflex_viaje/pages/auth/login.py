import reflex as rx

from ...utils.utils import login_title, login_description, login_meta
from ...navigation.routes import Routes


@rx.page(route=Routes.LOGIN.value, 
    title=login_title, 
    description=login_description, 
    meta=login_meta)   
def login_page() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.vstack(
                rx.vstack(
                    rx.heading("Basque adventure", size="9", class_name="mb-6 font-bold text-center"),
                    rx.heading("Iniciar Sesión", size="7", class_name="mb-6 font-bold text-center"),
                    rx.text("Email", class_name="text-sm font-medium mb-1 w-full text-left"),
                    rx.input(placeholder="tu@email.com", type="email", class_name="w-full p-2 border rounded-md dark:border-slate-700 dark:bg-slate-800"),
                    rx.text("Contraseña", class_name="text-sm font-medium mt-4 mb-1 w-full text-left"),
                    rx.input(placeholder="••••••••", type="password", class_name="w-full p-2 border rounded-md dark:border-slate-700 dark:bg-slate-800"),
                    rx.button("Entrar", class_name="w-full mt-6 bg-slate-900 dark:bg-slate-100 text-white dark:text-slate-900 font-semibold py-2 rounded-md hover:opacity-90 transition-opacity cursor-pointer"),
                   
                    class_name="w-full max-w-sm bg-white/80 dark:bg-slate-900/80 backdrop-blur-md p-8 rounded-2xl shadow-xl border border-white/20 dark:border-slate-800/50",
                    align="center",
                ),
                class_name="flex flex-1 flex-col items-end justify-center w-full p-6",
            ),
            class_name="layout-container flex h-full grow flex-col p-8 rounded-2xl shadow-xl border border-white/20 dark:border-slate-800/50",
            width="100%",
            max_width="1440px",
            background_image="url('/bg_ikurrina.png')",
            background_size="cover",
            background_position="start",
        ),
        class_name="min-h-screen w-full font-display text-slate-900 dark:text-slate-100",
        align="center",
    )
