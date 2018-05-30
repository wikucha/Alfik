from kivy.lang import builder
from kivy.uix.carousel import Carousel
from kivy.uix.screenmanager import Screen

from base_screen import BaseScreen
from tools import przycisk_ulubione, play_sound

# zmiana litery
def action(label, org, translate):
    def change(obj):
        if label.text == org:
            label.text = translate
        else:
            label.text = org
    return change

# karuzela
class LearnScreen(BaseScreen):
    def __init__(self, name):
        super(Screen, self).__init__(name=name)

    def on_enter(self):

        carousel = Carousel(direction='right')

        # tłumaczenie słowa-połaczenie z layoutem
        for litera in self.lang["translate"]:
            litera_tlumaczenie = self.lang["translate"][litera]["translation"]
            layout = builder.Builder.load_file("learn_layout.kv")
            carousel.add_widget(layout)

            slowo = layout.ids.slowo
            slowo.text = self.lang["translate"][litera]["word"]

            duza_litera = layout.ids.duza_litera
            duza_litera.text = litera

            # Podpięte działania
            layout.ids.zamien_litere.bind(
                on_release=action(duza_litera, litera, litera_tlumaczenie)
            )

            # utrzymanie przycisku
            polub = layout.ids.fav
            przycisk_ulubione(polub, litera, self.ulubione)

            # Dźwięk
            litera_sound = self.lang["translate"][litera]["sound"]
            layout.ids.play_sound.bind(on_release=play_sound(litera_sound))

        self.add_widget(carousel)
