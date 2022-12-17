import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

SCORE_FILE = os.getenv("SCORE_FILE") or "src/data/score_file.db"
RAN_IMAGE = "src/images/ran-1.png"
BG_IMAGE = "src/images/cave_tilesheet-1.png"
BG_IMAGE_2 = "src/images/cave_tilesheet-2.png"
BG_IMAGE_3 = "src/images/cave_tilesheet-3.png"
NOTE_IMAGE = "src/images/star.png"
ENEMY_IMAGE = "src/images/woodgrem-2.2.png"
KING_IMAGE = "src/images/gremking.png"
CHEESE_IMAGE = "src/images/cheese.png"
DECORE_1 = "src/images/decore-1.png"
DECORE_2 = "src/images/decore-2.png"
DECORE_3 = "src/images/decore-3.png"
DECORE_4 = "src/images/decore-6.png"
DECORE_5 = "src/images/decore-5.png"
INVIS = "src/images/invis3.png"
SPAWN_X = 20
SPAWN_Y = 290
BG_COLOR = (55,55,55)
WHITE = (255,255,255)
SCREEN_SIZE = (1184, 980)
SCREEN_WIDTH = 1184
BOX_HEIGHT = 344
RAN_SPEED = 3
DECORE_BARRIERS_2 = [[100,90,510,20],[100,50,590,90],[60,40,810,470],[58,40,522,460]]
DECORE_BARRIERS_3 = [[40,24,660,40],[90,24,690,100],[90,90,300,460]]
DECORE_2X = 590
DECORE_2Y = 120
DECORE_3X = 808
DECORE_3Y = 455
BARRIERS_LIST = [[10,280,10,200],[330,10,0,195],[330,10,0,392],
[60,10,330,226],[60,10,330,360],[10,100,330,360],[10,31,330,195],
[10,210,386,360],[10,236,386,0],[520,10,386,550],[220,10,680,150],
[60,10,900,222],[314,10,386,100],[10,160,680,0],[200,10,950,190],
[200,10,950,387],[10,207,1150,190],[10,32,950,190],[10,72,900,150],
[10,204,900,356],[58,10,900,356],[10,60,948,356],[118,10,710,430],
[10,30,710,430]]
BARRIERS_LIST_2 = [[10,280,10,200],[330,10,0,195],[330,10,0,392],
[60,10,330,226],[60,10,330,360],[10,100,330,360],[10,31,330,195],
[10,210,386,360],[10,236,386,0],[520,10,386,550],[210,10,690,150],
[60,10,900,222],[10,160,690,0],[200,10,950,190],
[200,10,950,387],[10,207,1150,190],[10,32,950,190],[10,72,900,150],
[10,204,900,356],[58,10,900,356],[10,60,948,356],[304,6,386,0]]
BARRIERS_LIST_3 = [[10,280,1164,200],[330,10,854,195],[330,10,854,392],
[60,10,794,226],[60,10,794,360],[10,100,844,360],[10,31,844,195],
[10,210,788,360],[10,236,788,0],[520,10,274,550],[220,10,274,150],
[60,10,226,222],[10,160,484,0],[220,10,10,190],
[220,10,10,387],[10,207,10,190],[10,32,226,190],[10,72,274,150],
[10,204,274,356],[58,10,226,356],[10,60,226,356],[304,6,494,0]]
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
ENEMY_2_X = 400
ENEMY_2_Y = 250
ENEMY_3_X = 500
ENEMY_3_Y = 270
ENEMY_4_X = 600
ENEMY_4_Y = 250
CHEESE_X = 540
CHEESE_Y = 445
