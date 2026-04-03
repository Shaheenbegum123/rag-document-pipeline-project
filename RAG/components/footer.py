import reflex as rx

def footer():
    return rx.box(
        rx.vstack(
            rx.divider(border_color="#334155"),
            rx.hstack(
                rx.text("AI Document Search", font_weight="700", color="#60a5fa", font_size="20px"),
                rx.spacer(),
                rx.text(
                    "© 2026 • Intelligent RAG Assistant • Built with Reflex",
                    color="#64748b",
                    font_size="15px"
                ),
                width="88%",
                align_items="center",
                padding_y="36px",
            ),
            bg="#0a0f1c",
            width="100%",
        ),
        width="100%",
    )