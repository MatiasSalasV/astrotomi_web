import reflex as rx
import astrotomi.styles.styles as styles
from astrotomi.components.social_media import social_media

def footer() -> rx.Component:
    return rx.vstack(
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
        ),

        rx.text(
            "© 2024 AstroTomii. Todos los derechos reservados.",
            align="center"
        ),
        width="100%",
        justify="center",
        text_align="center",
        align="center",
        color=styles.Color.WHITE_COLOR.value,
        id="contact"
    )