import reflex as rx
import astrotomi.styles.styles as styles

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
        # rx.link(
        #     "LO QUE HAGO",
        #     # href="#features",
        #     align_items="center",
        #     style=styles.nav_link,
        #     display=["none", "none", "none", "flex", "flex"],
        #     padding_x=styles.EMSize.DEFAULT.value,
        # ),
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
            # padding="1em",
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
                                fallback="ASTTO",
                                size="8",
                                color_scheme="amber"
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
                            "Digitalizo y automatizo tu negocio con IA, brindándote la ventaja de liderar tu sector.",
                            color=styles.Color.WHITE_COLOR.value,
                            padding_y=styles.EMSize.LARGE.value
                        ),
                        rx.vstack(
                            rx.link(
                                "SOBRE MI",
                                # href="#about",
                                align_items="center",
                                style=styles.nav_link,
                                padding_x=styles.EMSize.DEFAULT.value,
                            ),
                            rx.link(
                                "LO QUE HAGO",
                                # href="#features",
                                align_items="center",
                                style=styles.nav_link,
                                padding_x=styles.EMSize.DEFAULT.value,
                            ),
                            rx.link(
                                "YOUTUBE",
                                # href="#youtube",
                                align_items="center",
                                style=styles.nav_link,
                                padding_x=styles.EMSize.DEFAULT.value,
                            ),
                            rx.link(
                                "CONTÁCTAME",
                                href="#contact",
                                align_items="center",
                                style=styles.nav_link,
                                padding_x=styles.EMSize.DEFAULT.value,
                            ),   
                            align_items="start",
                        ),
                        # rx.text(
                        #     "ENCUENTRAME EN",
                        #     # font_weight=FontWeight.MEDIUM.value,
                        #     # color=TextColor.TEXT.value
                        # ),
                        
                        # rx.hstack(
                        #     icon_link_button(
                        #         "linkedin", 
                        #             const.LINKEDIN_URL,
                        #             "LinkedIn"
                        #         ),
                        #         icon_link_button(
                        #             "youtube",
                        #             const.YOUTUBE_URL,
                        #             "YouTube"
                        #         ),
                        #         icon_link_button(
                        #             "twitter", 
                        #             const.TWITTER_URL,
                        #             "Twitter"
                        #         ), 
                        #     ),
                    ),
                        
                    height="100%",
                    width="85%",
                    padding=styles.EMSize.LARGE.value,
                    background_color="rgba(41,43,84, 0.6)"
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