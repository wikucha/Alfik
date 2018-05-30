import pickle

from kivy.core.audio import SoundLoader



def load_lang(file_name):
    lang = {}
    try:
        exec(open(file_name, encoding="utf-8").read(), lang)
    except Exception as excp:
        raise excp
    return lang

def load_ulubione(file_name):

    ulubione = []
    try:
        ulubione = pickle.load(open(file_name, "rb"))
    except Exception as excp:
        print(excp)
    return ulubione

def aktywuj_ulubione(przycisk, stan=True):

    if przycisk.aktywny != stan:
        old_background = przycisk.background_normal
        przycisk.background_normal = przycisk.background_down
        przycisk.background_down = old_background
        przycisk.aktywny = stan

    return stan

# button ulubione
def dodaj_ulub(ulubione, litera, przycisk):

    def add(obj):

        if przycisk.aktywny:
            ulubione.remove(litera)
            aktywuj_ulubione(przycisk, False)
        else:
            ulubione.append(litera)
            aktywuj_ulubione(przycisk, True)

    return add

def przycisk_ulubione(polub, litera, ulubione):
    polub.aktywny = False
    if litera in ulubione:
        aktywuj_ulubione(polub, True)
    polub.bind(on_release=dodaj_ulub(ulubione, litera, polub))


# dźwięki
def play_sound(plik):
    def play_action(obj):
        if plik is None:
            return
        sound = SoundLoader.load(plik)
        if sound:
            sound.play()
    return play_action
