import reflex as rx
from enum import Enum

MAX_WIDTH = "1350px"

class Color(Enum):
    TITLE_COLOR="rgb(232 236 254 / 0.8)"
    TOPTITLE_COLOR="linear-gradient(93.69deg, #EDB680 4.17%, rgba(242, 124, 98, 0.97526) 100.02%)"
    PURPLE_COLOR="rgb(167 180 251 / 1)"
    WHITE_COLOR = "rgb(232 236 254 / 1)"

    PRIMARY = "#47BFBD"
    SECONDARY = "#119fbb"
    BACKGROUND = "#ecf0f3"
    CONTENT = "#171F26"
    BACKGROUND_GRADIENT = "linear-gradient(145deg, #e2e8ec, #ffffff)"
    OPACO = "#3c3e41"

class EMSize(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    BIGGER = "4em"

BASE_STYLE = {
    "background-image": "url('/bg.svg')",
    "background-size": "cover",
    "background-attachment": "fixed",

    rx.link: {
        "color":Color.WHITE_COLOR.value,
        "text_decoration": "none",
        "_hover": {
            # "color":Color.PRIMARY.value,
            "transition": "background-color 0.4s ease",
        },
        "transition":"background-color 0.4s ease",
    }
}


nav_link = dict(
    font_weight = "bold",
    border_radius=".75rem",
    # padding=".5rem 1rem",
    color="rgb(221 227 254 / 1)",
    _hover= {
        "bg": "#4a4d89",
    }
    # color = 
)

card_style = dict(
    background_image="radial-gradient(66.51% 75.22% at .48% 101.69%, rgba(149, 59, 181, .3) 0%, rgba(255, 255, 255, .063) 100%), linear-gradient(180deg, rgba(0, 0, 0, .38) .05%, rgba(0, 0, 0, 0) 86.64%);",
    box_shadow= "0 0 #0000, 0 0 #0000,0 25px 50px -12px rgb(0 0 0 / .25)",
    border_top = "1px solid",
    border_right = "1px solid",
    border_radius = "20px ",
    border_color= "rgba(185, 191, 245, 0.5)",
)


card_video_style = dict(
    height= "20rem",
    box_shadow = "0 0 #0000, 0 0 #0000, 0 2px 10px 0 #c8c8c8e3",
    border_radius = "20px ",
    
)