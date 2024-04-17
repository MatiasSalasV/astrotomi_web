import reflex as rx
import astrotomi.styles.styles as styles

def card_video(
        title:str,
        image:str,
        url:str
    ) -> rx.Component:
    return rx.box(
        rx.link(
            rx.vstack(
                rx.badge(
                    rx.flex(
                        rx.icon(
                            tag="youtube",
                        ),
                        rx.text("Video"),
                        spacing="1",
                        align="center"
                    ),
                    # color_scheme="amber",
                    radius="full",
                    bg="#4a4d89",
                    variant="solid",
                    color="white"
                    # size="2",
                ),
                rx.box(
                    rx.heading(
                        title,
                        padding_y=styles.EMSize.SMALL.value
                        # size="2",
                        # margin_bottom="24px"
                    ),
                    rx.flex(
                        rx.avatar(
                            size="3",
                            src="/astrotomi.PNG",
                            fallback="AT",
                            radius="full",
                            width="48px",
                            height="48px",
                            border = "2px solid #3442BD"
                        ),
                        rx.text(
                            "AstroTomi",
                            size="3",
                            # weight="bold"
                        ),
                        gap="0.5em",
                        align="center"
                    ),
                ),
                justify="between",
                height="100%",
                padding="2em",
                
                transition="transform 0.3s ease",
                _hover={
                    "transform": "scale(0.98)",
                    "text_shadow":"0 -3px 20px #4a4d89,0 4px 20px #4a4d89",
                    "background_color": "rgba(0, 0, 0, 0.5)",
                    "border_radius" :"20px "
                }
            ),
            href=url,
            is_external=True
        ),
        background= f"linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), center/cover url({image})",        
        max_width="460px",
        width="100%",
        margin=["1em 0","1em 0","1em"],
        color=styles.Color.TITLE_COLOR.value,
        style=styles.card_video_style,
    
    )
















rx.card(
        rx.flex(
            rx.flex(
                rx.text(
                    rx.icon(
                        "video"
                    ),
                    "Video",
                    # color="purple",
                    size="2",
                    background_color="#8A70FF",
                    border_radius="9999px",
                    padding="4px 8px"
                ),
                gap="2px",
                align="center"
            ),

            justify="between",
            align="center"
        ),
        rx.heading(
            "Expo Router Fullstack Apps",
            size="3",
            color="white",
            margin_top="12px"
        ),
        rx.flex(
            rx.text(
                rx.box(
                    src="https://raw.githubusercontent.com/magicpatterns/catalog/main/public/placeholder.png",
                    alt="React",
                    width="24px",
                    height="24px",
                    as_="img"
                ),
                "React",
                as_="div",
                size="2",
                display="flex",
                align_items="center",
                gap="4px"
            ),
            rx.text(
                rx.box(
                    src="https://raw.githubusercontent.com/magicpatterns/catalog/main/public/placeholder.png",
                    alt="TypeScript",
                    width="24px",
                    height="24px",
                    as_="img"
                ),
                "TS",
                as_="div",
                size="2",
                display="flex",
                align_items="center",
                gap="4px"
            ),
            gap="2px",
            align="center",
            margin_top="12px"
        ),
        rx.flex(
            rx.avatar(
                src="https://raw.githubusercontent.com/magicpatterns/catalog/main/public/placeholder.png",
                alt="Simon Grimm",
                size="3",
                radius="full"
            ),
            rx.text(
                "SIMON GRIMM",
                size="2"
            ),
            rx.badge(
                "PRO",
                color="purple",
                variant="solid"
            ),
            gap="2px",
            align="center",
            margin_top="12px"
        ),
        max_width="572",
        background="linear-gradient(145deg, #6C5DD3, #1E0E62)",
        border_radius="12px",
        padding="24px",
        box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)"
    )