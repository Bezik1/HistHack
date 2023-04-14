from game.object_loader import *
from game.quest_handler import Quest

class ObjectHandler:
    def __init__(self, game, pickups) -> None:
        self.game = game
        
        self.object_list = []
        self.pickups_picked = pickups
        self.pickups_list = []
        self.interactive_object_list = []
        self.weapons_list = []
        self.first_floor_pickups = []
        
        pickup_path = 'resources/items/small/'
        npc_path = 'resources/objects/npc/'
        static_object_path = 'resources/objects/static_objects/'
        
        #objects
        def help_quest():
            self.game.quest_handler.add_quest('pomoc', Quest(self.game, 'Pomóż cywilom i powstańcom', 'pomoc'))
            self.game.quest_handler.add_quest('list', Quest(self.game, 'Zanieś wiadomość do powstańca', 'list'))
        find_floor_1_quest = lambda: self.game.quest_handler.add_quest('szukanie', Quest(self.game, 'Znajdź zaginiony hełm i coś jeszcze', 'szukanie'))
        bring_blouse_quest = lambda: self.game.quest_handler.add_quest('bluzka', Quest(self.game, 'Zanieś bluzkę do sanitariuszki', 'bluzka'))
        
        def bring_blouse_quest_complete():
            if self.game.quest_handler.quests.get('bluzka', False):
                self.game.quest_handler.quests['bluzka'].status = True
                self.game.quest_handler.remove_quest('bluzka')
        
        def if_end_game():
            if self.game.win_condition:
                self.game.text_handler.add_text('Koniec', 'Brawo udało ci się ukończyć grę!')
                for key in self.game.text_handler.texts_active:
                    self.game.text_handler.texts_active[key] = False
                self.game.text_handler.texts_active['Koniec'] = True
                self.game.x = False
        
        #NPCs
        self.add_object(NPC(self.game, f'{npc_path}powstaniec4.png', (6.5, 1.5), 'Powstaniec', 
                            SOLDIER_TEXT, help_quest))

        self.add_object(NPC(self.game, f'{npc_path}staruszka.png', (1.5, 14.5), 'Staruszka', 
                    OLD_LADY_TEXT, bring_blouse_quest))

        self.add_object(NPC(self.game, f'{npc_path}sanitariuszka.png', (14.5, 4.5), 'Sanitariuszka', 
            SOCIAL_HELPER_TEXT, bring_blouse_quest_complete, 2))

        self.add_object(NPC(self.game, f'{npc_path}powstaniec2.png', (1.5, 7.5), 'Powstaniec_2', 
                    FIND_HAT_TEXT, find_floor_1_quest))
        
        self.add_object(NPC(self.game, f'{npc_path}powstaniec4.png', (30.5, 14.5), 'Powstaniec_3', 
                        REBEL2_TEXT, if_end_game, 2))
        
        #Animated NPCs
        self.add_object(AnimatedNPC(self.game, 'resources/objects/npc/animated/0.png', 
                       (6.5, 2.5), 'Powstaniec_4', REBEL_TEXT, (2.75, 1.5 )))
        
        #weapons
        #self.add_weapon(Grenade(self.game, (15.5, 2.5), 1)) - powodował błąd, którego nie mieliśmy czasu naprawić
        
        #interactive_objects
        self.add_interactive_object(InteractiveObject(self.game, f'{static_object_path}ledder.png', 
                                                      (8.5, 1.5), self.game.map.go_next, 0, 1.2))

        self.add_interactive_object(InteractiveObject(self.game, f'{static_object_path}ledder.png', 
                                                (8.5, 1.5), self.game.map.go_next, 1, 1.2, 0.2))

        self.add_interactive_object(InteractiveObject(self.game, f'{static_object_path}ledder.png', 
                                        PLAYER_POS, self.game.map.go_back, 2, 1.2, 0.2))

        self.add_interactive_object(InteractiveObject(self.game, f'{static_object_path}ledder.png', 
                                        PLAYER_POS, self.game.map.go_back, 1, 1.2, 0.2))

        #pickups
        self.add_pickup(Pickup(self.game, f'{pickup_path}granat_karbidowy.png', (11.5, 1.5), 'granat_karbidowy', 0, 0.29 , 1.5), 'granat_karbidowy')
        self.add_pickup(Pickup(self.game, f'{pickup_path}malpka.png', (14.5, 14.5), 'malpka', 0, 0.25, 1.5), 'malpka')
        self.add_pickup(Pickup(self.game, f'{pickup_path}futeral.png', (1.5, 18.5), 'futeral', 1), 'futeral')
        self.add_pickup(Pickup(self.game, f'{pickup_path}aparat.png', (20.5, 11.5), 'aparat', 0, 0.25, 1.5), 'aparat')
        self.add_pickup(Pickup(self.game, f'{pickup_path}bluzka.png', (20.5, 17.5), 'bluzka', 0, 0.25, 1.5), 'bluzka')
        self.add_pickup(Pickup(self.game, f'{pickup_path}helm.png', (28.5, 2.5), 'helm', 1, 0.25, 1.5), 'helm')
        self.add_pickup(Pickup(self.game, f'{pickup_path}opaska.png', (28.5, 1.5), 'opaska', 1, 0.25, 1.5), 'opaska')
        self.add_pickup(Pickup(self.game, f'{pickup_path}zegarek.png', (4.5, 1.5), 'zegarek', 1, 0.25, 1.5), 'zegarek')
        
    def update(self):
        [interactive_object.update() for interactive_object in self.interactive_object_list]
        [weapon.update() for weapon in self.weapons_list]
        [pickup.update() for pickup in self.pickups_list]
        [object.update() for object in self.object_list]
    
    def add_weapon(self, weapon):
        self.weapons_list.append(weapon)
    
    def add_interactive_object(self, object):
        self.interactive_object_list.append(object)
    
    def add_pickup(self, pickup, pickup_desc):
        if pickup_desc not in [pickup_picked[2] for pickup_picked in self.pickups_picked if len(self.pickups_picked) != 0]:
            self.pickups_list.append(pickup)
            
            if pickup.floor == 0:
                self.first_floor_pickups.append(pickup)
    
    def add_object(self, sprite):
        self.object_list.append(sprite)