import flet as ft
from flet import Text, Colors

import flet as ft
from flet import AppBar, Text, IconButton, Icons, Colors


class MenuBar:
    def __init__(self, pc, role: str):
        self.pc = pc
        self.role = role

    def get_appbar(self):
        if self.role == "admin":
            actions = [
                IconButton(icon=Icons.HOME, on_click=lambda _: self.pc.page.go("auth")),
                IconButton(icon=Icons.CHARGING_STATION_OUTLINED, on_click=lambda _: self.pc.page.go("chart")),
                IconButton(icon=Icons.EDIT, on_click=lambda _: self.pc.page.go("third")),
            ]
        elif self.role == "user":
            actions = [
                IconButton(icon=Icons.HOME, on_click=lambda _: self.pc.page.go("auth")),
                IconButton(icon=Icons.CHARGING_STATION_OUTLINED, on_click=lambda _: self.pc.page.go("chart")),
            ]
        else:
            actions = []

        return AppBar(title=Text("Tester"), bgcolor=Colors.CYAN_800, actions=actions)
