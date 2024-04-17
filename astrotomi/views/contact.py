import reflex as rx
import astrotomi.styles.styles as styles

from astrotomi.components.social_media import social_media

def contact() -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.text(
                "REDES DE CONTACTO",
                color_scheme="amber",
                size="4",
            ),
            rx.heading(
                "Lorem ipsum dolor sit amet, consectetur adipiscing",
                color=styles.Color.TITLE_COLOR.value,
                size="8",
                weight="bold",
                padding_y=styles.EMSize.SMALL.value
            ),
            rx.text(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit, Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. ",
                color=styles.Color.PURPLE_COLOR.value,
                font_size="1.25em",
            ),
            max_width="100ch",
            padding_y="2em"
        ),
        rx.hstack(
            social_media(
                "/icons/youtube.svg",
                "rgba(255, 0, 0, 0.5) 0px 4px 20px, rgba(255, 255, 255, 0.7) -1px 0px 4px",
                "https://www.youtube.com/@astrotomii"
            ),
            social_media(
                "/icons/instagram.svg",
                "rgb(229, 53, 171) 0px 4px 20px, rgba(255, 255, 255, 0.7) -1px 0px 4px",
                "https://www.instagram.com/astrotomi"
            ),
            social_media(
                "/icons/gmail.svg",
                "rgb(255, 255, 255) 0px 4px 20px, rgba(255, 255, 255, 0.7) -1px 0px 4px",
                """
                    mailto:tomas.fuentesf@usm.cl?subject=Consulta Servicios AstroTomii&body=Hola,
                    estoy interesado/a en tus servicios de mentorías de astrofísica y me gustaría recibir más información al respecto. 
                    ¿Podrías enviarme detalles sobre sus servicios, disponibilidad y precios?
                """,
            ),


            justify="center",
            align="center",
            width="100%",
        ),
        padding="1em",
        width="100%",
        justify="center",
        align="center",
        id="contact"

    )




