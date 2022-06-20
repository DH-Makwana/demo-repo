from ctypes import alignment
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class DemoApp(MDApp):
    def build(self):
        
        L1 = MDLabel(
            text="Hello world !!",
            halign='center',
            theme_text_color='Custom',
            text_color=(0, 0.5, 0.5, 1)
        )

        return L1

DemoApp().run()