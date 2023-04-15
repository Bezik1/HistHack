from game.objects.Object import Object

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