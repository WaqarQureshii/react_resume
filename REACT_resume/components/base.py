import reflex as rx

from .navbar import navbar_buttons

def base_page(child: rx.Component, *args) -> rx.Component:
    if not isinstance(child, rx.Component):
        child = rx.heading("This is not a valid child element.")
    return rx.fragment(
        navbar_buttons(),
        rx.box(
            child,
            rx.color_mode.button(position="bottom-right"),
            size='4',
            padding="10em",
            width="100%",
            id="main_content_element",
        )
    )