from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.core.window import Window
from kivy.graphics import Rectangle, Color
from kivy.core.audio import SoundLoader
from kivy.lang import builder
import pickle


def aktywuj(przycisk, stan=True):

    if przycisk.aktywny != stan:
        n= przycisk.background_normal
        przycisk.background_normal =przycisk.background_down
        przycisk.background_down = n
        przycisk.aktywny = stan

    return stan

#button ulubione
def dodaj_ulub(ulubione, litera, przycisk, przycisk_tlo_normal, przycisk_tlo_down):

    def add(obj):

        if przycisk.aktywny:
            ulubione.remove(litera)
            aktywuj(przycisk, False)
        else:
            ulubione.append(litera)
            aktywuj(przycisk, True)
        n = przycisk.background_normal

        pickle.dump(ulubione, open("ulubione.p", "wb"))
    return add

def load_lang(file_name):
    lang = {}
    exec(open(file_name, encoding="utf-8").read(), lang)
    return lang

#zmiana litery
def action(label, org, translate):
    def change(obj):
        if label.text == org:
            label.text = translate
        else:
            label.text = org
    return change

#dźwięki
def play_sound(plik):
    def play_action(obj):
        if plik is None: return
        sound = SoundLoader.load(plik)
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()
    return play_action

#karuzela
class CarouselApp(App):
    def build(self):
        carousel = Carousel(direction='right')
        lang=load_lang("lang/rus/config.py")
        ulubione= pickle.load(open("ulubione.p", "rb"))
        #ulubione = []
        # lang = {"translate":  {'а': {'translation': 'a', 'word': 'мама'}, 'б': {'translation': 'b', 'word': 'бумага'}}}

        #tło
        with carousel.canvas:
            Color(1,1,1)
            Rectangle(source="img/tlo.png", pos=carousel.pos,size=Window.size)
        #tłumaczenie słowa-połaczenie z layoutem
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

            #utrzymanie przycisku
            pulub=layout.ids.fav
            pulub.aktywny = False
            if litera in ulubione:
                aktywuj(pulub, True)

            pulub.bind(
                on_release=dodaj_ulub(ulubione, litera, pulub, pulub.background_normal, pulub.background_down)
            )

            litera_sound = lang["translate"][litera]["sound"]

            layout.ids.play_sound.bind(
                on_release= play_sound(litera_sound)

            )


        return carousel

if __name__ =="__main__":
    CarouselApp().run()