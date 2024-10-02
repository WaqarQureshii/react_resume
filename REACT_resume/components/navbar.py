import reflex as rx

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="bold"), href=url
    )


def navbar_buttons() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="./EatHumbleFinPyLogo.png",
                        width="7.00em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.vstack(
                        rx.heading(
                            "REACT",
                            size='8',
                            weight="bold"
                        ),
                        rx.heading(
                            "Resume Enhancement and Customization Tool",
                            size='4',
                            weight="medium",
                            color_scheme="blue",
                        )
                    ),
                    align_items="center",
                    wrap="nowrap"
                ),
                rx.hstack(
                    navbar_link("Home", "/"),
                    navbar_link("Why is there a paid component?", "/how_i_tried_keeping_it_free"),
                    navbar_link("Your Account", "/Account"),
                    spacing="6",
                ),
                rx.hstack(
                    rx.button("Log In With Google", size="3", color_scheme="red"),
                    spacing="4",
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="./EatHumbleFinPyLogo.png",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Reflex", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Home"),
                        rx.menu.item("About"),
                        rx.menu.item("Why is there a paid component?"),
                        rx.menu.item("Contact"),
                        rx.menu.separator(),
                        rx.menu.item("Log In With Google"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        width="100%",
        # position="fixed",
        # z_index="1"
    )