import reflex as rx
from RAG.components.navbar import navbar
from RAG.components.footer import footer
from RAG.states.rag_state import ChatState, MODEL_OPTIONS

def message_bubble(msg):
    is_user = (msg["role"] == "user")
    return rx.hstack(
        rx.cond(is_user, rx.spacer(), rx.fragment()),
        rx.box(
            rx.markdown(msg["content"]),
            bg=rx.cond(is_user, "linear-gradient(135deg, #3b82f6, #2563eb)", "#1e2937"),
            color=rx.cond(is_user, "white", "#e5e7eb"),
            padding="18px 24px",
            border_radius="22px",
            max_width="76%",
            box_shadow="0 15px 35px -10px rgba(0,0,0,0.4)",
        ),
        rx.cond(~is_user, rx.spacer(), rx.fragment()),
        width="100%",
        padding_y="4",
        justify=rx.cond(is_user, "end", "start"),
    )

def index():
    return rx.vstack(
        navbar(),
        rx.box(
            rx.foreach(ChatState.history, message_bubble),
            height="68vh",
            overflow_y="auto",
            padding="32px",
            width="88%",
            bg="#0f172a",
            border_radius="28px",
            box_shadow="0 30px 70px -15px rgba(59, 130, 246, 0.4)",
            border="1px solid rgba(147, 197, 253, 0.25)",
            margin_top="30px",
        ),
        rx.form.root(
            rx.vstack(
                rx.hstack(
                    rx.text("Model:", font_weight="700", color="#e0f2fe", font_size="18px"),
                    rx.select(
                        MODEL_OPTIONS,
                        value=ChatState.selected_model_label,
                        on_change=ChatState.set_selected_model_label,
                        size="3",
                        style={"background": "#1e2937", "color": "white", "border": "2px solid #60a5fa", "border_radius": "14px", "width": "420px"}
                    ),
                    width="88%",
                ),
                rx.hstack(
                    rx.input(
                        placeholder="Ask anything about your documents...",
                        value=ChatState.question,
                        on_change=ChatState.set_question,
                        width="100%",
                        height="64px",
                        style={"border_radius": "18px", "border": "2px solid #475569", "background": "#1e2937", "color": "white"}
                    ),
                    rx.button("Send", type="submit", bg="#3b82f6", color="white", height="64px", padding_x="40px", border_radius="18px", font_weight="700"),
                    width="88%",
                ),
                width="100%",
                align_items="center",
            ),
            on_submit=ChatState.ask,
        ),
        footer(),
        align_items="center",
        width="100%",
        min_height="100vh",
        background="linear-gradient(135deg, #0a0f1c 0%, #1e3a8a 100%)",
        spacing="0",
    )