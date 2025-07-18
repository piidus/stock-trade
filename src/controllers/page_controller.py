import flet as ft
# from views.auth_page import FirstPage
from views.chart_page import ChartPage
from views.third_page import ThirdPage
from controllers.menu import MenuBar
from views import AuthPage

class PageController:
    def __init__(self, page: ft.Page):
        self.page = page
        # self.page_media = page.media
        self.Global = {}
        self.menu_class = MenuBar

        self.pages = {
            "auth": AuthPage(self.page, self),
            "chart": ChartPage(self.page, self),
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
