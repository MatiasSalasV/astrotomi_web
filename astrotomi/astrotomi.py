import reflex as rx
import astrotomi.styles.styles as styles
from astrotomi.components.navbar import navbar
from astrotomi.views.header import header
from astrotomi.views.about import about
from astrotomi.views.youtube import youtube
from astrotomi.views.contact import contact
from astrotomi.views.services import services
from astrotomi.views.footer import footer

def index() -> rx.Component:
    return rx.box(
        # navbar(),
        # rx.center(
        #     navbar(),
        #     # padding_top="2em"
        #     padding="0"

        # ),
        rx.center(
            rx.vstack(
                navbar(),
                header(),
                about(),
                youtube(),
                services(),
                # contact(),
                footer(),
                max_width=styles.MAX_WIDTH,
                width="100%",
            ),
            
        ),
        padding=["1em","2em"]
    )


app = rx.App(
    style=styles.BASE_STYLE,
)
app.add_page(index)
