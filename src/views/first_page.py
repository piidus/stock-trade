import flet as ft

class FirstPage:
    def __init__(self, page: ft.Page, pc):
        self.page = page
        self.pc = pc

    def did_mount(self):
        self.page.title = "First Page"
        def set_role(e):
            role = role_field.value.strip().lower()
            if role in ["user", "admin"]:
                self.pc.Global["role"] = role
                self.page.appbar = self.pc.menu_class(self.pc, role).get_appbar()
                self.pc.load_page("second")
            else:
                self.page.controls.clear()
                self.page.controls.append(ft.Text("❌ Invalid role. Please enter 'user' or 'admin'."))
                self.page.update()

        role_field = ft.TextField(label="Enter role (user/admin)")
        self.page.controls.clear()
        self.page.controls.append(role_field)
        self.page.controls.append(ft.ElevatedButton(content=ft.Text("Submit"), on_click=set_role))
        self.page.update()
