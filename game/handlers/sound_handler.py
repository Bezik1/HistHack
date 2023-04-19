import pygame as pg

class SoundHandler:
    def __init__(self, game):
        pg.mixer.init()
        pg.mixer.music.set_volume(0.4)
        
        self.game = game
        self.path = 'resources/sound/'
        self.pickup_item = pg.mixer.Sound(self.path + 'pickup_item.wav')
        self.achtung_sound = pg.mixer.Sound(self.path + 'achtung.wav')