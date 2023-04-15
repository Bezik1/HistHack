from game.objects.Object import Object

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