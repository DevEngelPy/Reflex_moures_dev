import reflex as rx
import Reflex_01_Moure.styles as styles

def link_icon()->rx.Component:
    return rx.link(
        rx.icon(
            tag="link"
        )
    )
