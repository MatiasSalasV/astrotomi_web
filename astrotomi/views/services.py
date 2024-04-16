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
                "Mentoría online",
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. ",
                "$50.000"
            )
            # card_service(
            #     "Próximament",
            #     "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. ",
            #     "$XX.XXX"
            # )
        ),
        padding=["5em 1em","6em 1em","6em 1em","10em 1em","10em 1em"],
        width="100%",
        justify="center",
        align="center",
        id="services"
    )
        
        
        
# def card_service() -> rx.Component:
#   return rx.flex(
#     rx.card(
#       rx.flex(
#         rx.box(
#           rx.icon(
#             "info",
#             width="40",
#             height="40"
#           )
#         ),
#         rx.heading(
#           "Design Services",
#           as_="h2",
#           size="3",
#           weight="bold"
#         ),
#         rx.text(
#           "High-quality UX/UI design for your digital products to enhance user            experience.",
#           as_="p",
#           size="2",
#           color="gray"
#         ),
#         rx.button(
#           "Learn More",
#           variant="solid",
#           size="2"
#         ),
#         gap="3px",
#         direction="column",
#         align="center"
#       ),
#       variant="surface",
#       size="3",
#       width="300px",
#       margin="20px"
#     ),
#     rx.card(
#       rx.flex(
#         rx.box(
#           rx.icon(
#             "info",
#             width="40",
#             height="40"
#           )
#         ),
#         rx.heading(
#           "Consulting",
#           as_="h2",
#           size="3",
#           weight="bold"
#         ),
#         rx.text(
#           "Expert advice to help you manage and implement the best strategies            for your business.",
#           as_="p",
#           size="2",
#           color="gray"
#         ),
#         rx.button(
#           "Learn More",
#           variant="solid",
#           size="2"
#         ),
#         gap="3px",
#         direction="column",
#         align="center"
#       ),
#       variant="surface",
#       size="3",
#       width="300px",
#       margin="20px"
#     ),
#     rx.card(
#       rx.flex(
#         rx.box(
#           rx.icon(
#             "info",
#             width="40",
#             height="40"
#           )
#         ),
#         rx.heading(
#           "Marketing",
#           as_="h2",
#           size="3",
#           weight="bold"
#         ),
#         rx.text(
#           "Innovative marketing solutions to increase your visibility and            engagement.",
#           as_="p",
#           size="2",
#           color="gray"
#         ),
#         rx.button(
#           "Learn More",
#           variant="solid",
#           size="2"
#         ),
#         gap="3px",
#         direction="column",
#         align="center"
#       ),
#       variant="surface",
#       size="3",
#       width="300px",
#       margin="20px"
#     ),
#     as_="section",
#     gap="4px",
#     wrap="wrap",
#     justify="center",
#     align="center"
#   )