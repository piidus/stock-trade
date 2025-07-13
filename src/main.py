from flet import Page, run
from controllers.page_controller import PageController

def main(page: Page):
    pc = PageController(page)

    def route_change(e):
        route_name = e.route.strip("/") or "first"
        pc.load_page(route_name)

    page.on_route_change = route_change
    page.go(page.route)

run(main)
