from reflex import center
from reflex_viaje.navigation.routes import Routes
from reflex_viaje.navigation.state import NavState
from ..pages.auth.login import LoginState
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
                rx.cond(
                    LoginState.logged_in,
                    rx.hstack(
                        rx.cond(LoginState.usuario == "miranda@tello.es",
                            rx.vstack(
                                rx.text(f"Hola, {LoginState.usuario}", size="2", color="white"),
                                rx.image(
                                    src="/miranda.png",
                                    width="50px",
                                    height="50px",
                                    
                                ),
                                align_items="center",  
                            ),
                        ),
                        rx.cond(LoginState.usuario == "sancho@sancho.es",
                            rx.vstack(
                                rx.text(f"Hola, {LoginState.usuario}", size="2", color="white"),
                                rx.image(
                                    src="/sancho.png",
                                    width="50px",
                                    height="50px",
                                    
                                ),
                                align_items="center",  
                            ),
                        ),
                        rx.cond(LoginState.usuario == "almela@almela.es",
                           
                                rx.vstack(
                                    rx.text(f"Hola, {LoginState.usuario}", size="2", color="white"),
                                    rx.image(
                                        src="/almela.png",
                                        width="50px",
                                        height="50px",
                                        
                                    ),
                                    align_items="center",    
                                ),
                            
                        ),    
                        rx.button(
                            "Salir",
                            variant="surface",
                            size="2",
                            color_scheme="ruby",
                            on_click=LoginState.logout,
                        ),
                        spacing="4",
                        align_items="center",
                    ),
                    rx.hstack(
                        rx.button("Sign Up", size="3", variant="outline", on_click=NavState.to_signup),
                        rx.button("Log In", size="3", on_click=NavState.to_login()),
                        spacing="4",
                        justify="end",
                    )
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
                        rx.menu.item("Inicio", on_click=NavState.to_index()),
                        rx.menu.item("Día 1", on_click=NavState.to_diauno()),
                        rx.menu.item("Día 2", on_click=NavState.to_diados()),
                        rx.menu.item("Día 3", on_click=NavState.to_diatres()),
                        rx.menu.item("Día 4", on_click=NavState.to_diacuatro()),
                        rx.menu.item("Día 5", on_click=NavState.to_diacinco()),
                        rx.menu.separator(),
                        rx.menu.item("Log in", on_click=NavState.to_login()),
                        rx.menu.item("Sign up", on_click=NavState.to_signup()),
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