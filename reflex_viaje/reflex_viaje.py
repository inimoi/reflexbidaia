"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from .pages.index import index
from .pages.auth.login import login_page



app = rx.App(
    stylesheets=["styles.css"],
)
app.add_page(index)
app.add_page(login_page)
