import reflex as rx
import astrotomi.styles.styles as styles

def social_media(
        icon=str,
        shadow=str,
        url=str
) -> rx.Component:
    return rx.link(
        rx.box(
            rx.center(
                rx.avatar(
                    src=icon,
                    size="3",
                ),
                width="100%",
                height="100%",
            ),
            bg="radial-gradient(circle at top right, #1b2157, #000000)",
            box_shadow=shadow,
            border_radius="100%",
            width = "75px",
            height="75px",
            margin = "1em",
            style={
                "transition": "transform 0.5s ease",  # Agrega una transición suave para la propiedad transform
            },
            _hover={
                "transform": "scale(1.1)",
                
            }
        ),
        is_external=True,
        href=url
    )

