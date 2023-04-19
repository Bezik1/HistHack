import math

# game settings
RES = WIDTH, HEIGHT = 1600, 900
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60

#player settings
PLAYER_POS = 1.5, 1.5 #mini_map
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004
PLAYER_RUSH_SPEED = 0.008
PLAYER_ROT_SPEED = 0.002
PLAYER_SIZE_SCALE = 60
PLAYER_MAX_HEALTH = 100

#mouse settings
MOUSE_SENSITIVITY = 0.0003
MOUSE_MAX_REL = 40
MOUSE_BORDER_LEFT = 100
MOUSE_BORDER_RIGHT = WIDTH - MOUSE_BORDER_LEFT

FLOOR_COLOR = (30, 30, 30)

#raycaster settings
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20

#3D projection settings
SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS

#textures
TEXTURE_SIZE = 256
HALF_TEXTURE_SIZE = TEXTURE_SIZE // 2
WALL_TEXTURES = [
    'resources/textures/1.png',
    'resources/textures/2.png',
]

#text
RAW_TEXT = 'Podniosłeś serce \n Gratulacje!!'
JUMP_TEXT = 'Podniosłeś jump \n Gratulacje!!'
PLAYER_0_TEXT = 'Podniosłeś player0 \n Gratulacje!!'
SOLDIER_TEXT = '''Musisz dotrzeć kanałami do kamienicy,
aby dostarczyć ważną wiadomość do dowództwa.
Pamiętaj, aby zachować szczególną ostrożność.
Jako nasz człowiek masz również obowiązek pomagać cywilom,
jak i każdemu z naszego oddziału.
A posłuchaj i najważniejsze
Uważaj na granaty!!'''

OLD_LADY_TEXT = '''Młodzieńcze, uszyłam bardzo wytrzymałą bluzkę.
Czy mógłbyś wziąść ją ze sobą i przekazać sanitariuszce z tamtej bazy? 
Jak ona tam miała... Jasia?'''

SOCIAL_HELPER_TEXT = 'Dziękuję, pozdrów krawcową gdy ją spotkasz!'

FIND_HAT_TEXT = '''Witaj, jeden z naszych zgubił w kanałach na szlaku hełm
- rozjerzyj się za nim przy okazji. 
Może być tam coś jeszcze... Miej to na uwadze.'''

REBEL_TEXT = ''' Szybko szkopy będą tu za 15 minut!
Musimy się schować inaczej dowództwo nigdy nie dostanie wiadomości.
Najlepszym wyjściem, będzie pójście do kanałów.'''

REBEL2_TEXT = 'Pomóż wszystkim ludziom, aby przekazać mi wiadomość'

TEXTS_ARRAY = RAW_TEXT.split('\n')

TIME_PER_SIGN = 150

#floor
FLOOR_COLOR = (60, 60, 60)
CEILING_COLOR = (200, 200, 200)

#NPC
NPC_BASE_TEXT = "Czary mary \n Hokus pokus \n Abra kadabra"

#base game result
BASE_GAME_RESULT = {
    'pos': PLAYER_POS,
    'pickups': [], 
    'progress': 0, 
    'quests': [{}, []],
    'win_condition': False,
    'floor_index': 0,
}