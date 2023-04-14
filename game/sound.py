import pygame as pg

class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'resources/sound/'
        #pickup_item.mp3
        self.pickup_item = pg.mixer.Sound(self.path + 'pickup_item.wav')
        self.achtung_sound = pg.mixer.Sound(self.path + 'achtung.wav')
        pg.mixer.music.set_volume(0.4)