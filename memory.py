import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.widget import Widget

def load_lang(file_name):
    lang = {}
    exec(open(file_name, encoding="utf-8").read(), lang)
    return lang

class memoryWidget(Widget):
    pass

class MemoryApp(App):

    def build(self):
        return CustomWidget()

memoryWidget = MemoryApp()
memoryWidget.run()