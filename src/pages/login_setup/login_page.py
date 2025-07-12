from flet import (Page, Container, Card, Column, Text, border, border_radius, 
                  Colors, alignment, CrossAxisAlignment, MainAxisAlignment,
                  TextField, IconButton, Icon, KeyboardType, NumbersOnlyInputFilter,Row,
                  ElevatedButton, Ref)

class LoginPage:
    
    def __init__(self, page: Page, **kwargs):
        self.page = page
        self.page.bgcolor = "#e6f7ff"
        self.some_value = kwargs.get("some_value", "Default Value")
        self.ip_address = kwargs.get("ip_address", "No IP Address Provided")
        self.phone_no = Ref[TextField]()
        # Attempt to get the 'windowheight' value from kwargs or default to 400
        self._page_height = float(self.page._Control__attrs.get('height', ('650', False))[0] or '600')
        self._page_width = float(self.page._Control__attrs.get('width', ('400', False))[0] or '400')
    def did_mount(self):
        ...
        # print('[LoginPage] __init__ called', self._page_height)
        # # self.page_height, self.page_width = 800,500
        # print('[windowheight]',self.page._Control__attrs['windowheight'])
        # print('[windowwidth]',self.page._Control__attrs['windowwidth'])
        # print('[height]',self.page._Control__attrs['height'])
        # print('[width]',self.page._Control__attrs['width'])
        # print('[LoginPage] did_mount called', self.page_height, self.page_width)
    def size(self, height:int = 100, width:int= 100)->int:
        new_height = float(self._page_height * (height /100))
        new_wight = self._page_width * width /100
        return new_height, new_wight
    def on_focus(self, e):
        # print(e)
        self.card.height = self.size(30, 80)[0]
        self.card.update()
    
    def go_permission_page(self, e):
        # print(self.phone_no.current.value)
        # save to session
        self.page.session.set("user_number", self.phone_no.current.value)
        self.phone_no.current.value = ""
        # print("go_permission_page")
        #Go to permission Page
        self.page.go("/permission_page")

        # self.card.update()
    
    def button_on_change(self, e):
        # print(len(self.phone_no.current.value))
        if len(self.phone_no.current.value) == 3 :
            self.card.content.controls[1].disabled = False
            self.card.update()
        else:
            self.card.content.controls[1].disabled = True
            self.card.update()
    def main_card(self):
        card_height, card_width = self.size(50, 80)
        # print(type(card_height), card_width)
        self.card= Card(content=Column(
                                # scale=0.9,
                                # width=card_width - 50,
                                adaptive=True,
                                alignment=MainAxisAlignment.CENTER,
                                controls=[TextField(
                                        label="Enter Your Phone No",
                                        keyboard_type= KeyboardType.NUMBER,
                                        input_filter=NumbersOnlyInputFilter(),
                                        on_focus=self.on_focus,
                                        on_change=self.button_on_change,
                                        border=border.all(2, Colors.BLACK),
                                        prefix= Text(value="+91", color=Colors.BLACK),
                                        ref = self.phone_no,
                                        scale=0.9,
                                        ),
                                # margin=19,
                                # height=card_height,
                                    ElevatedButton("Next", 
                                                   disabled=True,
                                                #    width=card_width-900,
                                                
                                                   on_click=self.go_permission_page,)
                                    ],
                                # width=card_width-200,
                                
                        ),
                    margin=0,
                
                   height=card_height,  
                   width=card_width,                    
                   elevation=10, 
                   adaptive=True,
                   shadow_color='5555')
        list_view = Column(
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[self.card,],
            expand=True)
        
        # def build(self):
        return list_view
    def build(self):
        # _, width = self.size(width=80)
        return Container(
            alignment=alignment.center,
            bgcolor=Colors.BLUE_GREY_100,
            border=border.all(2, Colors.BLACK),
            border_radius= border_radius.all(10),
            padding= 30,
            margin=30,
            expand_loose=True,
            expand=True,
            content=Column(controls=[ self.main_card()]))