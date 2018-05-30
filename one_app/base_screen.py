import pickle
from kivy.uix.screenmanager import Screen
from kivy.app import App
class BaseScreen(Screen):
    def on_pre_enter(self):
        """ Akcje wykonywane przed wejściem -- odczyt alfabetu i ulubionych z aplikacji.
        """
        # Wybrane w menu glownym jezyk i ulubione
        app = App.get_running_app()
        self.lang = app.current_lang_dict
        self.ulubione = app.current_lang_ulubione
        self.ulubione_file = app.current_lang_ulubione_file
        self.clear_widgets()
        if not self.lang or len(self.lang) == 0:
            app.root.current = 'menu'


    def on_pre_leave(self):
        """ Akcje wykonywane przed wyjściem -- zapisanie ulubionych.
        """
        try:
            pickle.dump(self.ulubione, open(self.ulubione_file, "wb"))
        except Exception as e:
            print(e)
        app = App.get_running_app()
        app.current_lang_ulubione = self.ulubione
