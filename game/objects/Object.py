import math, pygame as pg
from game.constans import *

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