from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class PNVCalculatorApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, PNV Calculator", halign="center")


PNVCalculatorApp().run()
