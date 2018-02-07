from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.graphics import *


class CarouselApp(App):
    def change(self,obj):
        self.text="X"

        print("kkk")
    def build(self):



        carousel = Carousel(direction='right')



        lang = {"translate":  {'а': {'translation': 'a', 'word': 'мама'}, 'б': {'translation': 'b', 'word': 'бумага'}}}



        #exec(open("lang/rus/config.py").read(),lang)
        #print(lang["translate"])




        with carousel.canvas:
            Window.size
            Color(1,1,1)
            Rectangle(source="img/tlo.png", pos=carousel.pos,size=Window.size)

        #return carousel
        for i in lang["translate"]:
            self.text = i

            layouttop = GridLayout(cols=2)

            texta = Label(text=self.text, font_size='100sp')
            textb = Label(text=self.text, font_size='100sp')

            layouttop.add_widget(texta)
            layouttop.add_widget(textb)


            layout = GridLayout(rows=4)
            text1 = Label(text=self.text, font_size='100sp')

            layout.add_widget(layouttop)




            text2 = Label(text=self.text, font_size='300sp')

            layout.add_widget(text2)



            text3 = Button(text=self.text, font_size='50sp')

            def action(label,org,translate):
                def change(obj):
                    if label.text == org:
                        label.text = translate
                    else:
                        label.text = org
                return change

            text3.bind(on_release=action(text2,i,lang["translate"][i]["translation"]))

            layout.add_widget(text3)




            text4 = Label(text=lang["translate"][i]["word"], font_size='100sp')

            layout.add_widget(text4)



           # text5 = Label(text=text, font_size='500sp')

#            layout.add_widget(text5)

            #layout.add_widget(img)

            carousel.add_widget(layout)


            text = chr(ord(self.text)+1)


           # with  widget.canvas:
               # widget.bg_rect = Rectangle(source="slonce.jpg", pos=self.pos, size=self.size)
            #widget.bind(pos=redraw, size=redraw)


        return carousel




if __name__ =="__main__":
    CarouselApp().run()