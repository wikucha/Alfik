from kivy.core.window import Window
from kivy.uix.label import Label
from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse,Line,Rectangle
from kivy.lang import builder


def tree2(C1, C3,):
  if C1 <= 0.73252260685:
    if C1 <= 0.63205075264:
      return 0
    else:
      if C3 <= 0.475483775139:
        return 0
      else:
        return 1
  else:
    return 1

def tversky(A,B, AB, alpha, betha):
    return (AB / (AB + alpha * (len(A) - AB) + betha * (len(B) - AB)))



class MyPaintWidget(Widget):

    def __init__(self,**kwargs):
        Widget. __init__(self,**kwargs)
        self.color = (random(), random(), random())

    def on_touch_down(self,touch):
        with self.canvas:
            Color(*self.color) #*oznacza rozpakuj krotke
            d = 30.
            if touch.y>120 and touch.x>215 and touch.y<470 and touch.x<565:
                touch.ud['line'] = Line(points=(touch.x, touch.y),width=9)
                print((touch.x, touch.y))
            else:
                print("a")

    def on_touch_move(self, touch):
        if touch.y > 120 and touch.x > 215 and touch.y < 470 and touch.x < 565:
            touch.ud['line'].points += [touch.x, touch.y]

class MyPaintApp(App):
    def build(self):
        #self.layout=GridLayout(cols=2)#tworzymy 2 kolumny

        #czerwony=Button(text='czerwony')
        #czerwony.bind(on_release=self.self_color(1,1,0))

        parent = Widget()#widget ktory gromadzi widgety
        self.painter = MyPaintWidget()#gdy jest self z przodu to bedzie widoczna po wyjsciu z funkcji
        with self.painter.canvas:
         #   Rectangle(source="img/tlo.png", pos=(0, 0), size=Window.size)
            Color(0.85, 0.7, 0.75,0.5)

            # Add a rectangle
            nowyrozmiar=list(Window.size)
            nowyrozmiar[0]=350
            nowyrozmiar[1]=350
            Rectangle(pos=(215, 120), size=nowyrozmiar)

        text2 = Label(text="a", font_size='350sp',pos=(338,270))

        parent.add_widget(text2)

        parent.add_widget(self.painter)
        layout = builder.Builder.load_file("learn_layout_pisanie.kv")

        def clear_canvas(obj):
            self.painter.canvas.clear()

        def get_check(litera, correct):
            def check(obj):
                self.check_accuracy(obj, litera, correct)

            return check

        checkbtn = layout.ids.check
        clearbtn = layout.ids.clear
        nextbtn = layout.ids.next

        print(clearbtn)

        clearbtn.bind(on_release=clear_canvas)
        nextbtn.bind(on_release=lambda x: self.next_l(x))
        checkbtn.bind(on_release=self.get_check)

        layout.add_widget(parent)


        return layout
    
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

        C1 = tversky(A, B, AB, 0.9, 0.1)
        C3 = tversky(A, B, AB, 0.5, 0.5)

        return C1,C3


       #clearbtn = Button(text='Clear')#tej zmiennej nie bedzie widac po wyjsciu  z funkcji
       #clearbtn.bind(on_release=self.clear_canvas)#bind to powiazanie ze stanem w tym przypadku on release czyli zwolnienie myszki guzika

       #setcolor = Button(text='kolor')
       #setcolor.bind(on_release=self.set_color)  # bind to powiazanie ze stanem w tym przypadku on release czyli zwolnienie myszki guzika

        #self.layout.add_widget(parent)
       #self.layout.add_widget(clearbtn)
       #self.layout.add_widget(setcolor)
        #return self.layout






if __name__ == '__main__':
    MyPaintApp().run()