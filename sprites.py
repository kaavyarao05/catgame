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

ANGRYCATSPRITE=pygame.image.load(os.path.join('assets',"angrycat.png"))

MENUSPRITE=pygame.image.load(os.path.join('assets','menu.jpg'))
LOSE=pygame.image.load(os.path.join('assets','catcrying.jpg'))
LOSESPRITE=pygame.transform.scale(LOSE,(450,450)) 

HOUSESPRITE=pygame.image.load(os.path.join('assets',"house.png"))
HOUSEWIDTH=442
HOUSEHEIGHT=257

WINDOWOPENSPRITE=pygame.image.load(os.path.join('assets',"windowopen.png"))
WINDOWCLOSEDSPRITE=pygame.image.load(os.path.join('assets',"windowclosed.png"))
WINDOWWIDTH=101
WINDOWHEIGHT=56

GROUNDSPRITE=pygame.image.load(os.path.join('assets','ground.jpeg'))
GROUNDWIDTH=442
GROUNDHEIGHT=32