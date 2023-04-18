import pygame as pg
from config import *
from button import *
from sys import exit

class Menu:
    def __init__(self) -> None:
        pg.init()
        bg_music.set_volume(1)
        bg_music.play(loops = -1)
        
        self.pickups = []
        self.player_pos = PLAYER_POS
        self.game_over = False
        self.floor_index = 0
        self.quests = [{}, []]
        self.progress_value = 0
        self.clock = pg.time.Clock()
        self.menu = True
        self.FPS = 60
        self.button_list = []
        self.button_list.append(Button(self, 0, 100))
        self.button_list.append(Button(self, 1, 250))

    def draw(self):
        pg.display.update()
        self.clock.tick(self.FPS)
        screen.blit(bg_image,bg_rect)
        screen.blit(tail_image, tail_rect)
        screen.blit(logo_surf,logo_rect)
        for j in range(len(self.button_list)):
            screen.blit(self.button_list[j].text_surf, self.button_list[j].text_rect)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                for j in range(len(self.button_list)):
                    if self.button_list[j].text_rect.collidepoint(event.pos):
                        bg_music.stop()
                        self.button_list[j].pressing(j,screen)
                        bg_music.play(loops = -1)
    
    def run(self):
        while self.menu:
            pg.mouse.set_visible(True)
            self.draw()
            self.check_events()

if __name__ == '__main__':
    menu = Menu()
    menu.run()