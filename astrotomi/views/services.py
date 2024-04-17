import reflex as rx
import astrotomi.styles.styles as styles
from astrotomi.components.card_service import card_service

def services() -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.text(
                "SERVICIOS",
                color_scheme="amber",
                size="4",
            ),
            rx.heading(
                "Mentorías de Astrofísica",
                color=styles.Color.TITLE_COLOR.value,
                size="8",
                weight="bold",
                padding_y=styles.EMSize.SMALL.value
            ),
            rx.text(
                "Si quieres aprender un tema en especifico sobre el universo, te creamos una clase personalizada según tú nivel y requerimientos.",
                color=styles.Color.PURPLE_COLOR.value,
                font_size="1.25em",
            ),
            max_width="100ch",
            padding_y="2em"
        ),
        rx.hstack(
            card_service(
                "Mentoría 1 a 1",
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. ",
                "$50.000",
                "https://calendly.com/"
            ),
            card_service(
                "Academia de Astrofísica",
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. ",
                "$75.000",
                "https://calendly.com/"
            ),
            flex_direction=["column","column","column","row","row"],
        ),
        padding=["5em 1em","6em 1em","6em 1em","10em 1em","10em 1em"],
        width="100%",
        justify="center",
        align="center",
        id="services"
    )