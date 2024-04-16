import reflex as rx
import astrotomi.styles.styles as styles

from astrotomi.components.card_video import card_video

def youtube() -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.text(
                "CREACIÓN DE CONTENIDO",
                color_scheme="amber",
                size="4",
            ),
            rx.heading(
                "Divulgación de la astronomía, crecimiento personal y temas varios",
                color=styles.Color.TITLE_COLOR.value,
                size="8",
                weight="bold",
                padding_y=styles.EMSize.SMALL.value
            ),
            rx.text(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. ",
                color=styles.Color.PURPLE_COLOR.value,
                font_size="1.25em",
            ),
            max_width="100ch",
            padding_y="2em"
        ),

        rx.hstack(
            rx.vstack(
                card_video(
                    "Mi tesis de astrofísica | Resumen",
                    "photos/video.png",
                    "https://www.youtube.com/watch?v=QnVPnO8lzok"
                ),
                card_video(
                    "Como es estudiar astronomía en Chile",
                    "photos/video2.png",
                    "https://www.youtube.com/watch?v=ho5W4mK9hyg"
                ),
            ),
            rx.vstack(
                card_video(
                    "Guía para Principiantes en INVERSIONES 2024",
                    "photos/video3.png",
                    "https://www.youtube.com/watch?v=Rgm9SGDzRFg"
                ),
                card_video(
                    "7 CONSEJOS para ser una Persona de Valor",
                    "photos/video4.png",
                    "https://www.youtube.com/watch?v=RvTenp6xAcw"
                ),
            ),
            flex_direction=["column","column","column","row","row"],
        ),
        
        padding="1em",
        width="100%",
        justify="center",
        align="center",
        id="youtube"
    )