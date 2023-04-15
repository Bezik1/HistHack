from game.objects.Object import Object
from game.constans import *
import os, pygame as pg
from collections import deque

class Grenade(Object):
    def __init__(self, game, pos=(5.5, 4.5), floor=0, name='Grenade', 
                 scale=5, shift=-5.56, animation_time=120, path='resources/items/small/explosion/0.png'):
        super().__init__(game, path, pos, scale, shift, floor)

        self.name = name
        
        #falling animation properties
        self.fall_animation_time = 20
        self.animation_start = False
        self.collision = False
        self.voice = False
        self.trigger = True
        
        #explosion animation
        self.animation_time = animation_time
        self.path = path.rsplit('/', 1)[0]
        self.images = self.get_images(self.path)
        self.animation_time_prev = pg.time.get_ticks()
        self.animation_trigger = False
        self.current_animation_index = 0
        
        self.game.text_handler.add_text(self.name, 'Trrr Trrr Trr')

    def fall_animation(self):
        if self.fall_animation_time >= 0 and self.animation_start:
            self.OBJECT_HEIGHT_SHIFT += 0.27
            self.fall_animation_time -= 1
        elif self.fall_animation_time <= 0:
            self.check_animation_time()
            self.animate(self.images)
            
            if self.current_animation_index == len(self.images) and self.collision:
                self.game.player.alive = False

    def update(self):
        self.fall_animation()
        self.collision = self.collision_detect()
        
        self.voice = self.voice_detect()
        
        if (self.voice and self.trigger) and self.visible:
            self.game.sound.achtung_sound.play()
            self.trigger = False
        
        if self.collision and self.visible:
            self.animation_start = True
            for key in self.game.text_handler.texts_active:
                self.game.text_handler.texts_active[key] = False
            self.game.text_handler.texts_active[self.name] = True
        super().update()
    
    def voice_detect(self):
        px, py = self.game.player.pos
        distance_x = abs(self.x - px)
        distance_y = abs(self.y - py)
        if distance_x > 2.4 or distance_y > 2.4:
            return False
        return True
    
    def collision_detect(self):
            px, py = self.game.player.pos
            distance_x = abs(px - self.x)
            distance_y = abs(py - self.y)
            if distance_x > 1.5 or distance_y > 1.5:
                return False
            return True

    def animate(self, images):
        if self.animation_trigger:
            self.current_animation_index  += 1
            if self.current_animation_index < len(self.images):
                self.image = images[self.current_animation_index]
                self.image = pg.transform.scale(self.image, (1000, 1000)).convert_alpha()
            else:
                return False

    def check_animation_time(self):
        self.animation_trigger = False
        time_now = pg.time.get_ticks()
        if time_now - self.animation_time_prev > self.animation_time:
            self.animation_time_prev = time_now
            self.animation_trigger = True

    def get_images(self, path):
        images = deque()
        for file_name in os.listdir(path):
            if os.path.isfile(os.path.join(path, file_name)):
                img = pg.image.load(path + '/' + file_name).convert_alpha()
                images.append(img)
        return images