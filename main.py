from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.core.window import Window
from kivy.graphics import Rectangle, Color
from kivy.core.audio import SoundLoader
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

def play_sound(plik):
    def play_action(obj):
        if plik is None: return
        sound = SoundLoader.load(plik)
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()
    return play_action

class CarouselApp(App):
    def build(self):
        carousel = Carousel(direction='right')
        lang=load_lang("lang/rus/config.py")
        # lang = {"translate":  {'а': {'translation': 'a', 'word': 'мама'}, 'б': {'translation': 'b', 'word': 'бумага'}}}


        with carousel.canvas:
            Color(1,1,1)
            Rectangle(source="img/tlo.png", pos=carousel.pos,size=Window.size)

        for litera in lang["translate"]:
            litera_tlumaczenie = lang["translate"][litera]["translation"]
            layout = builder.Builder.load_file("learn_layout.kv")
            carousel.add_widget(layout)

            slowo = layout.ids.slowo
            duza_litera = layout.ids.duza_litera
            duza_litera = layout.ids['duza_litera'] # komenda równoznaczna z komendą powyżej
            duza_litera.text = litera
            slowo.text = lang["translate"][litera]["word"]

            layout.ids.zamien_litere.bind(
               on_release= action(duza_litera, litera, litera_tlumaczenie)
            )

            litera_sound = lang["translate"][litera]["sound"]

            layout.ids.play_sound.bind(
                on_release= play_sound(litera_sound)

            )


        return carousel

if __name__ =="__main__":
    CarouselApp().run()