import reflex as rx
import astrotomi.styles.styles as styles
from astrotomi.components.card_testimonials import card_testimonials

def testimonials() -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.text(
                "TESTIMONIOS",
                color_scheme="amber",
                size="4",
            ),
            rx.heading(
                "Experiencias Reales, Sin Filtros",
                color=styles.Color.TITLE_COLOR.value,
                size="8",
                weight="bold",
                padding_y=styles.EMSize.SMALL.value
            ),
            rx.text(
                "Desde estudiantes hasta soñadores que han encontrado su lugar en el cosmos, estas historias te invitan a sumergirte en el poder del conocimiento y la autoexploración.",
                color=styles.Color.PURPLE_COLOR.value,
                font_size="1.25em",
            ),
            max_width="100ch",
            padding_y="2em"
        ),
        rx.flex(
            card_testimonials(
                "Maximiliano Puramarino",
                "Mentoría 1 a 1",
                """Las clases estuvieron 10/10. Me gustó mucho que fueran personalizadas ya nadie 
                ofrece eso acá en temas de astrofísica. Las presentaciones de PowerPoint demasiado 
                buenas, y la explicación y forma de enseñar también excelente de verdad. Lo recomiendo 
                mucho para cualquiera que quisiera aprender astrofísica, y tomaría clases denuevo si o sii 👍🏿👍🏿    
                """,
            ),
            card_testimonials(
                "Persona 2",
                "Mentoría 1 a 1",
                "Texto de prueba para ver el testimonio con letra curva tipo citación externa entre doble comillas como un texto citado para testimonio",
            ),
            card_testimonials(
                "Persona 3",
                "Academia de Astrofísica",
                "Texto de prueba para ver el testimonio con letra curva tipo citación externa entre doble comillas como un texto citado para testimonio",
            ),
            card_testimonials(
                "Persona 4",
                "Academia de Astrofísica",
                "Texto de prueba para ver el testimonio con letra curva tipo citación externa entre doble comillas como un texto citado para testimonio",
            ),
            wrap="wrap",
            justify="center"
        ),
        padding=["1em 1em 5em 1em","1em 1em 6em 1em","1em 1em 6em 1em","1em 1em 10em 1em","1em 1em 10em 1em"],
        width="100%",
        justify="center",
        align="center",
        id="testomonials"
    )