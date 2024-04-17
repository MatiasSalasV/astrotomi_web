import reflex as rx
import astrotomi.styles.styles as styles

def header() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.heading(
                "Explora el universo con AstroTomii",
                font_size=["1.1em","1.5em","2em"],
                color=styles.Color.TITLE_COLOR.value,
                padding_y=["0em","0.1em"],
            ),
            rx.heading(
                "Aprende Astrofísica ",
                font_size=["2em","3em","3.8em"],
                # font_size = ["2.5em","3em","3.5em"],
                color=styles.Color.TITLE_COLOR.value,
                # color_scheme="white",
                padding_bottom=["0em","0.3em"],
                # background="linear-gradient(to right, #e1e1e1, #757575)",
                # background_clip="text"
                
            ),
            rx.heading(
                "de Manera Simple",
                font_size=["2em","3em","4em"],
                # font_size=["2em","2.5em","2em"],
                color=styles.Color.TITLE_COLOR.value,
                # padding_y=["0em","0.1em"],
                
            ),
            rx.text(
                """
                Únete a mis cursos y talleres interactivos diseñados para desatar 
                tu curiosidad y llevar tus conocimientos del cosmos al siguiente nivel. 
                Perfecto para estudiantes, aficionados y futuros científicos.
                """,
                size="4",
                color="rgb(187 198 253 / 1)",
                max_width="61ch",
                padding_y="1em",
            ),
            rx.button(
                rx.link(
                    "Agenda una ASESORÍA",
                    href="#services",
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
            background="linear-gradient(to right, #e1e1e1, #757575)",
            background_clip="text"
        ),

        rx.vstack(
            rx.image(
                # src="/1.svg",
                src="/space3.png",
                # max_width="800px",
                width="300px",
                height="auto"
            ),
            # align="center",
            # justify="center",
            padding="2em"
        ),

        flex_direction=["column","column","column","row","row"],
        padding=["5em 1em","6em 1em","6em 1em","10em 1em","10em 1em"],
        align="center",
        justify="center",
        width="100%",
        id="inicio"
        
    )












rx.box(
        rx.flex(
            rx.vstack(
                rx.heading(
                    "Become an expert React Native developer faster",
                    size="6",
                    align="center",
                    color="white",
                    max_width="600px"
                ),
                rx.text(
                    "From fundamentals to publishing iOS & Android apps, Galaxies helps you          to become a React Native developer fast.",
                    size="4",
                    align="center",
                    color="white",
                    max_width="600px"
                ),
                rx.button(
                    "Start for FREE",
                    variant="solid",
                    size="3",
                    color="orange"
                ),
            ),
            
            rx.image(
                src="/space3.png",
                # height="400px"
            ),
            
        
            align="center",
            justify="center",
            width="100%",
            flex_direction=["column","column","column","row","row"],
        )
    )
