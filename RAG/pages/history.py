import reflex as rx
from RAG.components.navbar import navbar
from RAG.components.footer import footer
from RAG.states.rag_state import ChatState
from RAG.pages.chat import message_bubble

def index():
    return rx.vstack(
        navbar(),
        rx.center(
            rx.vstack(
                rx.heading("Conversation History", color="#e0f2fe", font_size="42px", font_weight="700"),
                rx.box(
                    rx.foreach(ChatState.history, message_bubble),
                    height="68vh",
                    overflow_y="auto",
                    padding="32px",
                    width="100%",
                    bg="#0f172a",
                    border_radius="28px",
                    box_shadow="0 30px 70px -15px rgba(59, 130, 246, 0.4)",
                ),
                width="88%",
                spacing="6",
                margin_top="30px",
            )
        ),
        footer(),
        min_height="100vh",
        background="linear-gradient(135deg, #0a0f1c 0%, #1e3a8a 100%)",
        spacing="0",
    )