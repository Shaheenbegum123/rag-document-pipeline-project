import reflex as rx
from RAG.components.navbar import navbar
from RAG.components.footer import footer

def index():
    return rx.vstack(
        navbar(),
        rx.center(
            rx.hstack(
                # Left Side - Text
                rx.vstack(
                    rx.heading(
                        "AI Document Search",
                        font_size="62px",
                        font_weight="900",
                        color="#e0f2fe",
                        line_height="1.05",
                        text_shadow="0 12px 50px rgba(59, 130, 246, 0.7)",
                    ),
                    rx.text(
                        "Chat with Your Documents using AI",
                        font_size="31px",
                        color="#bae6fd",
                        font_weight="700",
                        margin_top="10px",
                    ),
                    rx.text(
                        "Upload PDFs, DOCX, PPTX or TXT files once.\n"
                        "Ask any question — our intelligent RAG AI delivers accurate answers with sources.",
                        font_size="20px",
                        color="#94a3b8",
                        white_space="pre-line",
                        line_height="1.65",
                        margin_top="24px",
                        max_width="520px",
                    ),

                    # Buttons (ONLY TWO NOW)
                    rx.hstack(
                        rx.button(
                            "Get Started",
                            on_click=rx.redirect("/upload"),
                            bg="linear-gradient(135deg, #3b82f6, #1e40af)",
                            color="white",
                            size="4",
                            font_weight="700",
                            padding_x="54px",
                            padding_y="18px",
                            border_radius="20px",
                            _hover={"transform": "translateY(-6px)", "box_shadow": "xl"}
                        ),
                        rx.button(
                            "Start Chatting",
                            on_click=rx.redirect("/chat"),
                            variant="outline",
                            color="#60a5fa",
                            border_color="#60a5fa",
                            border_width="2.5px",
                            size="4",
                            font_weight="700",
                            padding_x="46px",
                            padding_y="18px",
                            border_radius="20px",
                            _hover={"bg": "#1e40af", "color": "white"}
                        ),

                        spacing="6",
                        margin_top="50px",
                    ),

                    align_items="start",
                    spacing="5",
                    width="50%",
                ),

                # Right Side - Robot Image
                rx.box(
                    rx.image(
                        src="/robot.png",
                        alt="AI Robot Reading Document",
                        width="460px",
                        height="440px",
                        object_fit="cover",
                        border_radius="28px",
                        box_shadow="0 30px 70px -15px rgba(59, 130, 246, 0.7)",
                    ),
                    width="46%",
                    display="flex",
                    justify_content="center",
                ),

                width="90%",
                max_width="1300px",
                align_items="center",
                spacing="8",
                margin_top="50px",
            )
        ),
        footer(),
        min_height="100vh",
        background="linear-gradient(135deg, #0a0f1c 0%, #1e3a8a 100%)",
        spacing="0",
    )