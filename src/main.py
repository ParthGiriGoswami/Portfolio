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
    education_cards = ft.ResponsiveRow([ft.Card(
            content=ft.Container(content=ft.Column([
                    ft.Text("B.Tech in Computer Science", weight=ft.FontWeight.BOLD, size=20),
                    ft.Text("Graphic Era Hill University, Bhimtal"),
                    ft.Text("CGPA: 7.67", color=ft.Colors.BLUE_700),
                    ft.Text("Graduated: 2025", italic=True, size=12, color=ft.Colors.GREY)
                ], spacing=5), padding=11)),
        ft.Card(content=ft.Container(content=ft.Column([
                    ft.Text("Senior Secondary", weight=ft.FontWeight.BOLD, size=20),
                    ft.Text("Army Public School, Almora"),
                    ft.Text("Percentage: 74.4%", color=ft.Colors.BLUE_700),
                    ft.Text("Year: 2021", italic=True, size=12, color=ft.Colors.GREY)
                ], spacing=5), padding=11)),
        ft.Card(content=ft.Container(content=ft.Column([
                    ft.Text("High School", weight=ft.FontWeight.BOLD, size=20),
                    ft.Text("Army Public School, Almora"),
                    ft.Text("Percentage: 85.2%", color=ft.Colors.BLUE_700),
                    ft.Text("Year: 2019", italic=True, size=12, color=ft.Colors.GREY)
                ], spacing=5),padding=11)),
    ], spacing=10)
    ski = ft.Text("Skills", size=second_text_size, weight=ft.FontWeight.W_600, text_align="center")
    skilist=ft.Column([
        ft.ListTile(title=ft.Text("• Python")),
        ft.ListTile(title=ft.Text("• Java")),
        ft.ListTile(title=ft.Text("• MySQL")),
        ft.ListTile(title=ft.Text("• NoSQL")),
    ])
    pro = ft.Text("Projects", size=second_text_size, weight=ft.FontWeight.W_600, text_align="center")
    project_cards = ft.ResponsiveRow([
        ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Text("B.Tech in Computer Science", weight=ft.FontWeight.BOLD, size=20),
                    ft.Text("Graphic Era Hill University, Bhimtal"),
                    ft.Text("CGPA: 7.68", color=ft.Colors.BLUE_GREY_700),
                    ft.Text("Graduated: 2025", italic=True, size=12, color=ft.Colors.GREY)
                ], spacing=5), padding=11)),
        ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Text("B.Tech in Computer Science", weight=ft.FontWeight.BOLD, size=20),
                    ft.Text("Graphic Era Hill University, Bhimtal"),
                    ft.Text("CGPA: 7.68", color=ft.Colors.BLUE_GREY_700),
                    ft.Text("Graduated: 2025", italic=True, size=12, color=ft.Colors.GREY)
                ], spacing=5), padding=11)),
        ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Text("12th Grade (Science)", weight=ft.FontWeight.BOLD, size=20),
                    ft.Text("Army Public School, Almora"),
                    ft.Text("Percentage: 75.8%", color=ft.Colors.BLUE_GREY_700),
                    ft.Text("Year: 2021", italic=True, size=12, color=ft.Colors.GREY)
                ], spacing=5), padding=11)),
        ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Text("10th Grade", weight=ft.FontWeight.BOLD, size=20),
                    ft.Text("Army Public School, Almora"),
                    ft.Text("Percentage: 85.4%", color=ft.Colors.BLUE_GREY_700),
                    ft.Text("Year: 2019", italic=True, size=12, color=ft.Colors.GREY)
                ], spacing=5),padding=11)),
    ], spacing=10)
    layout = ft.Container(content=ft.Column([
            ft.Row([profile_icon], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([intro], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([txt], alignment=ft.MainAxisAlignment.CENTER),
            ft.Divider(), ft.Row([edu], alignment=ft.MainAxisAlignment.CENTER),
            education_cards, ft.Divider(), ski, skilist, ft.Divider(),
            ft.Row([pro], alignment=ft.MainAxisAlignment.CENTER), project_cards
        ], horizontal_alignment="center"),
        padding=ft.padding.only(top=30),
        alignment=ft.alignment.center,
        expand=True
    )
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
        txt.size = second_text_size
        edu.size=second_text_size
        pro.size=second_text_size
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