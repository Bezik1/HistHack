from game.constans import *

class Progress:
    def __init__(self, player, progress_value) -> None:
        _ = False
        self.progress_value = progress_value
        self.progress_map = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
            [1, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
            [1, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
            [1, _, _, 1, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, 1, _, _, _, 1],
            [1, _, _, 1, _, _, _, _, _, _, _, 1, _, _, _, 1, 1, 1, 1, _, _, _, _, _, _, _, _, 1, _, _, _, 1],
            [1, _, 1, 1, _, _, _, _, _, _, _, 1, _, _, _, 1, _, _, _, _, _, _, _, _, 1, 1, 1, 1, _, _, _, 1],
            [1, _, 1, _, _, _, _, 1, 1, 1, 1, 1, _, _, _, 1, _, _, _, _, _, _, _, _, 1, _, _, _, _, _, _, 1],
            [1, _, 1, _, _, _, _, 1, _, _, _, 1, _, _, _, 1, _, _, 1, _, _, _, _, _, 1, _, _, _, _, _, _, 1],
            [1, _, 1, _, _, _, _, 1, _, _, _, 1, _, _, _, 1, _, _, 1, _, _, _, _, _, 1, _, _, _, _, _, _, 1],
            [1, _, 1, _, _, _, _, 1, _, _, _, 1, 1, 1, 1, 1, _, _, 1, 1, _, _, 1, 1, 1, _, _, _, _, _, _, 1],
            [1, _, 1, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, 1, _, _, 1, _, _, _, _, _, _, _, _, 1],
            [1, _, 1, 1, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, 1, _, _, 1, _, _, _, _, _, _, _, _, 1],
            [1, _, _, _, _, _, _, 1, _, _, _, 1, 1, 1, 1, 1, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, 1],
            [1, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, 1],
            [1, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
            [1, _, _, _, _, _, _, 1, 1, 1, 1, 1, _, _, 1, 1, 1, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
            [1, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
            [1, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
            [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
            [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
            [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]

        self.player = player
        self.all_counter = 0
        self.wall_counter = 0
        for row in self.progress_map:
            for i in row:
                if i:
                    self.wall_counter += 1
                self.all_counter += 1
    
    def get_progress(self):
        counter = 0
        for row in self.progress_map:
            for i in row:
                if i:
                    counter += 1
        
        return round((counter - self.wall_counter + self.progress_value) / (self.all_counter - self.wall_counter) * 100)
    
    def update(self):
        x, y = int(self.player.pos[0]), int(self.player.pos[1])
        if not self.progress_map[y][x]:
            self.progress_map[y][x] = True
        #print(f'{self.get_progress()}%')