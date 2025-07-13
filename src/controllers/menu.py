import flet as ft
from flet import Text, Colors

def menu(pc, title: str, show_back: bool = False):
    actions = []

    if show_back:
        actions.append(
            ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                on_click=lambda _: pc.page.go("/second"),  # 👈 or use a stack if dynamic
            )
        )

    return ft.AppBar(leading=ft.IconButton(icon=ft.Icons.HOME_FILLED, on_click=lambda _: pc.page.go("/")), 
        title=Text(title), bgcolor=Colors.CYAN_800, actions=actions)
