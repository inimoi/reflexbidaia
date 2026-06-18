"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from .pages.index import index
from .pages.auth.login import login_page
from .pages.diauno import diauno
from .pages.diados import diados
from .pages.diatres import diatres
from .pages.diacuatro import diacuatro
from .pages.diacinco import diacinco    
from .pages.fotosviaje import fotosviaje
from .pages.fotosdestinos import fotosdestinos
from .pages.gastos import gastos
from .api.api import fastapi_app


app = rx.App(
    stylesheets=["styles.css"],
    api_transformer=fastapi_app
)
