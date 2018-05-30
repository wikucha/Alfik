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

from base_screen import BaseScreen
from kivy.uix.screenmanager import Screen


#karuzela
class MemoryScreen(BaseScreen):
    def __init__(self, name):
        super(Screen, self).__init__(name=name)

    def on_enter(self):
        box = GridLayout(cols=1,padding= 50, spacing= 10)


        layout_top = builder.Builder.load_file("memory_layout.kv")
        box.add_widget(layout_top)

        layout = GridLayout(cols=4)
        box.add_widget(layout)
        #tłumaczenie słowa-połaczenie z layoutem
        wszystkie_litery = list(self.lang["translate"].keys())
        wybrane_litery = random.sample(wszystkie_litery, 8)
        tlumaczenie_wybrane_litery = []

        for litera in wybrane_litery:
            litera_tlumaczenie = self.lang["translate"][litera]["translation"]
            tlumaczenie_wybrane_litery.append(litera_tlumaczenie)

        self.wybrane_przyciski = []
        def action(button, color,wynik):
            def change(obj):
                stary_kolor = button.background_color
                button.background_color=color
                button.disabled = True
                self.wybrane_przyciski.append(button)
                print(len(self.wybrane_przyciski))

                if len(self.wybrane_przyciski) > 1:

                    if self.wybrane_przyciski[0].tlumaczenie == self.wybrane_przyciski[1].tlumaczenie:


                        # sprawdz czy poprawne przyciski
                        for b in self.wybrane_przyciski:
                            b.disabled = True
                            b.background_color=(0.5, 0.8, 0.1,1)
                    else:
                        for b in self.wybrane_przyciski:
                            b.background_color = stary_kolor
                            b.disabled = False
                        x = wynik.ids.licznik.text
                        wynik.ids.licznik.text = str(int(x) + 1)

                        self.wybrane_przyciski.clear()
                    self.wybrane_przyciski.clear()
            return change

        lista = []
        lista.extend(wybrane_litery)
        random.shuffle(self.wybrane_przyciski)

        lista.extend(tlumaczenie_wybrane_litery)
        random.shuffle(tlumaczenie_wybrane_litery)

        random.shuffle(lista)
        for litera in wybrane_litery:

            Przycisk = Button(text=str(litera), background_color=(0, 0, 0, 0.3))
            Przycisk.tlumaczenie = self.lang["translate"][litera]["translation"]
            layout.add_widget(Przycisk)
            Przycisk.bind(on_release=action(Przycisk, (0.5, 0.8, 0.1, 0.7), layout_top))

        for litera in tlumaczenie_wybrane_litery:

            Przycisk = Button(text=str(litera), background_color=(0, 0, 0, 0.2))
            Przycisk.tlumaczenie = litera
            layout.add_widget(Przycisk)
            Przycisk.bind(on_release=action(Przycisk, (0.5, 0.8, 0.1, 0.7), layout_top))

        self.add_widget(box)
