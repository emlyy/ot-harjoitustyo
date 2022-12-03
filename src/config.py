import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

RAN_IMAGE = "src/images/ran-1.png"
BG_IMAGE = "src/images/cave_tilesheet-1.png"
NOTE_IMAGE = "src/images/star.png"
ENEMY_IMAGE = "src/images/woodgrem-2.2.png"
SPAWN_X = 20
SPAWN_Y = 290
BG_COLOR = (55,55,55)
WHITE = (255,255,255)
SCREEN_SIZE = (1184, 980)
SCREEN_WIDTH = 1184
BOX_HEIGHT = 344
RAN_SPEED = 3
BARRIERS_LIST = [[10,280,10,200],[330,10,0,195],[330,10,0,392],
[60,10,330,226],[60,10,330,360],[10,100,330,360],[10,31,330,195],
[10,210,386,360],[10,236,386,0],[520,10,386,550],[220,10,680,150],
[60,10,900,222],[314,10,386,100],[10,160,680,0],[200,10,950,190],
[200,10,950,387],[10,207,1150,190],[10,32,950,190],[10,72,900,150],
[10,204,900,356],[58,10,900,356],[10,60,948,356],[118,10,710,430],
[10,30,710,430]]
T_CORDS_X = 30
T_CORDS_Y1 = 650
T_CORDS_Y2 = 750
T_CORDS_Y3 = 850
Y2 = 760
Y3 = 860
D_BOX = 8
D_BOX_X = 18
NOTE_X = 235
NOTE_Y = 295
ENEMY_1_X = 780
ENEMY_1_Y = 270
#learn how to use os.getenv("") or
