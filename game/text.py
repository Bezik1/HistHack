import pygame as pg
from game.constans import *

class Text:
    def __init__(self, game, text_arr=TEXTS_ARRAY) -> None:
        self.screen = game.screen
        self.game = game

        self.current_text_arr = text_arr
        
        self.font = pg.font.Font(None, 36)
        self.active = False

        self.string_index = 0
        self.char_index = 0
        self.current_string = self.current_text_arr[self.string_index]

        self.delay_time = 4000
        self.delay_start_time =0
        self.start_time = 0
    
    def stop_timer(self):
        if self.active:
            self.active = False
            self.delay_start_time = 0
            self.start_time = 0
    
    def start_timer(self):
        if not self.active:
            self.active = True
            self.delay_start_time = pg.time.get_ticks()
            self.start_time = pg.time.get_ticks()
    
    def update(self):
        if self.active:
            current_time = pg.time.get_ticks()
            if current_time - self.start_time >= TIME_PER_SIGN / len(self.current_string):
                self.char_index += 1
                if self.char_index >= len(self.current_string) and pg.time.get_ticks() -self. delay_start_time >= self.delay_time:
                    self.string_index += 1
                    if self.string_index >= len(self.current_text_arr):
                        return False
                    self.current_string = self.current_text_arr[self.string_index]
                    self.char_index = 0
                    self.delay_start_time = pg.time.get_ticks()
                
                self.draw_text(self.current_string[:self.char_index + 1], 36, (255, 255, 255))
                self.start_time = current_time
    
    def draw_text(self, text, size, color):
        font = pg.font.Font(None, size)
        text_surface = font.render(text, True, color)
        self.screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, HEIGHT - text_surface.get_height() - 50))