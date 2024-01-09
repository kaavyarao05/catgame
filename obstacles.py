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
    def __init__(self,rect1:pygame.Rect,roof:pygame.Rect,rect2:pygame.Rect) -> None:
        global standablerect
        self.randomize()
        self.type="house"
        self.sprite=sprites.HOUSESPRITE
        self.x=WIDTH
        self.rect1=rect1
        self.rect2=rect2
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
        self.rect1.x-=speed2
        self.rect2.x-=speed2
        self.roof.x-=speed2
        screen.blit(sprites.HOUSESPRITE,(self.x,self.y))
        screen.blit(self.leftwsprite,(self.x+windowx1,self.y+windowy))
        screen.blit(self.rightwsprite,(self.x+windowx2,self.y+windowy))
        if self.x+sprites.HOUSEWIDTH<0:
            onscreen.pop(onscreen.index(self))
            self.reset(screen)
    def reset(self,screen):
        self.roof.x=WIDTH
        self.rect1.x=WIDTH
        self.rect2.x=WIDTH+270
        self.randomize()
        self.x=WIDTH
        self.y=12
        screen.blit(self.sprite,(self.x,self.y))

class obstacle:
    def __init__(self,type,layer) -> None:
        self.xoffset=15
        self.yoffset=20
        self.type=type
        self.layer=layer
        self.rect=pygame.Rect(
            WIDTH,
            layer-sprites.OBSTACLES[type]["height"],
            sprites.OBSTACLES[type]["width"]-self.xoffset,
            sprites.OBSTACLES[type]["height"]-self.yoffset
            )
        self.sprite=sprites.OBSTACLES[type]["sprite"]
    def reset(self,screen):
        self.rect.left=WIDTH
        self.rect.bottom=self.layer
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

dog1=obstacle("dog",LAYER1)
dog2=obstacle("dog",LAYER1)

eagle1=obstacle("eagle",LAYER3)
eagle2=obstacle("eagle",LAYER3)

hserect1=pygame.Rect(WIDTH,175,173,1)
hserect2=pygame.Rect(WIDTH+270,175,173,1)
hserectroof=pygame.Rect(WIDTH,84,sprites.HOUSEWIDTH,13)
hse=house(rect1=hserect1,roof=hserectroof,rect2=hserect2)

LAYER1OBS=[dog1,dog2]
LAYER2OBS=[hse]
LAYER3OBS=[eagle1,eagle2]

standablerect=[hserect1,hserectroof,hserect2]

speed1=5
speed2=4
diff=3
standablefreq=2

def housespawn(SCREEN):
    pass

def spawn(screen):
    layerlist=LAYER1OBS
    match random.randint(1,3):
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
    if len(standableobjlist)<standablefreq:
        pass
    for obj in standableobjlist:
        obj.update(SCREEN)

    