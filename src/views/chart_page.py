import flet as ft
from datetime import datetime

class ChartPage:
    def __init__(self, page: ft.Page, pc):
        self.page = page
        self.pc = pc


    def did_mount(self):
        self.page.title = "Trade Chart"
        self.pc.Global["from_second"] = "Updated from Second"
        from_first = self.pc.Global.get("from_first", "No data")
        # page_size = self.pc.page_media
        # print(page_size)

        self.page.add(FirstRowDesign().build())
        self.page.update()

class FirstRowDesign:

    def container(self, text): # Removed **kwargs as not used in this example
        return ft.Container(
            border=ft.border.all(5, ft.Colors.BLUE_100),
            bgcolor=ft.Colors.GREY_300,
            # For ResponsiveRow, you typically control width with `col` on the item itself
            # rather than expand=True on the container.
            content=ft.Row(
                [
                    ft.Text(text, weight=ft.FontWeight.BOLD, overflow="visible"),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            # Add alignment for the container's content
            alignment=ft.alignment.center
        )

    def build(self):
        return ft.Container(
            padding=20,
            bgcolor=ft.Colors.CYAN_100,
            # height=100,
            content=ft.ResponsiveRow( # <--- CHANGED TO ft.ResponsiveRow
                [
                    # Each container now becomes an item in ResponsiveRow and takes a `col` property.
                    # A typical responsive grid has 12 columns.
                    # For 7 items to start on one line and then wrap,
                    # you'll need to define how many columns each takes.
                    # If you want them to be roughly equal and wrap, you can give them
                    # a size that will fit a certain number on a wider screen, and less
                    # on a narrower screen.
                    # For example, if each takes 2 columns, you can fit 6.
                    # If each takes 3 columns, you can fit 4.
                    # For 7 items, let's try to fit 3 or 4, and let them wrap.
                    # We'll use breakpoints if you want more fine-grained control,
                    # but for simple wrapping, just setting a `col` value is enough.
                    ft.Column([self.container("First")], col={"xs": 5, "sm": 6, "md": 4, "lg": 3, "xl": 2}), # Example: takes 2 columns on extra large, 3 on large, etc.
                    ft.Column([self.container("Second")], col={"xs": 5, "sm": 6, "md": 4, "lg": 3, "xl": 2}),
                    ft.Column([self.container("Third")], col={"xs": 12, "sm": 6, "md": 4, "lg": 3, "xl": 2}),
                    ft.Column([self.container("Fourth")], col={"xs": 12, "sm": 6, "md": 4, "lg": 3, "xl": 2}),
                    ft.Column([self.container("Fifth")], col={"xs": 12, "sm": 6, "md": 4, "lg": 3, "xl": 2}),
                    ft.Column([self.container("Sixth")], col={"xs": 12, "sm": 6, "md": 4, "lg": 3, "xl": 2}),
                    ft.Column([self.container("Seventh")], col={"xs": 12, "sm": 6, "md": 4, "lg": 3, "xl": 2}),
                ],
                # ResponsiveRow does not have 'alignment' in the same way Row does for content.
                # Its items naturally wrap based on the `col` values and available space.
                # If you want to align the entire row itself within its parent, you'd do that on the parent.
            ),
        )