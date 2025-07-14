import flet as ft

class ThirdPage:
    def __init__(self, page: ft.Page, pc):
        self.page = page
        self.pc = pc

    def did_mount(self):
        data = self.pc.Global.get("from_second", "No data")
        self.page.title = "Third Page"
        self.page.add(ft.Text(f"Third Page\nGot from second: {data}"))
        self.page.update()
