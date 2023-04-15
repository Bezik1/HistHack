from game.objects.Object import Object
from game.constans import *
import os, pygame as pg
from collections import deque

class AnimatedNPC(Object):
        def __init__(self, game, path='resources/objects/npc/animated/0.png',
                 pos=(1.5, 6.5), name='Powstaniec3', text=REBEL_TEXT, end_pos=(0, 0), 
                 event=False, animation_time=60, floor=0, scale=0.9, shift=0.1):
            super().__init__(game, path, pos, scale, shift, floor)
            
            self.name = name
            self.text = text
            self.event = event
            self.speed = 0.03
            self.default_img = pg.image.load('resources/objects/npc/powstaniec3.png').convert_alpha()
            self.end_pos = self.end_x, self.end_y = end_pos
            self.animation_time = animation_time
            self.path = path.rsplit('/', 1)[0]
            self.images = self.get_images(self.path)
            self.animation_time_prev = pg.time.get_ticks()
            
            self.game.text_handler.add_text(name, text, name)
            self.first_active = True

        def check_wall(self, x, y):
            return (x, y) not in self.game.map.world_map
        
        def check_wall_collistion(self, dx, dy):
            if self.check_wall(int(self.x + dx), int(self.y)):
                self.x += dx
            if self.check_wall(int(self.x), int(self.y + dy)):
                self.y += dy

        def goto_end_pos(self):            
            angle = math.atan2(self.end_y + 0.5 - self.y, self.end_x + 0.5 - self.x)
            dx = math.cos(angle) * self.speed
            dy = math.sin(angle) * self.speed
            self.check_wall_collistion(dx, dy)
            
        def update(self):
            super().update()
            #if self.event:
            self.check_animation_time()
            self.animate(self.images)
            
            self.dialog_active = self.collision_detect()
            if self.dialog_active and self.first_active:
                for key in self.game.text_handler.texts_active:
                    self.game.text_handler.texts_active[key] = False
                self.game.text_handler.texts_active[self.name] = True
                self.first_active = False

        def animate(self, images):
            if (round(self.end_x), round(self.end_y)) != (round(self.x), round(self.y)):
                self.goto_end_pos()
                images.rotate(-1)
                self.image = images[0]
            else:
                self.image = self.default_img

        def check_animation_time(self):
            time_now = pg.time.get_ticks()
            if time_now - self.animation_time_prev > self.animation_time:
                self.animation_time_prev = time_now

        def get_images(self, path):
            images = deque()
            for file_name in os.listdir(path):
                if os.path.isfile(os.path.join(path, file_name)):
                    img = pg.image.load(path + '/' + file_name).convert_alpha()
                    images.append(img)
            return images

        def collision_detect(self):
            px, py = self.game.player.pos
            distance_x = abs(px - self.x)
            distance_y = abs(py - self.y)
            if distance_x > 2.5 or distance_y > 2.5:
                return False
            return True