from random import random

import imageio
import numpy as np
from kivy.core.window import Window
from kivy.graphics import Color, Ellipse, Line
from kivy.lang import builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget

from base_screen import BaseScreen


class MyPaintWidget(Widget):

    def on_touch_down(self, touch):
        color = (random(), 1, 1)
        with self.canvas:
            Color(*color, mode='hsv')
            przekatna = 10.
            Ellipse(pos=(touch.x - przekatna / 2, touch.y -
                         przekatna / 2), size=(przekatna, przekatna))
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=przekatna)

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


class PaintScreen(BaseScreen):

    def __init__(self, name):
        super(Screen, self).__init__(name=name)

    def check_accuracy2(self, obj):
        self.painter.size = Window.size
        self.textw.size = Window.size
        self.painter.export_to_png("test.png")
        self.textw.export_to_png("litera.png")

        obrazek_1 = imageio.imread("./test.png", pilmode="L")
        obrazek_1_lista = obrazek_1.flatten()

        obrazek_2 = imageio.imread("./litera.png", pilmode="L")
        obrazek_2_lista = obrazek_2.flatten()

        A = np.nonzero(obrazek_1_lista)[0]
        B = np.nonzero(obrazek_2_lista)[0]
        AB = len(np.intersect1d(A, B))

        C1 = tversky(A, B, AB, 0.9, 0.1)
        C3 = tversky(A, B, AB, 0.5, 0.5)
        if tree2(C1, C3):
            licznk = self.layout_top.ids.licznik_ok.text
            self.layout_top.ids.licznik_ok.text = str(int(licznk) + 1)
        else:
            licznk = self.layout_top.ids.licznik_false.text
            self.layout_top.ids.licznik_false.text = str(int(licznk) + 1)

    def on_enter(self):
        parent = GridLayout(cols=1)
        self.painter = MyPaintWidget(size=Window.size)

        self.lista = sorted(self.lang["translate"].keys())
        self.ktora_litera = 0
        self.textw = Label(
            text=self.lista[self.ktora_litera], font_size='500sp')

        self.layout_top = builder.Builder.load_file("proba_pisanie.kv")
        self.layout_top.ids.check.bind(on_release=self.check_accuracy2)
        self.layout_top.ids.clear_b.bind(on_release=self.clear_canva)
        self.layout_top.ids.next.bind(on_release=self.zmien_litera(+1))
        self.layout_top.ids.prev.bind(on_release=self.zmien_litera(-1))

        parent.add_widget(self.layout_top)

        parent2 = Widget()
        parent2.add_widget(self.textw)
        parent2.add_widget(self.painter)
        parent.add_widget(parent2)

        self.painter.size = Window.size
        self.textw.size = Window.size

        self.add_widget(parent)

    def clear_canva(self, obj):
        self.painter.canvas.clear()

    def zmien_litera(self, i):
        # TODO: add check for last and first position
        def change(obj):
            self.ktora_litera += i
            self.textw.text = self.lista[self.ktora_litera]
            self.painter.canvas.clear()
        return change


def tversky(A, B, AB, alpha, betha):
    return AB / (AB + alpha * (len(A) - AB) + betha * (len(B) - AB))


def tree2(C1, C3):
    if C1 <= 0.73252260685:
        if C1 <= 0.63205075264:
            return 0
        else:
            if C3 <= 0.475483775139:
                return 0
    return 1
