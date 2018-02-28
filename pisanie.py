from kivy.core.window import Window

from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse,Line,Rectangle

class MyPaintWidget(Widget):

    def __init__(self,**kwargs):
        Widget. __init__(self,**kwargs)
        self.color = (random(), random(), random())




    def on_touch_down(self,touch):
        with self.canvas:
            Color(*self.color) #*oznacza rozpakuj krotke
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))

            print((touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

class MyPaintApp(App):
    def build(self):
        self.layout=GridLayout(cols=2)#tworzymy 2 kolumny
        #czerwony=Button(text='czerwony')
        #czerwony.bind(on_release=self.self_color(1,1,0))


        parent = Widget()#widget ktory gromadzi widgety
        self.painter = MyPaintWidget()#gdy jest self z przodu to bedzie widoczna po wyjsciu z funkcji
        with self.painter.canvas:
            Rectangle(source="img/tlo.png", pos=(0, 0), size=Window.size)
            Color(1., 0, 0)

            # Add a rectangle
            nowyrozmiar=list(Window.size)
            nowyrozmiar[0]-=100
            nowyrozmiar[1]-=100
            Rectangle(pos=(50, 50), size=nowyrozmiar)
        parent.add_widget(self.painter)

       #clearbtn = Button(text='Clear')#tej zmiennej nie bedzie widac po wyjsciu  z funkcji
       #clearbtn.bind(on_release=self.clear_canvas)#bind to powiazanie ze stanem w tym przypadku on release czyli zwolnienie myszki guzika

       #setcolor = Button(text='kolor')
       #setcolor.bind(on_release=self.set_color)  # bind to powiazanie ze stanem w tym przypadku on release czyli zwolnienie myszki guzika

        self.layout.add_widget(parent)
       #self.layout.add_widget(clearbtn)
       #self.layout.add_widget(setcolor)
        return self.layout

    def clear_canvas(self, obj):
        self.painter.canvas.clear()
    def set_color(self,color):
        self.painter.color=(random(),1,1)


if __name__ == '__main__':
    MyPaintApp().run()