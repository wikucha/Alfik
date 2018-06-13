import random

from kivy.lang import builder
from kivy.properties import NumericProperty
from kivy.uix.carousel import Carousel

from base_screen import BaseScreen
from tools import play_sound


def action(app, button, color, buttons, wynik, czy_prawda):
    def change(obj):
        button.background_color=color

        if czy_prawda:
            wynik.score = 1
            pass

        for B in buttons:
            B.disabled = True
    return change


class FonquizScreen(BaseScreen):
    def on_enter(self):
        carousel = Carousel(direction='right')

        wszystkie_litery_alf = list(self.lang["translate"].keys())

        random.shuffle(wszystkie_litery_alf)

        for litera in wszystkie_litery_alf:
            litera_sound = self.lang["translate"][litera]["sound"]
            if litera_sound is None: continue
            litera_tlumaczenie = self.lang["translate"][litera]["translation"]
            layout = builder.Builder.load_file("fon_quiz_layout.kv")
            carousel.add_widget(layout)

            odp_false=(1,0.2,0,0.8)
            odp_true = (0, 1, 0, 0.8)

            odp_A=layout.ids.odp_A
            odp_B = layout.ids.odp_B
            odp_C = layout.ids.odp_C
            odp_D = layout.ids.odp_D

            buttons=[odp_A,odp_B,odp_C,odp_D]

            wszystkie_litery = list(self.lang["translate"].keys())
            wszystkie_litery.remove(litera)
            wybrane_litery=random.sample(wszystkie_litery, 3)
            wybrane_litery.append(litera)

            random.shuffle(wybrane_litery)
            layout.score = str(NumericProperty(0))
            layout.ids.wynik=layout.score
            for Przycisk, wybrana_litera in zip(buttons, wybrane_litery):
                Przycisk.text = wybrana_litera
                if litera == wybrana_litera:
                    Przycisk.bind(on_release=action(self, Przycisk, odp_true, buttons, layout, True))
                else:
                    Przycisk.bind(on_release=action(self, Przycisk, odp_false, buttons, layout, False))

            layout.ids.play_sound.bind(on_release= play_sound(litera_sound))

        self.add_widget(carousel)
