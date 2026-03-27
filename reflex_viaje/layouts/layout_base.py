
import reflex as rx

from ..components.navbar import navbar_buttons
from ..components.footer import footer


def base_layout(*args, **kwargs) -> rx.Component:
    return rx.container(
        navbar_buttons(),
        rx.vstack(
            *args,
            **kwargs,
            spacing="0",
            width="100%",
            align_items="center",
            padding_top="2em",  # Spacing between navbar and content
            min_height="85vh",
        ),
        footer(),
        width="100%",
        max_width="100%",  # Fluid container for full-width navbar
        padding_top="0.5em",  # Remove default padding so navbar hits edges
        size="4",
    )