from flet import (Page, Container,Text, ListView, border, border_radius, ElevatedButton,
                  Colors, padding, Row, Switch, PermissionType, PermissionStatus, PermissionHandler)
# from utilities import create_folder, create_logger

class PermissionPage:
    
    def __init__(self, page: Page, **kwargs):
        self.page = page
        self.permission_handler = PermissionHandler()
        self.page.overlay.append(self.permission_handler)

    def did_mount(self):
        # self.disable_button.disabled = False
        pass
    



    def request_permission(self, e):
        o = self.permission_handler.request_permission(e.control.data)
        
        self.page.add(Text(f"Requested to {e.control.data.name}: {o}"))
    # check storage permission first get permission > create folder and make database
    def storage_click(self, e):
        # print("storage_click")
        # print(e.control.value)
        if e.control.value:
            self.request_permission(e)
            # create folder and make database
            # create_folder()
            # create_folder(folder_name="INCHAT/logs")
            # self.log = create_logger()
            # self.log.info("storage permission granted")
            self.__container.disabled = False
            self.__container.update()
            
            
    def other_permissions_click(self, e):
        self.request_permission(e)
        self.log.info(f"other permission granted -- {e.control.data.name}")

    def heading(self):
        return Text("Permission Page", text_align="center")
    def storage_permission(self):
        switch = Switch(value=False, scale=0.8,
                        data = PermissionType.STORAGE,
                         on_change=self.storage_click)

        row = Row(controls=[Text("Storage Permission"), switch])
        container = Container(
            bgcolor=Colors.BLUE_GREY_100,
            border=border.all(2, Colors.BLACK),
            border_radius=border_radius.all(10),
            padding=padding.all(10),
            content=row,
        )
        return container
    
    def contact_permission(self):
        switch = Switch(value=False, scale=0.8,
                        data = PermissionType.CONTACTS,
                         on_change=self.other_permissions_click)

        row = Row(controls=[Text("Contact Permission"), switch])
        self.__container = Container(
            bgcolor=Colors.BLUE_GREY_100,
            border=border.all(2, Colors.BLACK),
            border_radius=border_radius.all(10),
            padding=padding.all(10),
            content=row,
            disabled=True
        )
        return self.__container
    
    def build(self):
        return ListView(controls=[self.heading(), self.storage_permission(), self.contact_permission()])