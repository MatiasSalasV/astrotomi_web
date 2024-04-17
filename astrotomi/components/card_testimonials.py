import reflex as rx
import astrotomi.styles.styles as styles

def card_testimonials(
        nombre:str,
        ocupacion:str,
        testimonio:str,
        foto:str
    ) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.box(
                rx.flex(
                    rx.avatar(
                        size="3",
                        src=foto,
                        fallback="AT",
                        radius="full",
                        width="48px",
                        height="48px",
                        border = "2px solid #3442BD"
                    ),
                    rx.vstack(
                        rx.heading(
                            nombre,
                            size="4",
                            trim="both",
                            weight="medium",
                        ),
                        rx.text(
                            ocupacion,
                            size="2",
                            trim="both",
                            color=styles.Color.PURPLE_COLOR.value
                        ),
                    ),
                    gap="0.5em",
                    align="center"
                ),
            ),
            rx.text(
                f'"{testimonio}"',
                padding_y=styles.EMSize.SMALL.value,
                font_style="Italic"
            ),   
            padding="2em 1.5em"
        ),
        max_width="470px",
        width="100%",
        color="#FFFFFF",
        margin=["1em 0","1em 0","1em"],
        style=styles.card_style
    )