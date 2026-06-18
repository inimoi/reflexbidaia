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


#DIA 1
diauno_title = "Día 1"
diauno_description = "Día 1"
diauno_meta = [
    {"name": "og:title", "content": diauno_title},
    {"name": "og:description", "content": diauno_description},
    ]
diauno_meta.extend(_meta)


#DIA 2
diados_title = "Día 2"
diados_description = "Día 2"
diados_meta = [
    {"name": "og:title", "content": diados_title},
    {"name": "og:description", "content": diados_description},
    ]
diados_meta.extend(_meta)

#DIA 3
diatres_title = "Día 3"
diatres_description = "Día 3"
diatres_meta = [
    {"name": "og:title", "content": diatres_title},
    {"name": "og:description", "content": diatres_description},
    ]
diatres_meta.extend(_meta)

#DIA 4
diacuatro_title = "Día 4"
diacuatro_description = "Día 4"
diacuatro_meta = [
    {"name": "og:title", "content": diacuatro_title},
    {"name": "og:description", "content": diacuatro_description},
    ]
diacuatro_meta.extend(_meta)

#DIA 5
diacinco_title = "Día 5"
diacinco_description = "Día 5"
diacinco_meta = [
    {"name": "og:title", "content": diacinco_title},
    {"name": "og:description", "content": diacinco_description},
    ]
diacinco_meta.extend(_meta)

#Fotos destinos
fotosdestinos_title = "Fotos destinos"
fotosdestinos_description = "Fotos de los destinos"
fotosdestinos_meta = [
    {"name": "og:title", "content": fotosdestinos_title},
    {"name": "og:description", "content": fotosdestinos_description},
    ]
fotosdestinos_meta.extend(_meta)

#fotos viaje
fotosviaje_title = "Fotos viaje"
fotosviaje_description = "Fotos del viaje"
fotosviaje_meta = [
    {"name": "og:title", "content": fotosviaje_title},
    {"name": "og:description", "content": fotosviaje_description},
    ]
fotosviaje_meta.extend(_meta)

#gastos
gastos_title = "Gastos"
gastos_description = "Gastos del viaje"
gastos_meta = [
    {"name": "og:title", "content": gastos_title},
    {"name": "og:description", "content": gastos_description},
    ]
gastos_meta.extend(_meta)   


 