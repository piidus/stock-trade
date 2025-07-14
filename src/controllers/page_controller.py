import flet as ft
from views.first_page import FirstPage
from views.second_page import SecondPage
from views.third_page import ThirdPage
from controllers.menu import MenuBar

class PageController:
    def __init__(self, page: ft.Page):
        self.page = page
        self.Global = {}
        self.menu_class = MenuBar

        self.pages = {
            "first": FirstPage(self.page, self),
            "second": SecondPage(self.page, self),
            "third": ThirdPage(self.page, self),
        }

    def load_page(self, page_name: str):
        if page_name in self.pages:
            self.page.controls.clear()
            self.pages[page_name].did_mount()
        else:
            self.page.controls.clear()
            self.page.controls.append(ft.Text(f"404 - Page '{page_name}' not found."))
            self.page.update()
