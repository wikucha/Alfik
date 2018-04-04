from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.core.window import Window
from kivy.graphics import Rectangle, Color
from kivy.core.audio import SoundLoader
from kivy.lang import builder

import random



def load_lang(file_name):
    lang = {}
    exec(open(file_name, encoding="utf-8").read(), lang)
    return lang

def action(button, color, buttons):
    def change(obj):
        button.background_color=color

        for B in buttons:
            B.disabled = True
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

        #ulubione = []
        # lang = {"translate":  {'а': {'translation': 'a', 'word': 'мама'}, 'б': {'translation': 'b', 'word': 'бумага'}}}


        with carousel.canvas:
            Color(1,1,1)
            Rectangle(source="img/tlo.png", pos=carousel.pos,size=Window.size)

        for litera in lang["translate"]:
            litera_tlumaczenie = lang["translate"][litera]["translation"]
            layout = builder.Builder.load_file("fon_quiz_layout.kv")
            carousel.add_widget(layout)

            odp_false=(1,0.2,0,0.8)
            odp_true = (0, 1, 0, 0.8)

            odp_A=layout.ids.odp_A
            odp_B = layout.ids.odp_B
            odp_C = layout.ids.odp_C
            odp_D = layout.ids.odp_D

            buttons=[odp_A,odp_B,odp_C,odp_D]

            wszystkie_litery = list(lang["translate"].keys())
            wszystkie_litery.remove(litera)
            wybrane_litery=random.sample(wszystkie_litery, 3)
            wybrane_litery.append(litera)

            random.shuffle(wybrane_litery)

            for Przycisk, wybrana_litera in zip(buttons, wybrane_litery):
                Przycisk.text = wybrana_litera
                if litera == wybrana_litera:
                    Przycisk.bind(on_release=action(Przycisk, odp_true, buttons))
                else:
                    Przycisk.bind(on_release=action(Przycisk, odp_false, buttons))


            litera_sound = lang["translate"][litera]["sound"]

            layout.ids.play_sound.bind(
                on_release= play_sound(litera_sound)

            )


        return carousel

if __name__ =="__main__":
    CarouselApp().run()