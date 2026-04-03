import reflex as rx

def navbar():
    return rx.hstack(
        rx.heading("🤖 AI Document Search", color="white", size="5", font_weight="bold"),
        rx.spacer(),
        rx.hstack(
            rx.link("Home", href="/", color="white", font_weight="medium", _hover={"color": "#60a5fa"}),
            rx.link("Upload Document", href="/upload", color="white", font_weight="medium", _hover={"color": "#60a5fa"}),
            rx.link("Chat", href="/chat", color="white", font_weight="medium", _hover={"color": "#60a5fa"}),
            rx.link("History", href="/history", color="white", font_weight="medium", _hover={"color": "#60a5fa"}),
            rx.link("About", href="/about", color="white", font_weight="medium", _hover={"color": "#60a5fa"}),
            spacing="6",
        ),
        bg="#1e3a8a",  # Dark blue like screenshot
        padding="16px 40px",
        width="100%",
        align_items="center",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1)",
        position="sticky",
        top="0",
        z_index="1000",
    )