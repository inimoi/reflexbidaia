import reflex as rx


def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")

#el previemw de la carga, debería ser una imegen
preview ="https://pythonfix.com/pkg/r/reflex/reflex-banner.webp"

_meta = [
    {"name": "og:type", "content": "website"},
    {"name": "og:image", "content": preview},
]

#Página 
index_title = "Viaje a Euskal Herria"
index_description = "Viaje de verano por Euskal Herria"
index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description},
    ]
index_meta.extend(_meta)