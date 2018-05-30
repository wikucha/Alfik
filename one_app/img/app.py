from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window

from learn import LearnScreen
from memory import MemoryScreen
from tools import load_lang, load_ulubione

Builder.load_file("app.kv")

# Ekran menu (wygląd wczytany z app.kv)
class MenuScreen(Screen):
    pass

# Ekran z ustawieniami
class SettingsScreen(Screen):
    pass

# Główna aplikacja zarządzająca grami
class MainApp(App):
    def current_lang():
        doc = "Obsluga wczytywania jezyka i ulubionych"
        def fget(self):
            return self._current_lang
        def fset(self, value):
            fname_dict = "lang/%s/config.py" % (value)
            fname_ulubione = "ulubione/%s_ulubione.pickle" % (value)

            self._current_lang = fname_dict
            self.current_lang_ulubione_file = fname_ulubione
            self.current_lang_dict = load_lang(fname_dict)
            self.current_lang_ulubione = load_ulubione(fname_ulubione)
        def fdel(self):
            del self._current_lang
        return locals()

    current_lang = property(**current_lang())

    def build(self):

        self._current_lang = None
        self.current_lang_ulubione_file = None
        self.current_lang_dict = None
        self.current_lang_ulubione = None

        sm = ScreenManager()

        # Ustawienie tła
        with sm.canvas:
            Color(1, 1, 1)
            rect = Rectangle(source="img/tlo.png", size=Window.size)

        # Skalowanie obrazka przy zmianie wymiarów okna (orientacji telefonu)
        def resize_action(size, pos):
            sm.size = Window.size
            rect.size = Window.size
        sm.bind(pos=resize_action, size=resize_action)

        # Aplikacje którymi zarządzamy
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(LearnScreen(name='game'))
        sm.add_widget(MemoryScreen(name='memory'))
        sm.add_widget(SettingsScreen(name='settings'))

        return sm

if __name__ == '__main__':
    MainApp().run()
