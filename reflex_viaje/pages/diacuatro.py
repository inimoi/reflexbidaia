"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx 
from rxconfig import config
from ..layouts.layout_base import base_layout
from ..utils.utils import _meta
from ..utils.utils import diacuatro_description, diacuatro_meta, diacuatro_title, lang
from ..navigation.routes import Routes
from ..layouts.protected.protected_routes import protected_page
from reflex_viaje.pages.auth.login import LoginState

@rx.page(
    route=Routes.DIACUATRO.value,
    title=diacuatro_title,
    description=diacuatro_description,
    meta=diacuatro_meta,
    on_load=LoginState.validate_token_app
)
def diacuatro() -> rx.Component:
    # Welcome Page (diauno)
    return protected_page(
        base_layout(
        rx.box(
            rx.image(
                src="/Plano_dia_4.png",
                width="100%",
                height="auto",
                alt="Plano Día 4",
            ),
            class_name="w-full max-w-4xl mx-auto overflow-hidden",
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