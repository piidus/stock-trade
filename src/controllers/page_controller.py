import flet as ft
from views.first_page import FirstPage
from views.second_page import SecondPage
from views.third_page import ThirdPage
from .menu import menu

class PageController:
    def __init__(self, page: ft.Page):
        self.page = page
        self.Global = {}
        self.pages = {
            "first": FirstPage(self.page, self),
            "second": SecondPage(self.page, self),
            "third": ThirdPage(self.page, self),
        }

    def load_page(self, page_name: str):
        if page_name not in self.pages:
            self.page.controls.clear()
            self.page.controls.append(ft.Text(f"404 - Page '{page_name}' not found."))
            self.page.update()
            return

        show_back = page_name not in ["first", "second"]  # ⬅️ Your condition for no back
        self.page.appbar = menu(self, title=page_name.title(), show_back=show_back)
        self.page.controls.clear()

        page_instance = self.pages[page_name]
        if hasattr(page_instance, "did_mount"):
            page_instance.did_mount()
