import math, pygame as pg
from game.constans import *
from game.quest_handler import Quest
import os
from collections import deque

class Object:
    def __init__(self, game, path='resources/objects/static_objects/bookshelf.png',
                 pos=(10.5, 8.5), scale=1, shift=0.1, floor=0):
        self.game = game
        self.floor = floor
        self.player = game.player
        self.visible = False
        self.x, self.y = pos
        self.image = pg.image.load(path).convert_alpha()
        self.IMAGE_WIDTH = self.image.get_width()
        self.IMAGE_HALF_WIDTH = self.image.get_width()
        self.IMAGE_RATIO = self.IMAGE_WIDTH / self.image.get_height()
        self.dx, self.dy, self.theta, self.screen_x, self.dist, self.norm_dist = 0, 0, 0, 0, 1, 1
        self.object_half_width = 0
        self.OBJECT_SCALE = scale
        self.OBJECT_HEIGHT_SHIFT = shift

    def get_object_projection(self):
        proj = SCREEN_DIST / self.norm_dist * self.OBJECT_SCALE
        proj_width, proj_height = proj * self.IMAGE_RATIO, proj

        image = pg.transform.scale(self.image, (proj_width, proj_height)).convert_alpha()

        self.object_half_width = proj_width // 2
        height_shift = proj_height * self.OBJECT_HEIGHT_SHIFT
        pos = self.screen_x - self.object_half_width, HALF_HEIGHT - proj_height // 2 + height_shift

        self.game.raycasting.objects_to_render.append((self.norm_dist, image, pos))

    def get_object(self):
        dx = self.x - self.player.x
        dy = self.y - self.player.y
        self.dx, self.dy = dx, dy
        self.theta = math.atan2(dy, dx)

        delta = self.theta - self.player.angle
        if (dx > 0 and self.player.angle > math.pi) or (dx < 0 and dy < 0):
            delta += math.tau

        delta_rays = delta / DELTA_ANGLE
        self.screen_x = (HALF_NUM_RAYS + delta_rays) * SCALE

        self.dist = math.hypot(dx, dy)
        self.norm_dist = self.dist * math.cos(delta)
        if -self.IMAGE_HALF_WIDTH < self.screen_x < (WIDTH + self.IMAGE_HALF_WIDTH) and self.norm_dist > 0.5:
            self.get_object_projection()

    def update(self):
        if self.floor == self.game.map.current_index:
            self.visible = True
        else:
            self.visible = False
        if self.visible:
            self.get_object()

class NPC(Object):
    def __init__(self, game, path='resources/objects/npc/wizard.png',
                 pos=(1.5, 6.5), name='Czarodziej', text=NPC_BASE_TEXT, func=lambda *args: None, floor=0, scale=0.9, shift=0.1):
        super().__init__(game, path, pos, scale, shift, floor)
        
        self.func = func
        self.name = name
        if not self.game.win_condition:
            self.text = text
        self.dialog_active = False
        self.trigger = True
        self.game.text_handler.add_text(name, text, name)
    
    def update(self):
        super().update()
        self.dialog_active = self.collision_detect()
        if (self.dialog_active and self.trigger) and self.visible:
            for key in self.game.text_handler.texts_active:
                self.game.text_handler.texts_active[key] = False
            self.game.text_handler.texts_active[self.name] = True
            self.func()
            self.trigger = False
    
    def collision_detect(self):
        px, py = self.game.player.pos
        distance_x = abs(px - self.x)
        distance_y = abs(py - self.y)
        if distance_x > 1.5 or distance_y > 1.5:
            return False
        return True

class InteractiveObject(Object):
        def __init__(self, game, path='resources/objects/pickups/heart.webp',
                        pos=(11.5, 3.5), interaction_fn=lambda *args: None, floor=0, scale=0.5, shift=0.01):
            super().__init__(game, path, pos, scale, shift)

            self.floor = floor
            self.interaction_fn = interaction_fn
            self.collisiton = False
            self.game.text_handler.add_text('ledder', 'Wciśnij i, aby przejść po drabinie')
        
        def update(self):
            self.collision = self.collision_detect()
            
            if self.collision and self.visible:
                for key in self.game.text_handler.texts_active:
                    self.game.text_handler.texts_active[key] = False
                self.game.text_handler.texts_active['ledder'] = True
                if self.game.interaction:
                    self.interaction_fn()
            super().update()
        
        def collision_detect(self):
            px, py = self.game.player.pos
            return int(px) == int(self.x) and int(py) == int(self.y)

class Pickup(Object):
    def __init__(self, game, path='resources/objects/pickups/heart.webp',
                 pos=(11.5, 3.5), name='Heart', floor=0, scale=0.5, shift=0.56):
        super().__init__(game, path, pos, scale, shift, floor)
        
        self.vanished = False
        self.item = (path, pos, name)
        game.text_handler.add_text(name, f'Podniosłeś {name}!')
    
    def update(self):
        self.collision_detect()
        if not self.vanished:
            super().update()
    
    def collision_detect(self):
        px, py = self.game.player.pos
        if ((int(self.x), int(self.y)) == (int(px), int(py)) and self.vanished == False) and self.visible:
            self.vanished = True
            self.game.player.add_pickup(self.item)
            self.game.sound.pickup_item.play()
            for key in self.game.text_handler.texts_active:
                self.game.text_handler.texts_active[key] = False
            self.game.text_handler.texts_active[self.item[2]] = True

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

class AnimatedObject(Object):
    def __init__(self, game, path='resources/objects/animated_objects/green_light/0.png',
                 pos=(11.5, 3.5), scale=0.8, shift=0.16, animation_time=120):
        super().__init__(game, path, pos, scale, shift)
        self.animation_time = animation_time
        self.path = path.rsplit('/', 1)[0]
        self.images = self.get_images(self.path)
        self.animation_time_prev = pg.time.get_ticks()
        self.animation_trigger = False

    def update(self):
        super().update()
        self.check_animation_time()
        self.animate(self.images)

    def animate(self, images):
        if self.animation_trigger:
            images.rotate(-1)
            self.image = images[0]

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