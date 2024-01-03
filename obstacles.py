import pygame,random
import sprites

'''
OBSTACLE CLASSES
type
rect
sprite
reset(self,screen)
update(self,screen)
'''

OBSTACLES1=["dog"]
OBSTACLES2=["house"]

WIDTH=400

LAYER1=270  #GROUND
LAYER2=180  #WALL
LAYER3=90   #ROOF

onscreen=[] #obstacles objects visible onscreen
standableobjlist=[]

timer=0.0
lastspawntime=0.0

windowx2=270
windowx1=60
windowy=105

hitbox=True

class house:
    def __init__(self,rect:pygame.Rect,roof:pygame.Rect) -> None:
        global standablerect
        self.randomize()
        self.type="house"
        self.sprite=sprites.HOUSESPRITE
        self.x=WIDTH
        self.rect=rect
        self.roof=roof
        self.y=12
    def randomize(self):
        match random.randint(1,4):
            case 1:
                self.leftwsprite=sprites.WINDOWOPENSPRITE
                self.rightwsprite=sprites.WINDOWCLOSEDSPRITE
            case 2:
                self.leftwsprite=sprites.WINDOWOPENSPRITE
                self.rightwsprite=sprites.WINDOWOPENSPRITE
            case 3:
                self.leftwsprite=sprites.WINDOWCLOSEDSPRITE
                self.rightwsprite=sprites.WINDOWCLOSEDSPRITE
            case 4:
                self.leftwsprite=sprites.WINDOWCLOSEDSPRITE
                self.rightwsprite=sprites.WINDOWOPENSPRITE
    def update(self,screen):
        global onscreen
        self.x-=speed2
        self.rect.x-=speed2
        self.roof.x-=speed2
        screen.blit(sprites.HOUSESPRITE,(self.x,self.y))
        screen.blit(self.leftwsprite,(self.x+windowx1,self.y+windowy))
        screen.blit(self.rightwsprite,(self.x+windowx2,self.y+windowy))
        if self.x+sprites.HOUSEWIDTH<0:
            onscreen.pop(onscreen.index(self))
            self.reset(screen)
    def reset(self,screen):
        self.roof.x=WIDTH
        self.rect.x=WIDTH
        self.randomize()
        self.x=WIDTH
        self.y=12
        screen.blit(self.sprite,(self.x,self.y))

class dog:
    def __init__(self) -> None:
        self.xoffset=15
        self.yoffset=20
        self.type="dog"
        self.rect=pygame.Rect(
            WIDTH,
            LAYER1-sprites.DOGHEIGHT,
            sprites.DOGWIDTH-self.xoffset,
            sprites.DOGHEIGHT-self.yoffset
            )
        self.sprite=sprites.DOGSPRITE
    def reset(self,screen):
        self.rect.left=WIDTH
        self.rect.bottom=LAYER1
        screen.blit(self.sprite,(self.rect.x-self.xoffset,self.rect.y-self.yoffset))
    def update(self,screen):
        global onscreen
        if hitbox==True:
            screen.fill("purple",self.rect)
        self.rect.x-=speed1 #self.rect.x=self.rect.x-speed1    rect-=speed      rect=rect-speed
        screen.blit(self.sprite,(self.rect.x-self.xoffset,self.rect.y-self.yoffset))
        if self.rect.right<=0:
            onscreen.pop(onscreen.index(self))
            self.reset(screen)

dog1=dog()
dog2=dog()

hserect1=pygame.Rect(WIDTH,175,sprites.HOUSEWIDTH,13)
hserectroof=pygame.Rect(WIDTH,84,sprites.HOUSEWIDTH,13)
hse=house(rect=hserect1,roof=hserectroof)

LAYER1OBS=[dog1,dog2]
LAYER2OBS=[hse]
LAYER3OBS=[]

standablerect=[hserect1,hserectroof]

speed1=5
speed2=4
diff=3


def spawn(screen):
    layerlist=LAYER1OBS
    match random.randint(1,2):
        case 1:
            layerlist=LAYER1OBS
        case 2:
            layerlist=LAYER2OBS
        case 3: 
            layerlist=LAYER3OBS
    new=layerlist[random.randint(0,len(layerlist)-1)]
    if not new in onscreen:
        new.reset(screen)
        onscreen.append(new)


def restart(screen):
    for obj in onscreen:
        obj.reset(screen)

def update(SCREEN,Cat,curscreen):
    global lastspawntime,timer
    timer=pygame.time.get_ticks()
    if len(onscreen)<diff:
        if timer-lastspawntime>1000.0:
            lastspawntime=timer
            spawn(SCREEN)
    for obj in onscreen:
        obj.update(SCREEN)
    for obj in standableobjlist:
        obj.update(SCREEN)

    