import pygame as pg
from game.constans import *

class QuestHandler:
    def __init__(self, game, quests) -> None:
        self.game = game
        self.screen = game.screen
        self.quests = quests[0]
        self.quests_names = quests[1]
        self.succesed_quests = []
        
        self.image = pg.image.load('resources/graphics/note.png')
        self.image = pg.transform.scale(self.image, (450, 600))
    
    def get_index_by_name(self, name):
        return self.quests_names.index(name)
    
    def draw(self):
        #surface = pg.Surface((420,600), pg.SRCALPHA)
        #surface.fill((0, 0, 0, 168)) 
        #self.screen.blit(surface, (WIDTH - surface.get_width(), HEIGHT // 2 - surface.get_height() // 2))
        self.screen.blit(self.image, (WIDTH - self.image.get_width(), HEIGHT // 2 - self.image.get_height() // 2 - 50))
        font = pg.font.Font(None, 40)
        text_surface = font.render('Zadania:', True, (0, 0, 0))
        self.screen.blit(text_surface, (WIDTH - text_surface.get_width() - 160, 
                                        HEIGHT // 2 - text_surface.get_height() - 220))
    
    def remove_quest(self, key):
        self.quests.pop(key)
        self.quests_names.remove(key)
        self.succesed_quests.append(key)
    
    def update(self):
        if self.game.expand_quests:
            self.draw()
        [self.quests[key].update() for key in self.quests]
        pickups_names = [pickup[2] for pickup in self.game.player.pickups]
        first_floor_basic_quests_condition = 'szukanie' in self.succesed_quests and 'bluzka' in self.succesed_quests
        
        if ('helm' in pickups_names and 'opaska' in pickups_names) and self.quests.get('szukanie', False):
            self.quests['szukanie'].status = True
            self.remove_quest('szukanie')
        
        if first_floor_basic_quests_condition and self.game.quest_handler.quests.get('pomoc', False):
            self.game.quest_handler.quests['pomoc'].status = True
            self.game.quest_handler.remove_quest('pomoc')
        
        if first_floor_basic_quests_condition and 'pomoc' in self.succesed_quests:
            self.game.win_condition = True
        
    def add_quest(self, name, quest):
        self.quests[name] = quest
        self.quests_names.append(name)

class Quest:
    def __init__(self, game, text, name) -> None:
        self.game = game
        self.screen = game.screen
        self.text = text
        self.name = name
        self.status = False
    
    def change_status(self):
        self.status = True
    
    def draw(self):
        font = pg.font.Font(None, 24)
        text_arr = self.text.split('\n')
        for i, text in enumerate(text_arr):
            text_surface = font.render(f'{self.game.quest_handler.get_index_by_name(self.name)+1}. {text}', True, (0, 0, 0))
            self.screen.blit(text_surface, (WIDTH - text_surface.get_width() - 120, 
                            (HEIGHT // 3) + self.game.quest_handler.get_index_by_name(self.name)*30 + 30*i - 55))
    
    def update(self):
        if not self.status and self.game.expand_quests:
            self.draw()