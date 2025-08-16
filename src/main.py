import flet as ft
import asyncio
async def main(page: ft.Page):
    page.title = "Portfolio"
    page.padding = 0
    page.scroll = "adaptive"
    profile_size = 380
    text_size = 40
    second_text_size = 40
    profile_icon = ft.Container(
        content=ft.Icon(ft.Icons.PERSON, size=profile_size, color=ft.Colors.WHITE),
        width=profile_size, height=profile_size, bgcolor=ft.Colors.BLUE_GREY_900,
        border_radius=200, alignment=ft.alignment.center)
    intro = ft.Text("Hello Guys, I am Parth Giri and I am", size=text_size, weight=ft.FontWeight.W_600, text_align="center")
    txt = ft.Text("", size=second_text_size, weight=ft.FontWeight.W_600, text_align="center")
    edu = ft.Text("Educational Details", size=second_text_size, weight=ft.FontWeight.W_600, text_align="center")
    education_cards = ft.ResponsiveRow([
        ft.Card(content=ft.Container(content=ft.Column([
            ft.Text("B.Tech in Computer Science", weight=ft.FontWeight.BOLD, size=20),
            ft.Text("Graphic Era Hill University, Bhimtal"),
            ft.Text("CGPA: 7.67", color=ft.Colors.BLUE_700),
            ft.Text("Graduated: 2025", italic=True, size=12, color=ft.Colors.GREY)
        ], spacing=5), padding=11),margin=ft.Margin(20,0,20,10)),
        ft.Card(content=ft.Container(content=ft.Column([
            ft.Text("Senior Secondary", weight=ft.FontWeight.BOLD, size=20),
            ft.Text("Army Public School, Almora"),
            ft.Text("Percentage: 74.4%", color=ft.Colors.BLUE_700),
            ft.Text("Year: 2021", italic=True, size=12, color=ft.Colors.GREY)
        ], spacing=5), padding=11),margin=ft.Margin(20,0,20,10)),
        ft.Card(content=ft.Container(content=ft.Column([
            ft.Text("High School", weight=ft.FontWeight.BOLD, size=20),
            ft.Text("Army Public School, Almora"),
            ft.Text("Percentage: 85.2%", color=ft.Colors.BLUE_700),
            ft.Text("Year: 2019", italic=True, size=12, color=ft.Colors.GREY)
        ], spacing=5),padding=11),margin=ft.Margin(20,0,20,10)),
    ], spacing=10)
    ski = ft.Text("Skills", size=second_text_size, weight=ft.FontWeight.W_600, text_align="center")
    skilist=ft.Column([
        ft.ListTile(title=ft.Text("• Python")), ft.ListTile(title=ft.Text("• Java")),
        ft.ListTile(title=ft.Text("• MySQL")), ft.ListTile(title=ft.Text("• NoSQL")),])
    pro = ft.Text("Projects", size=second_text_size, weight=ft.FontWeight.W_600, text_align="center")
    def create_project_card(title, tech, details, repo_url=None):
        return ft.Card( content=ft.Container( content=ft.Column([
                    ft.Text(title, weight=ft.FontWeight.BOLD, size=20),
                    ft.Text(f"• Technologies / Frameworks: {tech}"),
                    *[ft.Text(f"• {d}", italic=True, size=12, color=ft.Colors.GREY) for d in details]
                ], spacing=5), padding=20, on_click=lambda e: e.page.launch_url(repo_url)),
            margin=ft.Margin(20, 0, 20, 10))
    project_cards = ft.ResponsiveRow([
        create_project_card("Dictionary (May 2023-April 2023)", "Python, CustomTkinter, SQL Server",
            ["Designed and implemented a dictionary application with functionality to add, edit, and delete words.",
                "Built a user-friendly GUI using CustomTkinter for seamless interaction."],
            "https://github.com/ParthGiriGoswami/Dictionary.git"),
        create_project_card( "Chatbot (Aug 2023-Sep 2023)", "Python, Flet",
            [ "Developed a chatbot capable of real-time conversations within a custom-built chat interface.",
                "Integrated intelligent response handling for natural user interaction."],
            "https://github.com/ParthGiriGoswami/Chatbot.git"),
        create_project_card( "Text Summarization (May 2024-June 2024)", "Python, Tkinter, HuggingFace Transformers",
            ["Built an AI-powered tool to summarize lengthy texts into concise, readable summaries.",
                "Utilized Transformer-based NLP models for high-accuracy text compression and GUI integration using CustomTkinter."],
            "https://github.com/ParthGiriGoswami/Text-Summarization.git"),
        create_project_card( "Antivirus Scanner (August 2024-June 2025)", "Python, Flet, OS, Psutil, Cryptography",
            ["Created a cross-platform antivirus scanner for detecting and managing malware.",
                "Implemented real-time system monitoring and secure file handling using Psutil and Cryptography libraries.",
                "Developed an interactive GUI with Flet for scanning, exclusion lists, and device monitoring."],
            "https://github.com/ParthGiriGoswami/Antivirus.git"),
        create_project_card( "Portfolio Website (July 2025)", "Python, Flet, Docker",
            [ "Designed and deployed a personal portfolio website showcasing projects, skills, and education.",
                "Implemented a responsive UI with Flet and deployed via Docker for cross-platform accessibility."],
            "https://github.com/ParthGiriGoswami/Portfolio.git")], spacing=10)
    layout = ft.Container(content=ft.Column([
            ft.Row([profile_icon], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([intro], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([txt], alignment=ft.MainAxisAlignment.CENTER),
            ft.Divider(), ft.Row([edu], alignment=ft.MainAxisAlignment.CENTER),
            education_cards, ft.Divider(), ski, skilist, ft.Divider(),
            ft.Row([pro], alignment=ft.MainAxisAlignment.CENTER), project_cards
        ], horizontal_alignment="center"), padding=ft.padding.only(top=30), 
        alignment=ft.alignment.center, expand=True)
    page.add(layout)
    def resize(e):
        nonlocal profile_size, text_size, second_text_size
        width = page.window.width
        if width < 500:
            second_text_size=40
            text_size = 22
        elif width < 900: 
            second_text_size=75
            text_size = 60
        else:
            second_text_size=75
            text_size = 60
        profile_icon.width = profile_icon.height = profile_size
        profile_icon.content.size = profile_size
        intro.size = text_size
        txt.size = edu.size=pro.size=ski.size=second_text_size
        page.update()
    page.on_resize = resize
    resize(None)  
    async def typewrite(text, delay=0.12):
        for ch in text:
            txt.value += ch
            txt.update()
            await asyncio.sleep(delay)
    async def backspace(n, delay=0.1):
        for _ in range(n):
            txt.value = txt.value[:-1]
            txt.update()
            await asyncio.sleep(delay)
    while True:
        await typewrite("Python Developer")
        await asyncio.sleep(0.4)
        await backspace(len("Python Developer"))
        await typewrite("AI Trainee Engineer")
        await asyncio.sleep(0.4)
        await backspace(len("AI Trainee Engineer"))
ft.app(main)