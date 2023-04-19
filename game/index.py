import pygame as pg
from game.constans import *
from game.map import Map
from game.player import Player
from game.texture_loader import TextureLoader
from game.handlers.object_handler import ObjectHandler
from game.raycasting import RayCasting
from game.handlers.text_handler import TextHandler
from game.handlers.sound_handler import SoundHandler
from game.progress import Progress
from game.handlers.quest_handler import QuestHandler

class Game:
    def __init__(self, config) -> None:
        pg.init()
        pg.mouse.set_visible(False)

        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        
        self.pos = config['pos']
        self.progress_value = config['progress']
        self.pickups = config['pickups']
        self.floor_index = config['floor_index']
        self.quests = config['quests']
        
        self.delta_time = 1
        self.interaction = False
        self.first_final_event = False
        self.expand_quests = False
        self.win_condition = False
        
        self.new_game()
    
    def new_game(self):
        self.map = Map(self, self.floor_index)
        self.player = Player(self, self.pos, self.pickups)
        self.quest_handler = QuestHandler(self, self.quests)
        self.text_handler = TextHandler(self)
        self.texture_loader = TextureLoader(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectHandler(self, self.pickups)
        self.sound = SoundHandler(self)
        self.progress = Progress(self.player, self.progress_value)
    
    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.quest_handler.update()
        self.text_handler.update()
        self.progress.update()
        self.map.update()
        
        pg.display.flip()
        
        if 'kamienica' not in self.quest_handler.quests:
            self.first_final_event = True 
        
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() : .1f}')
        
    def draw(self):
        self.screen.fill('black')
        self.texture_loader.draw()
    
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.x =  False
            elif event.type == pg.KEYDOWN and event.key == pg.K_q:
                self.expand_quests = not self.expand_quests
            elif event.type == pg.KEYDOWN and event.key == pg.K_i:
                self.interaction = True

    def game_over(self):
        self.map.current_index = 0
        self.progress_value = 0
        self.x = False
    
    def get_game_result(self):
        return {
            'pos': (self.player.x, self.player.y), 
            'pickups': self.player.pickups, 
            'progress': self.progress.get_progress(), 
            'quests': (self.quest_handler.quests, self.quest_handler.quests_names),
            'win_condition': self.win_condition,
            'floor_index': self.map.current_index,
        }

    def run(self):
        self.x = True
        while self.x:
            if not self.player.alive:
                self.game_over()
            self.check_events()
            self.update()
            self.draw()
        return self.get_game_result()