from reflex_viaje.navigation.routes import Routes
import reflex as rx

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(rx.text(text, size="4", weight="medium"), href=url)


def navbar_buttons() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.heading("Viaje a Euskal Herria", size="7", weight="bold"),
                rx.hstack(
                    navbar_link("Inicio", "/#"),
                    navbar_link("Día 1🚐", "/diauno"),
                    navbar_link("Día 2⛱️", "/diados"),
                    navbar_link("Día 3🎉", "/diatres"),
                    navbar_link("Día 4🥐", "/diacuatro"),
                    navbar_link("Día 5🚐", "/diacinco"),
                    spacing="5",
                ),
                rx.hstack(
                    rx.button("Sign Up", size="3", variant="outline"),
                    rx.button("Log In", size="3"),
                    spacing="4",
                    justify="end",
                ),
                justify="between",
                align_items="center",
                
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.heading("Viaje a Euskal Herria", size="6", weight="bold"),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(rx.icon("menu", size=30)),
                    rx.menu.content(
                        rx.menu.item("Inicio", href=Routes.INDEX.value),
                        rx.menu.item("Día 1", href=Routes.DIAUNO.value),
                        rx.menu.item("Día 2", href=Routes.DIADOS.value),
                        rx.menu.item("Día 3", href=Routes.DIATRES.value),
                        rx.menu.item("Día 4", href=Routes.DIACUATRO.value),
                        rx.menu.item("Día 5", href=Routes.DIACINCO.value),
                        rx.menu.separator(),
                        rx.menu.item("Log in"),
                        rx.menu.item("Sign up"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        class_name="nav-footer-style rounded-2xl shadow-md border border-slate-100 hover:shadow-lg transition-shadow",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
        background_image="url('/iku.png')",
        background_size="cover",
        
    )