import reflex as rx
from rxconfig import config

from ..components import base

def home_page() -> rx.Component:
    # Welcome Page (Index)
    return base.base_page(
        rx.vstack(
            rx.heading("Welcome to your professional resume editor.", size="9", id="section1heading", align="center"),
            rx.text("Professional resume writer skilled in presenting information concisely and using niche-appropriate language, while avoiding redundancy and cliché terms.", size="6", id="section1content", align="center"),
            rx.heading("The Goal: At least get you past the Applicant Tracker System (ATS) and/or the Recruiter. But how?", size="6"),
            align="center",
        ),
    )