from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.core.window import Window
from kivy.graphics import Rectangle, Color
from kivy.core.audio import SoundLoader
from kivy.lang import builder
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.gridlayout import GridLayout


import random

licznik_wynik=0

def load_lang(file_name):
    lang = {}
    exec(open(file_name, encoding="utf-8").read(), lang)
    return lang

def action(app, button, color, buttons, czy_prawda):

    def change(obj):
        button.background_color=color

        if czy_prawda:

            app.score+=1


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
    score= NumericProperty(0)
    def build(self):
        box = GridLayout(cols=1,padding= 50, spacing= 10)

        carousel = Carousel(direction='right')
        lang=load_lang("lang/rus/config.py")
        layout_top = builder.Builder.load_file("fon_quiz_layout_top.kv")
        box.add_widget(layout_top)
        box.add_widget(carousel)




        #ulubione = []
        # lang = {"translate":  {'а': {'translation': 'a', 'word': 'мама'}, 'б': {'translation': 'b', 'word': 'бумага'}}}


        with carousel.canvas:
            Color(1,1,1)
            Rectangle(source="img/tlo.png", pos=carousel.pos,size=Window.size)

        wszystkie_litery_alf = list(lang["translate"].keys())

        random.shuffle(wszystkie_litery_alf)

        for litera in wszystkie_litery_alf:
            litera_sound = lang["translate"][litera]["sound"]
            if litera_sound is None: continue
            litera_tlumaczenie = lang["translate"][litera]["translation"]
            #layout = builder.Builder.load_file("fon_quiz_layout.kv")
            #carousel.add_widget(layout)

            odp_false=(1,0.2,0,0.8)
            odp_true = (0, 1, 0, 0.8)

            #odp_A=layout.ids.odp_A
            #odp_B = layout.ids.odp_B
            #odp_C = layout.ids.odp_C
            #odp_D = layout.ids.odp_D

            #buttons=[odp_A,odp_B,odp_C,odp_D]

            wszystkie_litery = list(lang["translate"].keys())
            wszystkie_litery.remove(litera)
            wybrane_litery=random.sample(wszystkie_litery, 3)
            wybrane_litery.append(litera)

            random.shuffle(wybrane_litery)

            for Przycisk, wybrana_litera in zip(buttons, wybrane_litery):
                Przycisk.text = wybrana_litera
                if litera == wybrana_litera:
                    Przycisk.bind(on_release=action(self,Przycisk, odp_true, buttons,  True))
                else:
                    Przycisk.bind(on_release=action(self,Przycisk, odp_false, buttons,  False))




            layout.ids.play_sound.bind(
                on_release= play_sound(litera_sound)

            )


        return carousel

if __name__ =="__main__":
    CarouselApp().run()