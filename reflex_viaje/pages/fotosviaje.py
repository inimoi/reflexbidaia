"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config
from ..layouts.layout_base import base_layout
from ..utils.utils import _meta
from ..utils.utils import (
    fotosviaje_title,
    fotosviaje_description,
    fotosviaje_meta,
    lang,
)
from ..navigation.routes import Routes
import httpx
import os


class UploadState(rx.State):
    """The app state for the upload page."""

    is_uploading: bool = False
    upload_status: str = ""

    photos: list[dict[str, str]] = []
    current_index: int = 0

    async def load_photos(self):
        backend_url = os.getenv("API_URL", "http://localhost:8000")
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(f"{backend_url}/photos")
                data = response.json()
                if data.get("success"):
                    self.photos = data["photos"]
            except Exception as e:
                print(f"Error loading photos: {e}")

    def next_photo(self):
        if self.photos:
            self.current_index = (self.current_index + 1) % len(self.photos)

    def prev_photo(self):
        if self.photos:
            self.current_index = (self.current_index - 1) % len(self.photos)

    def set_index(self, index: int):
        self.current_index = index

    @rx.var
    def current_photo_url(self) -> str:
        if self.photos:
            return self.photos[self.current_index]["url"]
        return ""

    @rx.var
    def total_photos(self) -> int:
        return len(self.photos)

    async def handle_upload(self, files: list[rx.UploadFile]):
        """Handle the upload of file(s) via the FastAPI endpoint."""
        self.is_uploading = True
        self.upload_status = "Subiendo archivo..."

        # URL del backend (FastAPI)
        # En Reflex, por defecto el backend corre en el puerto 8000
        backend_url = os.getenv("API_URL", "http://localhost:8000")
        upload_endpoint = f"{backend_url}/upload"

        async with httpx.AsyncClient() as client:
            for file in files:
                upload_data = await file.read()
                file_name = file.filename

                try:
                    # Preparar el archivo para el POST request
                    files_payload = {
                        "file": (file_name, upload_data, file.content_type)
                    }

                    # Llamar al endpoint de FastAPI
                    response = await client.post(upload_endpoint, files=files_payload)
                    result = response.json()

                    if response.status_code == 200 and result.get("success"):
                        self.upload_status = f"✅ {result.get('message')}"
                    else:
                        error_type = result.get("error")
                        if error_type == "duplicate":
                            self.upload_status = f"⚠️ {result.get('message')}"
                        else:
                            self.upload_status = f"❌ {result.get('message')}"

                except Exception as e:
                    print(f"Error calling API: {e}")
                    self.upload_status = f"❌ Error de conexión: {str(e)}"

        await self.load_photos()
        self.is_uploading = False


def photos_carousel() -> rx.Component:
    return rx.cond(
        UploadState.total_photos > 0,
        rx.box(
            rx.box(
                rx.image(
                    src=UploadState.current_photo_url,
                    class_name="w-full h-full object-cover transition-all duration-700 ease-in-out select-none rounded-2xl",
                ),
                rx.cond(
                    UploadState.total_photos > 1,
                    rx.box(
                        rx.button(
                            rx.icon("chevron-left", size=24),
                            on_click=UploadState.prev_photo,
                            class_name="absolute left-2 top-1/2 -translate-y-1/2 z-10 flex items-center justify-center w-10 h-10 bg-black/30 backdrop-blur-md hover:bg-black/50 border border-white/10 rounded-full transition-all duration-300 hover:scale-110 cursor-pointer shadow-lg",
                        ),
                        rx.button(
                            rx.icon("chevron-right", size=24),
                            on_click=UploadState.next_photo,
                            class_name="absolute right-2 top-1/2 -translate-y-1/2 z-10 flex items-center justify-center w-10 h-10 bg-black/30 backdrop-blur-md hover:bg-black/50 border border-white/10 rounded-full transition-all duration-300 hover:scale-110 cursor-pointer shadow-lg",
                        ),
                        rx.hstack(
                            rx.foreach(
                                UploadState.photos,
                                lambda photo, i: rx.box(
                                    class_name=rx.cond(
                                        UploadState.current_index == i,
                                        "w-8 h-2.5 bg-[#bc945c] rounded-full transition-all duration-300 shadow-[0_0_8px_#bc945c]",
                                        "w-2.5 h-2.5 bg-white/40 hover:bg-white/70 rounded-full transition-all duration-300 cursor-pointer",
                                    ),
                                    on_click=UploadState.set_index(i),
                                ),
                            ),
                            spacing="2",
                            class_name="absolute bottom-3 left-1/2 -translate-x-1/2 z-10",
                        ),
                        class_name="absolute inset-0 z-10",
                    ),
                ),
                class_name="relative w-full h-[40vh] min-h-[150px] max-h-[250px] overflow-hidden rounded-2xl shadow-xl",
            ),
            class_name="w-full max-w-3xl mx-auto",
        ),
        rx.box(
            rx.text(
                "No hay fotos en el bucket. ¡Sube tu primera foto!",
                class_name="text-white/60 text-center text-lg",
            ),
            class_name="w-full h-[40vh] min-h-[150px] max-h-[250px] flex items-center justify-center rounded-2xl border-2 border-dashed border-white/20",
        ),
    )


@rx.page(
    route=Routes.FOTOSVIAJE.value,
    title=fotosviaje_title,
    description=fotosviaje_description,
    meta=fotosviaje_meta,
    on_load=UploadState.load_photos,
)
def fotosviaje() -> rx.Component:
    # Welcome Page (Index)
    return base_layout(
        rx.box(
            rx.vstack(
                rx.hstack(
                    rx.heading("Sube tus Fotos", size="8", margin_bottom="2rem", style={"color": "white"}),
                    rx.upload(
                        rx.vstack(
                            rx.button(
                                "Seleccionar Archivos",
                                color_scheme="blue",
                                variant="solid",
                            ),
                            rx.text(
                                "Arrastra los archivos aquí o haz clic para seleccionar",
                                color="gray",
                            ),
                            rx.text(
                                "Admita archivos JPG, PNG, GIF y WEBP",
                                color="gray",
                            ),
                            align_items="center",
                            justify_content="center",
                            padding="2rem",
                            border="2px dashed",
                            border_color=rx.color("blue", 5),
                            border_radius="md",
                            _hover={"bg": rx.color("blue", 2)},
                        ),
                        id="photo_upload",
                        multiple=True,
                        accept={
                            "image/png": [".png"],
                            "image/jpeg": [".jpg", ".jpeg"],
                            "image/gif": [".gif"],
                            "image/webp": [".webp"],
                        },
                        max_files=5,
                        disabled=UploadState.is_uploading,
                        on_drop=UploadState.handle_upload(
                            rx.upload_files(upload_id="photo_upload")
                        ),
                    ),
                    rx.cond(
                        UploadState.is_uploading,
                        rx.spinner(size="3"),
                    ),
                    rx.text(
                        UploadState.upload_status,
                        color=rx.cond(
                            UploadState.upload_status.contains("Error")
                            | UploadState.upload_status.contains("⚠️"),
                            rx.color("red", 9),
                            rx.color("green", 9),
                        ),
                        weight="bold",
                        margin_top="1rem",
                    ),
                    align_items="center",
                    width="100%",
                    height="30%",
                    padding_top="2rem",
                    flex="1",
                ),
                rx.hstack(
                    photos_carousel(),
                    flex="1",
                    width="100%",
                ),
                
                rx.grid(
                    rx.vstack(
                        rx.link(
                            rx.icon("map-pin", size=32, class_name="text-blue-900 mb-2"),
                            rx.heading(
                                "Fotos de los destinos", size="5", class_name="font-bold"
                            ),
                            rx.text(
                                "Explora los rincones de nuestro viaje",
                                class_name="text-slate-600 text-center",
                            ),
                            class_name="p-8 bg-white rounded-2xl shadow-md border border-slate-100 hover:shadow-lg transition-shadow",
                            href=Routes.FOTOSDESTINOS.value,
                        ),
                    ),
                    rx.vstack(
                        rx.link(
                            rx.icon("camera", size=32, class_name="text-blue-900 mb-2"),
                            rx.heading("Fotos del viaje", size="5", class_name="font-bold"),
                            rx.text(
                                "Sube y ve tus momentos favoritos.",
                                class_name="text-slate-600 text-center",
                            ),
                            class_name="p-8 bg-white rounded-2xl shadow-md border border-slate-100 hover:shadow-lg transition-shadow",
                            href=Routes.FOTOSVIAJE.value,
                        ),
                    ),
                    rx.vstack(
                        rx.link(
                            rx.icon("utensils", size=32, class_name="text-blue-900 mb-2"),
                            rx.heading(
                                "Gastos comunes del viaje", size="5", class_name="font-bold"
                            ),
                            rx.text(
                                "Visualización de los gastos comunes",
                                class_name="text-slate-600 text-center",
                            ),
                            class_name="p-8 bg-white rounded-2xl shadow-md border border-slate-100 hover:shadow-lg transition-shadow",
                            href=Routes.GASTOS.value,
                        ),
                    ),
                    columns="3",
                    spacing="4",
                    class_name="w-full mt-8 grid-cols-1 md:grid-cols-3",  
                    ),
                gap="4rem",
                width="100%",
                
            ),
        ),
        width="100%",
        padding_x="1",
        padding_y="5rem",
    ),

