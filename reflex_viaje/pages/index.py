"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx 
from rxconfig import config
from ..layouts.layout_base import base_layout
from ..utils.utils import _meta
from ..utils.utils import index_title, index_description, index_meta, lang
from ..navigation.routes import Routes

class State(rx.State):
    """The app state."""

@rx.page(
    route=Routes.INDEX.value,
    title=index_title,
    description=index_description,
    meta=index_meta,
)
def index() -> rx.Component:
    # Welcome Page (Index)
    return base_layout(
        rx.box(
            rx.vstack(
                rx.heading(
                    "Euskal Herria",
                    class_name="text-6xl md:text-8xl font-bold text-white tracking-tighter drop-shadow-2xl mb-4",
                ),
                rx.text(
                    "Descubre la magia del norte. Paisajes infinitos, cultura milenaria y gastronomía única.",
                    class_name="text-xl md:text-2xl text-white/90 max-w-2xl text-center font-medium drop-shadow-lg mb-8",
                ),
                rx.button(
                    "Empezar la Aventura",
                    class_name="bg-white text-blue-900 hover:bg-blue-50 px-8 py-6 text-lg font-bold rounded-full transition-all transform hover:scale-105 shadow-xl",
                    on_click=lambda: rx.redirect(Routes.LOGIN.value),
                ),
                class_name="relative z-10 flex flex-col items-center justify-center h-full px-4",
            ),
            # Overlay para mejorar legibilidad
            rx.box(
                class_name="absolute inset-0 bg-black/40 z-0",
            ),
            class_name="relative w-full h-[80vh] overflow-hidden rounded-3xl shadow-2xl",
            style={
                "background_image": "url('/hero_bg.png')",
                "background_size": "cover",
                "background_position": "center",
            },
        ),
        rx.grid(
            rx.vstack(
                rx.icon("map-pin", size=32, class_name="text-blue-900 mb-2"),
                rx.heading("Destinos", size="5", class_name="font-bold"),
                rx.text("Explora los rincones más bellos.", class_name="text-slate-600 text-center"),
                class_name="p-8 bg-white rounded-2xl shadow-md border border-slate-100 hover:shadow-lg transition-shadow",
            ),
            rx.vstack(
                rx.icon("camera", size=32, class_name="text-blue-900 mb-2"),
                rx.heading("Galería", size="5", class_name="font-bold"),
                rx.text("Captura momentos inolvidables.", class_name="text-slate-600 text-center"),
                class_name="p-8 bg-white rounded-2xl shadow-md border border-slate-100 hover:shadow-lg transition-shadow",
            ),
            rx.vstack(
                rx.icon("utensils", size=32, class_name="text-blue-900 mb-2"),
                rx.heading("Gastronomía", size="5", class_name="font-bold"),
                rx.text("Saborea la auténtica cocina vasca.", class_name="text-slate-600 text-center"),
                class_name="p-8 bg-white rounded-2xl shadow-md border border-slate-100 hover:shadow-lg transition-shadow",
            ),
            columns="3",
            spacing="4",
            class_name="w-full mt-12 grid-cols-1 md:grid-cols-3",
        ),
        width="100%",
        padding_x="4",
    )