from game.text import Text
from game.constans import *

class TextHandler:
    def __init__(self, game) -> None:
        self.game = game
        self.texts_active = {}
        self.texts = {}
    
    def add_text(self, key, text=RAW_TEXT, speaker=''):
        if speaker != '':
            text_arr = [f'{speaker}: {fragment}' for fragment in text.split('\n')]
        else:
            text_arr = text.split('\n')
        self.texts_active[key] = False
        self.texts[key] = Text(self.game, text_arr)
    
    def update(self):
        [self.texts[key].update() for key in self.texts]
        [self.texts[key].start_timer() if value else self.texts[key].stop_timer() for key, value in self.texts_active.items()]