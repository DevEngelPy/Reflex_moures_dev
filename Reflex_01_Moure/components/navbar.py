import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
                "DevEngelPy",
                heigth="40em"
                ),
        position="sticky",
        bg="#3398FF",
        padding_x="16px",
        padding_y="8px",
        z_index="999"
    )