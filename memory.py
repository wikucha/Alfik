from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.core.window import Window
from kivy.graphics import Rectangle, Color
from kivy.core.audio import SoundLoader
from kivy.lang import builder
import pickle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
import random


def aktywuj(przycisk, stan=True):

    if przycisk.aktywny != stan:
        n= przycisk.background_normal
        przycisk.background_normal =przycisk.background_down
        przycisk.background_down = n
        przycisk.aktywny = stan

    return stan

def load_lang(file_name):
    lang = {}
    exec(open(file_name, encoding="utf-8").read(), lang)
    return lang

wybrane_przyciski = []
def action(button, color):
    def change(obj):
        button.background_color=color
        button.disabled = True
        global wybrane_przyciski
        print(len(wybrane_przyciski))
        if len(wybrane_przyciski) > 0:
            wybrane_przyciski.clear()
            # sprawdz czy poprawne przyciski
            for b in wybrane_przyciski:
                b.disabled = False
        else:
            wybrane_przyciski.append(button)
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
        box = GridLayout(cols=1,padding= 50, spacing= 10)



        lang=load_lang("lang/rus/config.py")
        ulubione= pickle.load(open("ulubione.p", "rb"))

        #tło
        with box.canvas:
            Color(1,1,1)
            Rectangle(source="img/tlo.png", pos=box.pos,size=Window.size)

        layout_top = builder.Builder.load_file("memory_layout.kv")
        box.add_widget(layout_top)

        layout = GridLayout(cols=4)
        box.add_widget(layout)
        #tłumaczenie słowa-połaczenie z layoutem
        wszystkie_litery = list(lang["translate"].keys())
        wybrane_litery = random.sample(wszystkie_litery, 8)
        tlumaczenie_wybrane_litery = []

        for litera in wybrane_litery:
            litera_tlumaczenie = lang["translate"][litera]["translation"]
            tlumaczenie_wybrane_litery.append(litera_tlumaczenie)


        lista = []
        lista.extend(wybrane_litery)
        lista.extend(tlumaczenie_wybrane_litery)

        random.shuffle(lista)
        for i in lista:

            Przycisk = Button(text=str(i), background_color=(0, 0, 0, 0.2))
            layout.add_widget(Przycisk)
            Przycisk.bind(on_release=action(Przycisk, (0.4, 0.6, 1, 1)))





        #random.shuffle(wybrane_litery)
        #for i in wybrane_litery:
        #   layout.add_widget(Button(text=str(i),background_color= (0,0,0,0.2)))



        return box

if __name__ =="__main__":
    CarouselApp().run()