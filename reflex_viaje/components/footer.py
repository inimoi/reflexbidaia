import reflex as rx

def footer() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text("© 2026 Iñigo. All rights reserved."),
            spacing="4",
            justify="center",
            align_items="center",
        ),
        class_name="nav-footer-style rounded-2xl shadow-md border border-slate-100 hover:shadow-lg transition-shadow",
        background_image="url('/iku.png')",
        background_size="cover",
        background_position="right",
        
    )
