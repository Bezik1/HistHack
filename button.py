import pygame as pg
from config import *
from game.index import Game
from collection import Collection

class Button():
    def __init__(self, menu, index,y):
        self.menu = menu
        self.text = menu_options[index]
        self.font = pg.font.Font('resources/font/aleo.otf',80)
        self.text_surf = self.font.render(self.text, False, (0, 0, 0))
        self.text_rect = self.text_surf.get_rect(center = (1350,y))
        self.items = []

    def pressing(self,index,screen):
        match index:
            case 0:
                if not self.menu.game_over:
                    game = Game(self.menu.player_pos, self.menu.pickups, self.menu.progress_value, self.menu.quests)
                    self.menu.player_pos, self.menu.pickups, self.menu.progress_value, self.menu.quests, self.menu.game_over = game.run()
            case 1:
                collection = Collection(self.menu)
                collection.run(self.items)
            case _:
                print('Index out of range')

