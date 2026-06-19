import reflex as rx
from . import routes

class NavState(rx.State):
    def to_index(self):
        return rx.redirect(routes.Routes.INDEX.value)

    def to_login(self):
        return rx.redirect(routes.Routes.LOGIN.value)
    
    def to_fotosdestinos(self):
        return rx.redirect(routes.Routes.FOTOSDESTINOS.value)
    
    def to_gastos(self):
        return rx.redirect(routes.Routes.GASTOS.value)

    def to_fotosviaje(self):
        return rx.redirect(routes.Routes.FOTOSVIAJE.value)
    
    def to_diauno(self):
        return rx.redirect(routes.Routes.DIAUNO.value)
    
    def to_diados(self):
        return rx.redirect(routes.Routes.DIADOS.value)
    
    def to_diatres(self):
        return rx.redirect(routes.Routes.DIATRES.value)
    
    def to_diacuatro(self):
        return rx.redirect(routes.Routes.DIACUATRO.value)
    
    def to_diacinco(self):
        return rx.redirect(routes.Routes.DIACINCO.value)
    
    def to_signup(self):
        return rx.redirect(routes.Routes.INDEX.value)
 