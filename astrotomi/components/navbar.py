import reflex as rx
import astrotomi.styles.styles as styles
from astrotomi.components.social_media import social_media

def navbar() -> rx.Component:
  return rx.flex(
    rx.flex(
        rx.box(
            width="40px",
            height="40px",
            background_color="#0a84ff",
            border_radius="50%",
            as_="div"
        ),
        rx.link(
            "AstroTomi",
            href="http://localhost:3000/"
        ),
        align="center",
        gap="4px"
    ),    
    rx.flex(
        rx.link(
            "SOBRE MI",
            href="#about",
            align_items="center",
            style=styles.nav_link,
            display=["none", "none", "none", "flex", "flex"],
            padding_x=styles.EMSize.DEFAULT.value,
        ),
        rx.link(
            "YOUTUBE",
            href="#youtube",
            align_items="center",
            style=styles.nav_link,
            display=["none", "none", "none", "flex", "flex"],
            padding_x=styles.EMSize.DEFAULT.value,
        ),
        rx.link(
            "SERVICIOS",
            href="#services",
            align_items="center",
            style=styles.nav_link,
            display=["none", "none", "none", "flex", "flex"],
            padding_x=styles.EMSize.DEFAULT.value,
        ),
        rx.link(
            "TESTIMONIOS",
            href="#testomonials",
            align_items="center",
            style=styles.nav_link,
            display=["none", "none", "none", "flex", "flex"],
            padding_x=styles.EMSize.DEFAULT.value,
        ),  
        rx.button(
            rx.link(
                "Agenda",
                href="#services",
                display="flex",     
                align_items="center",
                color= "#fff",
            ),    
            variant="outline",
            box_shadow="0 0 6px #9d60d480",
            border="solid 1px #edb680",
            color= "#fff",
            padding=["0em 1em","0em 3em","0em 3em","0em 3em","0em 3em"],
        ),

        rx.drawer.root(
            rx.drawer.trigger(
                rx.button(
                    rx.icon(tag="menu"),
                    variant="outline",
                    border="0px",
                ),
                display=["flex", "flex", "flex", "none", "none"],
                color=styles.Color.WHITE_COLOR.value
            ),
            rx.drawer.overlay(),
            rx.drawer.portal(
                rx.drawer.content(
                    rx.vstack(
                        rx.hstack(
                            rx.avatar(
                                src="/astrotomi.PNG", 
                                bg="linear-gradient(90deg, rgba(94,106,110,1) 0%, rgba(51,17,187,1) 100%)",
                                size="9",
                                fallback="AT",
                                radius="full",
                                margin="1em",
                                border = "2px solid #3442BD"
                            ),
                            rx.flex(
                                rx.drawer.close(
                                    rx.box(
                                        rx.button(
                                            rx.icon(tag="x"),
                                            variant="ghost",
                                            
                                            color_scheme="amber"
                                        )
                                    )
                                ),
                                align_items="start",
                            ),
                            justify="between",
                            width="100%"
                        ),
                        rx.text(
                            """
                            Me gusta crear vídeos que exploran tanto la asombrosa vastedad del cosmos como el 
                            potencial ilimitado del desarrollo personal.
                            """,
                            color=styles.Color.PURPLE_COLOR.value,
                            font_size="1.05em",
                            padding_top=styles.EMSize.DEFAULT.value,
                            padding_bottom=styles.EMSize.SMALL.value
                        ),
                        rx.text(
                            """
                           ¿Preparado para expandir tu mente y 
                            sumergirte en un universo de posibilidades?
                            """,
                            color=styles.Color.PURPLE_COLOR.value,
                            font_size="1.05em",
                            padding_bottom=styles.EMSize.LARGE.value
                        ),
                        rx.text(
                            "ENCUENTRAME EN",
                            weight="bold",
                            color=styles.Color.WHITE_COLOR.value,
                        ),
                        
                        rx.flex(
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
                            wrap="wrap",
                            justify="start"
                        ),
                    ),
                        
                    height="100%",
                    width="85%",
                    padding="1.5em",
                    background="radial-gradient(66.51% 75.22% at .48% 101.69%,rgba(149,59,181,.3) 0%,#ffffff10 100%),linear-gradient(107.33deg,#264d99 0%,#05050a 47.75%)"
                )
            ),
            direction="left",
        ),

        gap="10px"
    ),
    
    as_="nav",
    align="center",
    justify="between",
    border= "1px solid #3442BD",
    box_shadow= "0 -3px 20px #9fa9ff40,0 4px 20px #9fa9ff40",
    border_radius= '24px',
    bg="radial-gradient(66.51% 75.22% at .48% 101.69%,rgba(149,59,181,.3) 0%,#ffffff10 100%),linear-gradient(107.33deg,#264d99 0%,#05050a 47.75%)",
    position="sticky", 
    top="2em",            
    zIndex="1000",      
    padding="1em",
    max_width="1350px",
    width="100%" ,

    
    
        
  )