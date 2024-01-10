import pygame,os

CATSPRITE1=pygame.image.load(os.path.join('assets',"run1.png"))
CATSPRITE2=pygame.image.load(os.path.join('assets',"run2.png"))
CATSPRITE3=pygame.image.load(os.path.join('assets',"run3.png"))
CATSPRITE4=pygame.image.load(os.path.join('assets',"run4.png"))
CATSPRITE5=pygame.image.load(os.path.join('assets',"run5.png"))
CATSPRITE6=pygame.image.load(os.path.join('assets',"run6.png"))
CATSPRITE7=pygame.image.load(os.path.join('assets',"run7.png"))
CATWIDTH=65
CATHEIGHT=50

DOGSPRITE=pygame.image.load(os.path.join('assets',"dog.png"))
DOGWIDTH=101
DOGHEIGHT=80

EAGLESPRITE=pygame.image.load(os.path.join('assets',"eagle.png"))
EAGLEHEIGHT=90
EAGLEWIDTH=90

ANGRYCATSPRITE=pygame.image.load(os.path.join('assets',"angrycat.png"))
ANGRYCATHEIGHT=47
ANGRYCATWIDTH=97

OBSTACLES={
    "dog":{
        "sprite":DOGSPRITE,
        "height":DOGHEIGHT,
        "width":DOGWIDTH
    },
    "eagle":{
        "sprite":EAGLESPRITE,
        "height":EAGLEHEIGHT,
        "width":EAGLEWIDTH
    }
}

MENUSPRITE=pygame.image.load(os.path.join('assets','menu.png'))
LEADERBOARDSPRITE=pygame.image.load(os.path.join('assets','leaderboard.png'))
LOSE=pygame.image.load(os.path.join('assets','catcrying.jpg'))
LOSESPRITE=pygame.transform.scale(LOSE,(450,450)) 

HOUSESPRITE=pygame.image.load(os.path.join('assets',"house.png"))
HOUSEWIDTH=442
HOUSEHEIGHT=257

WINDOWOPENSPRITE=pygame.image.load(os.path.join('assets',"windowopen.png"))
WINDOWCLOSEDSPRITE=pygame.image.load(os.path.join('assets',"windowclosed.png"))
WINDOWWIDTH=101
WINDOWHEIGHT=56

SKYSPRITE=pygame.image.load(os.path.join('assets',"sky.png"))
SKYWIDTH=400
BUSHSPRITE=pygame.image.load(os.path.join('assets',"bushes.png"))
BUSHWIDTH=400

GROUNDSPRITE=pygame.image.load(os.path.join('assets','ground.jpeg'))
GROUNDWIDTH=442
GROUNDHEIGHT=32