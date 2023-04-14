import pygame as pg
from config import *


class Item():
    def __init__(self,index) -> None:
        self.expanded = False
        self.font_name = pg.font.Font('resources/font/Aller_Rg.ttf',50)
        self.font_text = pg.font.Font('resources/font/aleo.otf',25)
        self.name = pickup_names[index]
        self.text = (open(f'resources/items/descriptions/opis_{pickup_names[index]}.txt','r',encoding="utf-8").read())
        self.text_lines = self.text.split('\n')
        self.image_x = 0
        self.image_y = 0
        if index%2 == 0:#0,2,4,6
            self.x = 250
            self.y = 200 + index*50
        else:#1,3,5,7
            self.x = 450
            self.y = 200 + index*50
        self.pos_image = (self.x,self.y)

        self.mark_surf = pg.image.load(f'resources/graphics/question_mark.png')
        self.mark_surf = pg.transform.scale(self.mark_surf, (75,75))
        self.mark_rect = self.mark_surf.get_rect(center = (self.pos_image))
        self.image_surf = pg.image.load(f'resources/items/small/{self.name}.png')            
        self.image_surf = pg.transform.rotozoom(self.image_surf,0,2)
        self.image_rect = self.image_surf.get_rect(center = self.pos_image)
        self.text_lines_surfs = []
        self.text_lines_rects = []
        for line in self.text_lines:
            self.text_lines_surfs.append(self.font_text.render(line, False, (0,0,0)))
        for i in range(len(self.text_lines)):
            self.text_lines_rects.append(self.text_lines_surfs[i].get_rect(center = (1100,450 + i*30)))
        #expanded image
        self.big_image_surf = pg.image.load(f'resources/items/big/{self.name}.png')         
        self.big_image_rect = self.big_image_surf.get_rect(center = (1100,300))
        self.visible = False

    
    def draw(self):
        if self.expanded:
            screen.blit(self.big_image_surf,self.big_image_rect)
            for i in range(len(self.text_lines)):
                screen.blit(self.text_lines_surfs[i],self.text_lines_rects[i])
        if self.visible:
            screen.blit(self.image_surf,self.image_rect)
        else:
            screen.blit(self.mark_surf,self.mark_rect)