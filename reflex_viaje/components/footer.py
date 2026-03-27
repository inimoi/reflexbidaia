import reflex as rx

def footer() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text("© 2026 Reflex. All rights reserved."),
            rx.text("Privacy Policy"),
            rx.text("Terms of Service"),
            rx.text("Contact"),
            spacing="4",
            justify="center",
            align_items="center",
        ),
        class_name="nav-footer-style",
    )
