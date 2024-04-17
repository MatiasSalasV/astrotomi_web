import reflex as rx
import astrotomi.styles.styles as styles

def card_service(
        title:str,
        description:str,
        value:str,
        url:str
    ) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.heading(
                    title,
                    size="7",
                    weight="bold",
                    color=styles.Color.TITLE_COLOR.value
                ),
                rx.spacer(),
                rx.badge(
                    rx.text(value),
                    radius="full",
                    bg="#4a4d89",
                    color="white",
                    size="2",
                ),
                align="center",
                width="100%"
            ),
            rx.text(
                description,
                size="3",
                padding_y="0.5em",
                color=styles.Color.PURPLE_COLOR.value,
                # font_size=["1em","1.25em"]
                font_size="1.25em"
            ),
            rx.list(
                rx.list.item(
                    rx.icon("check", color="violet"),
                    " Aprendizaje asegurado",
                ),
                rx.list.item(
                    rx.icon("check", color="violet"),
                    " Equipo capacitado",
                ),
                rx.list.item(
                    rx.icon("check", color="violet"),
                    " Facilidades de pago",
                ),
                padding_y = "1em"
            ),
            rx.button(
                rx.link(
                    "Agenda AHORA",
                    href=url,
                    is_external=True
                ),
                variant="solid",
                size="3",
                width="100%",
                box_shadow="0 2px 20px 6px #fef6b280",
                border="solid 2px #fff",
                bg="linear-gradient(93.69deg, #edb680 4.17%, rgba(242, 124, 98, .67526) 100.02%)",
                transition="background 0.3s ease, box-shadow 0.3s ease",
                _hover={
                    "transition": "background 0.3s ease, box-shadow 0.3s ease",
                    "background": "linear-gradient(93.69deg, #d97a5f 4.17%, rgba(242, 124, 98, .85) 100.02%)",  # Oscurecer ligeramente el color de fondo al hacer hover
                    "box_shadow": "0 2px 30px 8px #fef6b2",
                }
            ),
            padding="2em 1.5em"
        ),
        max_width="470px",
        width="100%",
        color="#FFFFFF",
        # margin_bottom = "1em",
        margin=["1em 0","1em 0","1em"],
        style=styles.card_style
    )