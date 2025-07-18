

import flet as ft
import requests
import jwt
class LoginCard_Design:
    def __init__(self, on_login_click):
        self.on_login_click = on_login_click
        # Store references to the text fields
        self.email_field = ft.CupertinoTextField(placeholder_text="Email", value="sudiipkumarbasu@gmail.com", keyboard_type=ft.KeyboardType.EMAIL)
        self.password_field = ft.TextField(label="Password", value="12345678", password=True, keyboard_type=ft.KeyboardType.TEXT)

    def build(self):
        return ft.Container(
            adaptive=True,
            # alignment=ft.alignment.center,
            blend_mode=ft.BlendMode.DARKEN,
            border=ft.border.all(1, ft.Colors.BLUE_600),
            border_radius=20,
            bgcolor=ft.Colors.YELLOW_100,
            padding=20,
            content=ft.Column(
                [
                    self.email_field,    # Use the stored reference
                    self.password_field, # Use the stored reference
                    ft.ElevatedButton("Login", on_click=self.on_login_click),
                ],
                # alignment=ft.MainAxisAlignment.END,
                # horizontal_alignment=ft.CrossAxisAlignment.END
            ),
        )

class AuthPage:
    def __init__(self, page: ft.Page, pc):
        self.page = page
        self.pc = pc
        self.login_card_design = None # To store the instance of LoginCard_Design

    def _login_button_clicked(self, e):
        """
        This function will be called when the Login button is clicked.
        Now we can access the values of the text fields.
        """
        if self.login_card_design: # Ensure login_card_design is initialized
            email = self.login_card_design.email_field.value
            password = self.login_card_design.password_field.value

            # print(f"Email: {email}")
            # print(f"Password: {password}")

            # You can now use 'email' and 'password' for your login logic
            if email and password :
                # try to login
                try:
                    response = requests.post("https://mtf.piidus.in/api/customer", json={"email": email, "password": password})
                    
                except Exception as e:
                    print(e)
                else:
                    response_json = response.json()
                    print(response_json)
                    session_token = response_json.get("session_token")
                    self.pc.Global["session_token"] = session_token
                    # decode the session token
                    decoded_token = jwt.decode(session_token, "hardsecretkey", algorithms=["HS256"])
                    print(decoded_token)
                    # also save in local storage
                    # self.page.client_storage.set("session_token", session_token)
                    
                    # add menu bar
                    self.page.appbar = self.pc.menu_class(self.pc, "admin").get_appbar()
                    self.page.go("chart")
                    # self.page.update()
            else:
                self.snack_bar = ft.SnackBar(
                    content=ft.Text("Invalid credentials."),
                    bgcolor=ft.Colors.RED_500,
                    visible=True
                )
                self.page.open(self.snack_bar)
            

    def did_mount(self):
        self.page.title = "Authentication"
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        # print(self.page.client_storage)
        # print(self.page.client_storage.get("session_token"))
        # print(self.pc.Global)
        # if self.page.client_storage.get("session_token"):
        #     # add menu bar
        #     self.page.appbar = self.pc.menu_class(self.pc, "admin").get_appbar()
        #     self.page.go("/chart")
            
        # else:
        # Create the LoginCard_Design instance and store it
        self.login_card_design = LoginCard_Design(on_login_click=self._login_button_clicked)
        self.page.add(self.login_card_design.build())
        self.page.update()