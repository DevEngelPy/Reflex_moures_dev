import reflex as rx #frameword
#componentes
from Reflex_01_Moure.components.navbar import navbar
#vistas
from Reflex_01_Moure.views.headers.header import top
from Reflex_01_Moure.views.links.link import links
from Reflex_01_Moure.views.footer.footer import footer
#estilos
import Reflex_01_Moure.styles.generic_styles as style
from Reflex_01_Moure.styles.generic_styles import Spacer 



def index() -> rx.Component:
    return rx.box(
        navbar(),
            rx.vstack(
                    top(),
                    links(),
                    #estilo manera 01
                    max_width = style.MAX_WIDTH,
                    width="100%",
                    margin_y=Spacer.BIG.value,
                    margin_x="500px"
                ),
        footer()
    )


app = rx.App(
    style=style.BASE_STYLE
)
app.add_page(index)
app._compile()  