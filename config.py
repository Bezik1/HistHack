import pygame as pg
from game.constans import *
pg.init()
#options(buttons)
menu_options = ['Graj','Kolekcja']
#background
bg_image = pg.image.load('resources/graphics/bg_menu_3.jpg')
bg_image = pg.transform.scale(bg_image, (1600,900))
bg_rect = bg_image.get_rect(topleft = (0,0))
#wstazka
tail_image = pg.image.load('resources/graphics/papier.jpg')
tail_image = pg.transform.scale(tail_image, (350,900))
tail_rect = tail_image.get_rect(midtop = (1350,0))
#menu music
bg_music = pg.mixer.Sound('resources/audio/bg_music.mp3')
#logo
logo_surf = pg.image.load('resources/graphics/powstaniec_pomnik.png')
logo_surf = pg.transform.rotozoom(logo_surf, 0, 0.3)
logo_rect = logo_surf.get_rect(midbottom = (1350,900))
#screen
screen = pg.display.set_mode((1600,900))
pg.display.set_caption('Grand Theft Auto VI')
#items
pickup_names = ['aparat','bluzka','futeral','granat_karbidowy','helm','opaska','malpka','zegarek']
#font
menu_font = pg.font.Font('resources/font/Pixeltype.ttf',200)
