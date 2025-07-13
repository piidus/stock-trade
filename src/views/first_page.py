import flet as ft
from datetime import datetime

class FirstPage:
    def __init__(self, page: ft.Page, pc):
        self.page = page
        self.pc = pc

    def did_mount(self):
        self.page.title = "First Page"
        print(f'[first_page] {self.pc.Global}')
        self.pc.Global["from_first"] = "Sent from First Page"
        self.page.add(ft.Text(f"{datetime.now()}"))
        self.page.add(
            ft.TextButton(
                content=ft.Text("Go to Second Page"),
                on_click=lambda _: self.page.go("/second"),
            )
        )
        self.page.update()

