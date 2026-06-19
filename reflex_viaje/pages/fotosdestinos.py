"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx 
from ..layouts.layout_base import base_layout
from ..utils.utils import fotosdestinos_title, fotosdestinos_description, fotosdestinos_meta

from ..navigation.routes import Routes
from reflex_viaje.pages.auth.login import LoginState
from ..layouts.protected.protected_routes import protected_page

class FotosDestinosState(rx.State):    
    images: list[dict[str, str]] = [
        {"url": "/Donostia.jpg", "title": "Donostia-San Sebastián", "desc": "La espectacular playa de La Concha y vistas desde el Monte Igueldo."},
        {"url": "/Biarritz.png", "title": "Biarritz", "desc": "Elegancia imperial, playas de surfistas y el icónico Rocher de la Vierge."},
        {"url": "/Bayonne.png", "title": "Bayona", "desc": "Catedral gótica, calles coloridas y delicioso chocolate artesanal."},
        {"url": "/Fuenterrabia.png", "title": "Hondarribia (Fuenterrabía)", "desc": "Barrio de la Marina con balcones coloridos y murallas medievales."},
        {"url": "/pasaidonibane.png", "title": "Pasai Donibane (Pasajes de San Juan)", "desc": "Pueblo marinero encajado entre la montaña y la bahía."},
        {"url": "/sanjuandeluz.png", "title": "San Juan de Luz", "desc": "Bahía tranquila, arquitectura vasca y rica historia real."},
        {"url": "/zarautz.png", "title": "Zarautz", "desc": "La playa más larga del País Vasco, paraíso de surf y buena comida."},
        {"url": "/Getaria_1.jpg", "title": "Getaria", "desc": "Pueblo pesquero famoso por su 'ratón', el txakoli y Elcano."},
        {"url": "/zumaia_1.jpg", "title": "Zumaia (Flysch)", "desc": "Impresionantes acantilados y formaciones geológicas de millones de años."},
        {"url": "/Hendaye.jpg", "title": "Hendaya", "desc": "Playa kilométrica en la frontera y el impresionante Castillo de Abbadia."},
        {"url": "/Hecho.png", "title": "Valle de Hecho", "desc": "Naturaleza indómita, bosques y picos majestuosos del Pirineo Aragonés."}
    ]
    
    current_index: int = 0
    
    def next_image(self):
        self.current_index = (self.current_index + 1) % len(self.images)
        
    def prev_image(self):
        self.current_index = (self.current_index - 1) % len(self.images)
        
    def set_index(self, index: int):
        self.current_index = index

    @rx.var
    def current_image_url(self) -> str:
        return self.images[self.current_index]["url"]
        
    @rx.var
    def current_image_title(self) -> str:
        return self.images[self.current_index]["title"]
        
    @rx.var
    def current_image_desc(self) -> str:
        return self.images[self.current_index]["desc"]


def carousel() -> rx.Component:
    return rx.box(
        # Inner container with relative positioning
        rx.box(
            # Image component that binds to State.current_image_url
            rx.image(
                src=FotosDestinosState.current_image_url,
                class_name="w-full h-full object-cover transition-all duration-700 ease-in-out select-none",
            ),
            # Gradient overlay to make the text contrast nicely
            rx.box(
                class_name="absolute inset-0 bg-gradient-to-t from-black/85 via-black/40 to-transparent z-10 pointer-events-none"
            ),
            # Text / Caption Overlay (Title + Description)
            rx.vstack(
                rx.heading(
                    FotosDestinosState.current_image_title,
                    class_name="text-2xl md:text-4xl font-bold text-white drop-shadow-lg tracking-tight",
                    style={"font_family": "var(--font-heading)", "color": "white"}
                    
                ),
                rx.text(
                    FotosDestinosState.current_image_desc,
                    class_name="text-white/90 text-sm md:text-base max-w-xl drop-shadow-md font-medium",
                ),
                align_items="start",
                spacing="2",
                class_name="absolute bottom-8 left-8 right-8 md:bottom-12 md:left-12 md:right-12 z-20"
            ),
            # Left Navigation Button
            rx.button(
                rx.icon("chevron-left", size=24, class_name="text-white"),
                on_click=FotosDestinosState.prev_image,
                class_name="absolute left-4 top-1/2 -translate-y-1/2 z-20 flex items-center justify-center w-10 h-10 md:w-12 md:h-12 bg-black/30 backdrop-blur-md hover:bg-black/50 border border-white/10 rounded-full transition-all duration-300 hover:scale-110 cursor-pointer shadow-lg active:scale-95"
            ),
            # Right Navigation Button
            rx.button(
                rx.icon("chevron-right", size=24, class_name="text-white"),
                on_click=FotosDestinosState.next_image,
                class_name="absolute right-4 top-1/2 -translate-y-1/2 z-20 flex items-center justify-center w-10 h-10 md:w-12 md:h-12 bg-black/30 backdrop-blur-md hover:bg-black/50 border border-white/10 rounded-full transition-all duration-300 hover:scale-110 cursor-pointer shadow-lg active:scale-95"
            ),
            # Indicators (dots)
            rx.hstack(
                *[
                    rx.box(
                        class_name=rx.cond(
                            FotosDestinosState.current_index == i,
                            "w-8 h-2.5 bg-[#bc945c] rounded-full transition-all duration-300 shadow-[0_0_8px_#bc945c]",
                            "w-2.5 h-2.5 bg-white/40 hover:bg-white/70 rounded-full transition-all duration-300 cursor-pointer"
                        ),
                        on_click=FotosDestinosState.set_index(i)
                    )
                    for i in range(12)  # length of State.images list
                ],
                spacing="2",
                class_name="absolute bottom-4 left-1/2 -translate-x-1/2 z-20"
            ),
            class_name="relative w-full h-[55vh] min-h-[250px] max-h-[400px] overflow-hidden rounded-3xl shadow-2xl border border-slate-200/10 group"
        ),
        class_name="w-full max-w-5xl mx-auto my-6 px-2"
    )


@rx.page(
    route=Routes.FOTOSDESTINOS.value,
    title=fotosdestinos_title,
    description=fotosdestinos_description,
    meta=fotosdestinos_meta,
    on_load=LoginState.validate_token_app
)
def fotosdestinos() -> rx.Component:
    # Welcome Page (Index)
    return protected_page(
        base_layout(
            rx.vstack(
                rx.heading("Destinos del Viaje", class_name="text-3xl md:text-5xl font-extrabold mb-2 mt-4 text-center", style={"color": "white"}),
                rx.text("Explora los mágicos lugares que visitamos en nuestra aventura.", class_name="text-white text-center max-w-xl mx-auto"),
                carousel(),
                align_items="center",
                width="100%",
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