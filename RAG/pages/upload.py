import reflex as rx
from RAG.components.navbar import navbar
from RAG.components.footer import footer
from RAG.states.rag_state import ChatState

def index():
    return rx.vstack(
        navbar(),
        rx.center(
            rx.vstack(
                rx.heading("Upload Your Documents", font_size="46px", font_weight="800", color="#e0f2fe"),
                rx.text(
                    "Securely upload files. Our AI will index them for smart search.",
                    font_size="19px",
                    color="#94a3b8",
                    margin_bottom="40px"
                ),
                rx.upload(
                    rx.vstack(
                        rx.icon("upload", size=52, color="#60a5fa"),
                        rx.button("📤 Select Files", bg="#3b82f6", color="white", size="4", font_weight="700", border_radius="16px"),
                        rx.text("or drag & drop your files here", color="#64748b", font_weight="500"),
                        align="center",
                        spacing="5",
                    ),
                    id="doc_upload",
                    multiple=True,
                    padding="6.5em",
                    border="3px dashed #60a5fa",
                    border_radius="28px",
                    bg="#1e2937",
                    width="500px",
                    on_drop=ChatState.handle_upload(rx.upload_files(upload_id="doc_upload")),
                    _hover={"border_color": "#bae6fd", "bg": "#334155"},
                ),
                # Success Dialog (styled attractively)
                rx.alert_dialog.root(
                    rx.alert_dialog.content(
                        rx.alert_dialog.title("✅ Upload Complete!", color="#4ade80", font_weight="700"),
                        rx.alert_dialog.description("Your documents are now ready for AI search.", color="#cbd5e1"),
                        rx.hstack(
                            rx.alert_dialog.cancel(rx.button("Upload More", variant="outline")),
                            rx.alert_dialog.action(rx.button("Go to Chat", on_click=rx.redirect("/chat"), bg="#3b82f6")),
                        ),
                        bg="#0f172a",
                        border_radius="24px",
                        padding="40px",
                    ),
                    open=ChatState.show_upload_dialog,
                ),
                rx.text("Uploaded Files:", font_size="18px", font_weight="600", color="#e0f2fe", margin_top="30px"),
                rx.foreach(ChatState.uploaded_files, lambda f: rx.text(f, color="#94a3b8")),
                spacing="6",
                align_items="center",
            )
        ),
        footer(),
        min_height="100vh",
        background="linear-gradient(135deg, #0a0f1c 0%, #1e3a8a 100%)",
        spacing="0",
    )