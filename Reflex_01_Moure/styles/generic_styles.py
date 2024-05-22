from enum import Enum
import reflex as rx
#ejemplo 1
MAX_WIDTH="600px"
#tamaños
class Spacer(Enum):
    SMALL = "8px" #->0.5em
    DEFAUL = "16px" #->1em
    BIG = "32px" #->2em

#style base
BASE_STYLE={
    rx.button:{
        "width":"100%",
        "heigth":"100%",
        "display":"block",
        "padding":Spacer.SMALL.value,
        "border_radius":Spacer.DEFAUL.value
    },
    rx.link:{
        "text_decoration":"none",
        "_hover":{}
    }
}

