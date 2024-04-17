import reflex as rx
import astrotomi.styles.styles as styles

def card_about() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.avatar(
                src="/astrotomi.PNG", 
                bg="linear-gradient(90deg, rgba(94,106,110,1) 0%, rgba(51,17,187,1) 100%)",
                size="9",
                fallback="AT",
                radius="full",
                margin="1em",
                border = "2px solid #3442BD"
            ),
            rx.box(
                rx.heading(
                    "Hola, soy Tomás Fuentes 👋",
                    size="8",
                    margin_bottom="8px",
                    weight="bold",
                    color=styles.Color.TITLE_COLOR.value
                ),
                rx.text(
                    """
                    Un apasionado por la astrofísica y la creación de contenido. 
                    Una de mis mayores metas es enseñar lo que he ido aprendiendo 
                    sobre el universo, a través de videos en mi canal de YouTube y 
                    clases personalizadas.
                    """,
                    size="3",
                    padding_y="0.5em",
                    color=styles.Color.PURPLE_COLOR.value,
                    # font_size=["1em","1.25em"]
                    font_size="1.25em"
                ),
                rx.text(
                    """
                    Soy Licenciado en Astrofísica por la UTFSM, 
                    con experiencia en diversas áreas de estudio, desde física introductoria 
                    hasta formación planetaria y extragaláctica. Actualmente mi enfoque investigativo 
                    se centra en zonas de formación estelar en galaxias a bajo redshift.

                    """,
                    as_="p",
                    size="3",
                    padding_y="0.5em",
                    color=styles.Color.PURPLE_COLOR.value,
                    font_size="1.25em"
                ),
                # rx.text(
                #     """
                #         AstroTomii es un proyecto dedicado a compartir desarrollo personal, financiero y mentalidad, también documento mi carrera como astrofísico. Uno de mis sueños de niño fue ser Youtuber, 
                #         actualmente estoy muy interesado en la creación de contenido y edición de video. Herramientas con las cuales emprendí denuevo un canal.
                #     """,
                #     as_="p",
                #     size="3",
                #     padding_y="0.5em",
                #     color=styles.Color.PURPLE_COLOR.value,
                #     font_size="1.25em"
                # ),
                
                padding_y="1em",
            ),
            gap="4px",
            align="center",
            flex_direction=["column","column","column","row","row"],
        ),
        
        color="#FFFFFF",
        padding="20px",
        style=styles.card_style
    )