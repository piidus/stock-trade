import flet as ft
from flet import Page,  AppView, app
from controllers.page_controller import PageController
import warnings
warnings.filterwarnings("ignore")

def main(page: Page):
    pc = PageController(page)

    def route_change(e):
        """
        This function is called whenever the app's route changes.
        It will take the route and strip any leading or trailing slashes,
        and then use that string as the name of the page to load.
        If the route is empty, it defaults to "auth".
        """
        route_name = e.route.strip("/") or "auth"
        pc.load_page(route_name)

    page.on_route_change = route_change
    page.go(page.route)

# app(target=main, view=ft.AppView.WEB_BROWSER, port=5000)#(main )#, view=ft.AppView.WEB_BROWSER)#, web_renderer=ft.WebRenderer.SKWASM)
# for mobile: 
app(target=main, view=ft.AppView.FLET_APP)