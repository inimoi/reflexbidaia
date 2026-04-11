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

#Login
login_title = "Login"
login_description = "Login"
login_meta = [
    {"name": "og:title", "content": login_title},
    {"name": "og:description", "content": login_description},
    ]
login_meta.extend(_meta)

#register
register_title = "Registro"
register_description = "Registro"
register_meta = [
    {"name": "og:title", "content": register_title},
    {"name": "og:description", "content": register_description},
    ]
register_meta.extend(_meta)