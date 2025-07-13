import flet as ft
from datetime import datetime

class SecondPage:
    def __init__(self, page: ft.Page, pc):
        self.page = page
        self.pc = pc

    def did_mount(self):
        self.page.title = "Second Page"
        self.pc.Global["from_second"] = "Updated from Second"
        from_first = self.pc.Global.get("from_first", "No data")

        self.page.add(ft.Text(f"{datetime.now()}"))
        self.page.add(ft.Text(f"Received: {from_first}"))
        self.page.add(
            ft.TextButton(
                content=ft.Text("Go to Third Page"),
                on_click=lambda _: self.page.go("/third"),
            )
        )
        self.page.update()
