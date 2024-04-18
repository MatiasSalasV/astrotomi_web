import reflex as rx
import astrotomi.styles.styles as styles

def card_testimonials(
        nombre:str,
        ocupacion:str,
        testimonio:str,
    ) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.box(
                rx.flex(
                    rx.box(
                        rx.icon(
                            "circle-user-round",                            
                            width="48px",
                            height="48px",
                            color="var(--orange-8)"
                            # color="orange"
                            
                        ),
                        # padding="0.2em",
                        border_radius="50%",
                        bg="radial-gradient(66.51% 75.22% at .48% 101.69%,rgba(149,59,181,.3) 0%,#ffffff10 100%),linear-gradient(107.33deg,#264d99 0%,#05050a 47.75%)",
                        # border = "2px solid #3442BD"
                    ),
                    # rx.avatar(
                    #     size="3",
                    #     src=foto,
                    #     fallback="AT",
                        
                    # ),
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