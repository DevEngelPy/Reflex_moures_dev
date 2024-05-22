import reflex as rx
#componente
from Reflex_01_Moure.components.link_button import link_button
#styles


def links() -> rx.Component:
    return rx.vstack(
        link_button("facebook", "https://www.facebook.com/luisangel.morenomorales/", "facebook"),
        link_button("GitHub","https://github.com/DevEngelPy", "github"),
        width="100%",
    )