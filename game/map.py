import pygame as pg
from game.constans import *

_ = False

tenement1_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, 1, _, _, _, _, _, _, 1, 1, 1, 1, 1, 1, 1, 1, 1, _, _, _, _, _, _, _, 1, 1],
    [1, _, _, _, _, _, _, 1, 1, _, _, _, _, _, _, _, _, _, _, 1, 1, 1, 1, _, _, _, _, _, _, _, 1, 1],
    [1, _, _, _, _, _, 1, 1, 1, _, _, _, _, _, 1, _, _, _, _, 1, 1, 1, 1, _, _, 1, 1, 1, _, _, 1, 1],
    [1, 1, 1, 1, 1, _, 1, 1, 1, _, _, _, _, _, 1, _, _, 1, 1, 1, 1, 1, 1, _, _, 1, 1, 1, _, _, 1, 1],
    [1, 1, 1, 1, 1, _, 1, 1, 1, _, _, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, _, _, _, _, 1, 1, _, _, 1, 1],
    [1, 1, 1, 1, 1, _, 1, 1, 1, _, _, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, _, _, _, _, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, 1, 1 ,1, 1, 1, _, _, _, _, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, _, 1, _, _, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, _, _, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, _, 1, _, _, _, _, _, _, _, 1, 1, 1, 1, 1, 1, 1, _, _, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, _, 1, _, _, _, _, _, _, _, 1, 1, 1, 1, 1, _, 1, 1, 1, 1, 1, 1, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, _, 1, 1, 1, _, 1, 1, 1, _, 1, 1, _, _, _, _, 1, 1, 1, 1, 1, 1, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, _, 1, _, _, _, 1, 1, 1, _, 1, 1, _, _, 1, 1, 1, 1, _, _, 1, 1, 1, _, _, _, 1],
    [1, _, _, _, _, _, _, 1, 1, 1, 1, 1, 1, 1, _, 1, 1, _, _, 1, 1, 1, 1, _, _, 1, 1, 1, _, _, _, 1],
    [1, _, _, _, _, _, _, 1, _, 1, 1, 1, 1, 1, _, _, 1, _, _, 1, 1, 1, 1, _, _, _, _, _, _, 1, 1, 1],
    [1, _, _, _, _, _, _, 1, _, 1, 1, _, _, _, _, _, _, _, _, _, _, 1, 1, _, _, _, _, _, _, 1, 1, 1],
    [1, _, _, _, _, _, _, 1, _, 1, 1, _, _, _, _, _, 1, _, _, 1, _, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

channels_map = [
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, _, _, 2, 2, 2, 2, 2, _, _, _, _, _, _, _, _, 2, _, _, 2, _, 2, _, _, _, _, _, 2, _, 2, _, 2],
    [2, _, _, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, _, 2, _, _, 2, _, 2, _, _, _, _, _, 2, _, 2, _, 2],
    [2, _, _, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, _, 2, _, _, 2, _, 2, _, 2, 2, 2, 2, 2, _, 2, _, 2],
    [2, _, _, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, _, 2, _, _, 2, _, 2, _, 2, _, _, _, _, _, 2, _, 2],
    [2, _, _, _, _, _, _, _, _, _, _, 2, 2, 2, 2, _, 2, _, _, 2, _, 2, _, 2, _, 2, 2, 2, 2, 2, _, 2],
    [2, _, _, _, _, _, _, _, _, _, _, 2, 2, 2, 2, _, 2, _, _, 2, _, 2, _, 2, _, 2, _, _, _, _, _, 2],
    [2, 2, 2, 2, _, 2, 2, 2, 2, _, _, 2, 2, 2, 2, _, 2, 2, 2, 2, _, 2, 2, 2, _, 2, 2, 2, 2, 2, 2, 2],
    [2, _, _, _, _, _, _, _, 2, _, _, 2, 2, 2, 2, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 2],
    [2, _, 2, 2, 2, 2, 2, _, 2, _, _, 2, 2, 2, 2, 2, 2, 2, 2, _, _, _, _, _, _, _, _, _, _, _, _, 2],
    [2, _, 2, _, 2, 2, 2, _, 2, _, _, 2, 2, 2, 2, 2, 2, 2, 2, _, _, _, _, _, _, _, _, _, _, _, _, 2],
    [2, _, 2, _, 2, 2, 2, _, 2, _, _, 2, 2, 2, 2, 2, 2, 2, 2, _, _, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, _, 2, _, 2, 2, 2, _, _, _, _, 2, 2, 2, 2, 2, 2, 2, 2, _, _, 2, _, _, _, _, _, _, _, _, _, 2],
    [2, _, 2, _, 2, 2, 2, 2, 2, 2, _, _, _, _, _, _, _, _, _, _, _, _, 2, _, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, _, 2, _, 2, 2, 2, 2, 2, _, _, _, _, _, _, _, _, _, _, _, _, 2, _, 2, _, _, _, _, _, 2, _, 2],
    [2, _, 2, _, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, _, 2, 2, 2, 2, 2, 2, 2, _, 2, _, 2, _, _, _, 2, _, 2],
    [2, _, 2, _, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, _, 2, 2, 2, 2, 2, 2, 2, 2, 2, _, 2, 2, 2, 2, 2, _, 2],
    [2, _, 2, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
]

#(31, 10)

tenement2_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, 1, 1, _, _, _, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, _, 1, _, 1, 1, _, _, _, _, _, _, _, 1, 1],
    [1, _, 1, 1, _, _, _, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, _, 1, _, 1, 1, _, _, _, _, _, _, _, 1, 1],
    [1, _, 1, 1, 1, _, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, _, 1, _, 1, 1, 1, 1, 1, 1, 1, _, _, 1, 1],
    [1, _, 1, 1, 1, _, 1, 1, 1, 1, 1, _, _, _, _, _, 1, 1, 1, 1, _, 1, 1, 1, 1, 1, 1, 1, _, _, 1, 1],
    [1, _, 1, 1, 1, _, 1, 1, 1, 1, 1, _, _, _, _, _, 1, 1, 1, 1, _, 1, _, _, _, _, _, _, _, _, 1, 1],
    [1, _, 1, 1, 1, _, 1, 1, 1, 1, 1, _, 1, 1, 1, 1, 1, 1, 1, 1, _, 1, _, _, _, _, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, 1, 1 ,1, _, 1, _, _, _, _, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, _, 1, _, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, _, 1, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, 1, 1, 1, 1, 1, _, 1, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, 1, 1, 1, 1, 1, _, 1, 1, 1, 1, 1, 1, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, _, 1, 1, 1, 1, 1, 1, _, _, 1, _, 1, 1, 1, 1, 1, 1, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, _, _, _, _, _, 1, 1, 1, 1, 1, 1, _, _, 1, _, 1, 1, _, _, 1, 1, 1, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, _, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, _, _, 1, _, 1, 1, _, _, 1, 1, 1, _, _, _, 1],
    [1, _, _, _, _, _, _, 1, _, 1, 1, 1, 1, 1, 1, _, 1, _, _, 1, _, 1, 1, _, _, _, _, _, _, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, _, 1, 1, _, _, _, _, _, 1, _, _, 1, _, 1, 1, _, _, _, _, _, _, 1, 1, 1],
    [1, _, _, _, _, _, 1, 1, _, 1, 1, _, _, _, _, _, 1, _, _, 1, _, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

class Map:
    def __init__(self, game, floor_index) -> None:
        self.game = game
        self.maps = [tenement1_map, channels_map, tenement2_map]
        self.current_index = floor_index
        self.mini_map = self.maps[self.current_index]
        self.world_map = {}
        self.get_map()
    
    def draw_current_map_name(self):
        match self.current_index:
            case 0:
                text = 'Kamienica 1'
            case 1:
                text = 'Kanały'
            case 2:
                text = 'Kamienica 2'
            case _:
                text = 'Kamienica 1'
    
        font = pg.font.Font(None, 55)
        text_surface = font.render(text, True, (255, 255, 255))
        self.game.screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2,  text_surface.get_height() // 2 + 50))
    
    def update(self):
        self.draw_current_map_name()
        self.mini_map = self.maps[self.current_index]
        self.get_map()
    
    def go_back(self):
        self.current_index -= 1
        self.world_map = {}
        self.game.player.set_pos((8.5, 1.5))
        self.game.interaction = False
        
    def go_next(self):
        self.current_index += 1
        self.world_map = {}
        self.game.player.set_pos(PLAYER_POS)
        self.game.interaction = False
    
    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    def draw(self):
        [pg.draw.rect(self.game.screen, 'darkgray', (pos[0]*200, pos[1]*100, 100, 100), 1)
         for pos in self.world_map]