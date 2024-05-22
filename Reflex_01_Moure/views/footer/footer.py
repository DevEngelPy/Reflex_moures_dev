import reflex as rx
#componente
from Reflex_01_Moure.components.footer import footers
def footer() -> rx.Component:
    return rx.vstack(footers())