from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.core.window import Window
from kivy.graphics import Rectangle, Color

from kivy.lang import builder


def load_lang(file_name):
    lang = {}
    exec(open(file_name, encoding="utf-8").read(), lang)
    return lang

def action(label, org, translate):
    def change(obj):
        if label.text == org:
            label.text = translate
        else:
            label.text = org
    return change


class CarouselApp(App):
    def build(self):
         carousel = Carousel(direction='right')
         lang=load_lang("lang/rus/config.py")
       # lang = {"translate":  {'а': {'translation': 'a', 'word': 'мама'}, 'б': {'translation': 'b', 'word': 'бумага'}}}


        with carousel.canvas:
            Color(1,1,1)
            Rectangle(source="img/tlo.png", pos=carousel.pos,size=Window.size)

        #return carousel
        for litera in lang["translate"]:
            litera_tlumaczenie = lang["translate"][litera]["translation"]
            layout = builder.Builder.load_file("learn_layout.kv")
            


        return carousel

if __name__ =="__main__":
    CarouselApp().run()