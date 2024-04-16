import reflex as rx
import astrotomi.styles.styles as styles
from astrotomi.components.card_about import card_about

def about() -> rx.Component:
    return rx.vstack(
        card_about()   ,
        # rx.box(height="100vh"),
        padding=["5em 1em","6em 1em","6em 1em","10em 1em","10em 1em"],
        align="center",
        id="about"
        
    )