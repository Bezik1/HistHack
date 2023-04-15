from game.objects.Object import Object
from game.constans import *

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