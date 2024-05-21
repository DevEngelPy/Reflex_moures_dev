import reflex as rx #frameword
#componentes
from Reflex_01_Moure.components.navbar import navbar
#vistas
from Reflex_01_Moure.views.headers.header import top
from Reflex_01_Moure.views.links.link import links

def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.box(
            top(),
            links()
        )
    )


app = rx.App()
app.add_page(index)
app._compile()  