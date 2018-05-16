from kivy.core.window import Window
from kivy.uix.label import Label
from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse,Line,Rectangle
import pickle
import imageio
import numpy as np

wektor=[1,2]

def dodaj_ulub(ulub, litera):

    def add(obj):
        global wektor
        with open("text.txt", "a") as myfile:
            for i in wektor:
                myfile.write(str(i)+",")
            myfile.write("\n")

    return add

class MyPaintWidget(Widget):

    def on_touch_down(self, touch):
        color = (random(), 1, 1)
        with self.canvas:
            Color(*color, mode='hsv')
            d = 10.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=d)

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

class MyPaintApp(App):

    def build(self):
        parent = Widget()
        self.painter = MyPaintWidget(size=Window.size)
        checkbtn = Button(text='Check')
        clearbtn = Button(text='Clear')
        nextbtn = Button(text='Next')

        def get_check(litera, correct):
            def check(obj):
                self.check_accuracy(obj, litera, correct)
            return check

        def clear(x):
            self.clear_canva(x)

        #checkbtn.bind(on_release=check)
        clearbtn.bind(on_release=clear)
        nextbtn.bind(on_release=lambda x: self.next_l(x))

        self.textw = Label(text='A', font_size='500sp')

        self.painter.size = Window.size
        self.textw.size = Window.size

        parent.add_widget(self.textw)
        parent.add_widget(self.painter)

        grid= GridLayout(rows=2)

        layout = GridLayout(cols=3)

        layout.add_widget(checkbtn)
        layout.add_widget(clearbtn)
        layout.add_widget(nextbtn)
        grid.add_widget(layout)


        poprawny = Button(text="T")
        poprawny.bind(on_release= get_check(self.textw.text, 1))

        niepoprawny = Button(text="N")
        niepoprawny.bind(on_release= get_check(self.textw.text, 0))

        layout2 = GridLayout(cols=2)
        grid.add_widget(layout2)

        layout2.add_widget(poprawny)
        layout2.add_widget(niepoprawny)
        parent.add_widget(grid)
        return parent

    def check_accuracy(self, obj, litera, correct):
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
        t1 = tversky(A, B, AB, 0.9, 0.1)
        t2 = tversky(A, B, AB, 0.1, 0.9)
        t3 = tversky(A, B, AB, 0.5, 0.5)

        print(litera, correct, t1, t2, t3, AB / ( len(A) + len(B) - AB), len(A)/len(B))

        with open("text.txt", "a") as myfile:
            text = litera + "," + str(correct) +  str(t1) + str(t2) + str(t3) + str(AB / ( len(A) + len(B) - AB)) + str(len(A)/len(B)) + "\n"
            myfile.write(text)

        # print(tversky2(obrazek_1,obrazek_2, 0.1, 0.9))

        print("ok")

    def clear_canva(self, obj):
        self.painter.canvas.clear()

    def next_l(self, obj):
        self.textw.text = chr(ord(self.textw.text) + 1)

    def clear_canvas(self, obj):
        self.painter.canvas.clear()
    def set_color(self,color):
        self.painter.color=(random(),1,1)

def tversky(A,B, AB, alpha, betha):
    return (AB / (AB + alpha * (len(A) - AB) + betha * (len(B) - AB)))

def tversky2(A,B, alpha, betha):
    t1 = 0
    t2 = 0
    nonzero = 0
    for a,b in zip(A,B):
        x=(tversky(a,b, 0.9, 0.1))
        y=(tversky(a,b, 0.1, 0.9))
        if x > 0 or x >0:
            nonzero +=1
            t1+=x
            t2+=y

    return nonzero, t1/nonzero, t2/nonzero



if __name__ == '__main__':
    MyPaintApp().run()