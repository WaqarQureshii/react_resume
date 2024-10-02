import reflex as rx

from rxconfig import config

from .components import navbar, base
from . import pages

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.heading("TEST")

app = rx.App(
    theme=rx.theme(appearance="dark",
                   accent_color="blue",
                   gray_color="slate",
                   )
)

app.add_page(index)
app.add_page(pages.home_page, "/")
app.add_page(pages.why_page, "/how_i_tried_keeping_it_free")
app.add_page(pages.account_page, "/Account")

