import reflex as rx

def top() -> rx.Component:
    return rx.vstack(
        rx.avatar(name="Luis", size="9"),
        rx.text("@engel"),
        rx.text("Mi Alias Es: DevEngelPy"),
        justify="center",
        margin_left="160px"
    )