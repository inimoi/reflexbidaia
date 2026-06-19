from reflex_viaje.navigation.routes import Routes
import reflex as rx
from ...pages.auth.login import LoginState


def protected_page(content: rx.Component) -> rx.Component:
    """
    Componente que protege una página.
    Si no está autenticado, redirige a login.
    """

    return rx.cond(
        LoginState.logged_in,
        content,
    )
