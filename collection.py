import pygame as pg
from config import *
from item import *

class Collection():
    def __init__(self, menu) -> None:
        self.menu = menu
        self.bg_surf = pg.image.load('resources/graphics/pavement_surf.jpg')
        self.bg_surf = pg.transform.scale(self.bg_surf, (1600,900))
        self.bg_rect = self.bg_surf.get_rect(topleft = (0,0))
        self.pressed_index = -1
        self.j = 70
        self.items = [Item(i) for i in range(8)]
        self.visible_items = []
        self.bg_info_surf = pg.image.load('resources/graphics/blank_sheet.png')
        self.bg_info_surf = pg.transform.scale(self.bg_info_surf, (750,792))
        self.bg_info_rect = self.bg_info_surf.get_rect(center = (1100,450))
        self.blanket_surf = pg.image.load('resources/graphics/blanket_light.jpg')
        self.blanket_surf = pg.transform.scale(self.blanket_surf, (400,500))
        self.blanket_rect = self.blanket_surf.get_rect(center = (350,400))

    
    def display(self):
        screen.blit(self.bg_surf,self.bg_rect)
        screen.blit(self.bg_info_surf, self.bg_info_rect)
        screen.blit(self.blanket_surf, self.blanket_rect)
        for pickup_taken in self.menu.pickups:
            for i in range(8):
                if self.items[i].name == pickup_taken[2]:
                    self.items[i].visible = True
        for i in range(8):
          self.items[i].draw() 

    def check_events(self,items):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.x =  False
            if event.type == pg.MOUSEBUTTONDOWN:
                for j in range(len(pickup_names)):
                    if self.items[j].image_rect.collidepoint(event.pos) and self.items[j].visible:
                        if self.pressed_index!= -1:
                            self.items[self.pressed_index].expanded = False
                        self.pressed_index = j
                        self.items[self.pressed_index].expanded = True

    def run(self,items):
        self.x = True
        while self.x:
            self.check_events(items)
            self.display()
            pg.display.update()