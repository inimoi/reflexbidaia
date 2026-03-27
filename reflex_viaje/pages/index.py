"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx 
from rxconfig import config
from ..layouts.layout_base import base_layout
from ..utils.utils import _meta
from ..utils.utils import index_title, index_description, index_meta, lang

class State(rx.State):
    """The app state."""

@rx.page(
    route="/",
    title=index_title,
    description=index_description,
    meta=index_meta,
)
def index() -> rx.Component:
    # Welcome Page (Index)
    return base_layout(
        rx.container(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
        ),
    )