from sqlite3 import SQLITE_CREATE_INDEX
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton as FB

class DemoApp(MDApp):
    def build(self):
        screen = Screen()

        B1 = FB(
            text='Button',
            pos_hint={'center_x':0.5,'center_y':0.9},
            text_color=(1, 1, 0, 1)
            )
        L1 = MDLabel(
            text="SOS",
            halign='center',
            pos_hint={'center_x':0.5, 'center_y':0.95},
            theme_text_color='Custom',
            text_color=(0, 0.5, 0.5, 1),
            font_style='H3'
            )

        screen.add_widget(B1)
        screen.add_widget(L1)
        return screen

DemoApp().run()