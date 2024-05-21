import reflex as rx
#componente
from Reflex_01_Moure.components.link_button import link_button


def links() -> rx.Component:
    return rx.vstack(
        link_button("facebook", "https://www.facebook.com/luisangel.morenomorales/"),
        link_button("GitHub","https://github.com/DevEngelPy"),
        link_button("Email","jbew")
    )