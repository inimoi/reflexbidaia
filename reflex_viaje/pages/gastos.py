"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from reflex_viaje.pages.auth.login import LoginState
import reflex as rx 
from rxconfig import config
from ..layouts.layout_base import base_layout
from ..utils.utils import _meta
from ..utils.utils import gastos_title, gastos_description, gastos_meta, lang
from ..navigation.routes import Routes
from ..layouts.protected.protected_routes import protected_page


@rx.page(
    route=Routes.GASTOS.value,
    title=gastos_title,
    description=gastos_description,
    meta=gastos_meta,
    on_load=LoginState.validate_token_app
)
def gastos() -> rx.Component:
    # Welcome Page (Index)
    return protected_page(
        base_layout(
            rx.box(
                rx.text("Gastos"),
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