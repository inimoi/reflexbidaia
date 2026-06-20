"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from reflex_viaje.pages.auth.login import LoginState
import reflex as rx 
from rxconfig import config
from ..layouts.layout_base import base_layout
from ..utils.utils import _meta
from ..utils.utils import index_title, index_description, index_meta, lang
from ..navigation.routes import Routes
from ..layouts.protected.protected_routes import protected_page


@rx.page(
    route=Routes.INDEX.value,
    title=index_title,
    description=index_description,
    meta=index_meta,
    on_load=LoginState.validate_token_app
)
def index() -> rx.Component:
    # Welcome Page (Index)
    return protected_page(
        base_layout(
            rx.box(
                rx.vstack(
                    rx.heading(
                        "Viaje a Euskal Herria",
                        class_name="text-4xl md:text-6xl text-red tracking-tighter drop-shadow-2xl mb-2",
                        style={"color": "white"},
                    ),
                    rx.button(
                        "Ruta día 1, jueves 06/08 ",
                        class_name="bg-white text-blue-900 hover:bg-blue-50 px-8 py-4 text-lg font-bold rounded-full transition-all transform hover:scale-105 shadow-xl",
                        on_click=lambda: rx.redirect(Routes.DIAUNO.value),
                    ),
                    rx.button(
                        "Ruta día 2, viernes 07/08",
                        class_name="bg-white text-blue-900 hover:bg-blue-50 px-8 py-4 text-lg font-bold rounded-full transition-all transform hover:scale-105 shadow-xl",
                        on_click=lambda: rx.redirect(Routes.DIADOS.value),
                    ),
                    rx.button(
                        "Ruta día 3, sábado 08/08",
                        class_name="bg-white text-blue-900 hover:bg-blue-50 px-8 py-4 text-lg font-bold rounded-full transition-all transform hover:scale-105 shadow-xl",
                        on_click=lambda: rx.redirect(Routes.DIATRES.value),
                    ),
                    rx.button(
                        "Ruta día 4, domingo 09/08",
                        class_name="bg-white text-blue-900 hover:bg-blue-50 px-8 py-4 text-lg font-bold rounded-full transition-all transform hover:scale-105 shadow-xl",
                        on_click=lambda: rx.redirect(Routes.DIACUATRO.value),
                    ),
                    rx.button(
                        "Ruta día 5, lunes 10/08",
                        class_name="bg-white text-blue-900 hover:bg-blue-50 px-8 py-4 text-lg font-bold rounded-full transition-all transform hover:scale-105 shadow-xl",
                        on_click=lambda: rx.redirect(Routes.DIACINCO.value),
                    ),
                    class_name="relative z-10 flex flex-col items-center justify-center h-full px-4",
                ),
                # Overlay para mejorar legibilidad
                rx.box(
                    class_name="absolute inset-0 z-0",
                ),
                class_name="relative w-full h-[50vh] overflow-hidden rounded-3xl shadow-2xl",
                style={
                    "background_image": "url('/Donostia.jpg')",
                    "background_size": "cover",
                    "background_position": "center",
                },
            ),
            rx.grid(
                rx.vstack(
                    rx.link(
                        rx.icon("map-pin", size=32, class_name="text-blue-900 mb-2"),
                        rx.heading("Fotos de los destinos", size="5", class_name="font-bold"),
                        rx.text("Explora los rincones de nuestro viaje", class_name="text-slate-600 text-center"),
                        class_name="p-8 bg-white rounded-2xl shadow-md border border-slate-100 hover:shadow-lg transition-shadow",
                        href=Routes.FOTOSDESTINOS.value
                    ),
                ),
                rx.vstack(
                    rx.link(
                        rx.icon("camera", size=32, class_name="text-blue-900 mb-2"),
                        rx.heading("Fotos del viaje", size="5", class_name="font-bold"),
                        rx.text("Sube y ve tus momentos favoritos.", class_name="text-slate-600 text-center"),
                        class_name="p-8 bg-white rounded-2xl shadow-md border border-slate-100 hover:shadow-lg transition-shadow",
                        href=Routes.FOTOSVIAJE.value
                    ),
                ),
                rx.vstack(
                    rx.link(
                        rx.icon("utensils", size=32, class_name="text-blue-900 mb-2"),
                        rx.heading("Gastos comunes del viaje", size="5", class_name="font-bold"),
                        rx.text("Visualización de los gastos comunes", class_name="text-slate-600 text-center"),
                        class_name="p-8 bg-white rounded-2xl shadow-md border border-slate-100 hover:shadow-lg transition-shadow",
                        href=Routes.GASTOS.value
                    ),
                ),
                columns="3",
                spacing="4",
                class_name="w-full mt-8 grid-cols-1 md:grid-cols-3",
            ),
            width="100%",
            padding_x="4",
        ),
    )