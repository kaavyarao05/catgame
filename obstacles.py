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

onscreen=[]
timer=0.0
lastspawntime=0.0

defaultx=WIDTH+200

windowx2=270
windowx1=60
windowy=105

class house:
    def __init__(self) -> None:
        self.randomize()
        self.type="house"
        self.sprite=sprites.HOUSESPRITE
        self.x=WIDTH
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
        screen.blit(sprites.HOUSESPRITE,(self.x,self.y))
        screen.blit(self.leftwsprite,(self.x+windowx1,self.y+windowy))
        screen.blit(self.rightwsprite,(self.x+windowx2,self.y+windowy))
        if self.x+sprites.HOUSEWIDTH<0:
            onscreen.pop(onscreen.index(self))
            self.reset(screen)
    def reset(self,screen):
        self.randomize()
        self.x=WIDTH
        self.y=12
        screen.blit(self.sprite,(self.x,self.y))

class dog:
    def __init__(self,rect) -> None:
        self.type="dog"
        self.rect=rect
        self.sprite=sprites.DOGSPRITE
    def reset(self,screen):
        self.rect.left=WIDTH
        self.rect.bottom=LAYER1
        screen.blit(self.sprite,(self.rect.x,self.rect.y))
    def update(self,screen):
        global onscreen
        self.rect.x-=speed1
        screen.blit(self.sprite,(self.rect.x,self.rect.y))
        if self.rect.right<=0:
            onscreen.pop(onscreen.index(self))
            self.reset(screen)

Dog1Rect=pygame.Rect(WIDTH,LAYER1-sprites.DOGHEIGHT,sprites.DOGWIDTH,sprites.DOGHEIGHT)
Dog2Rect=pygame.Rect(WIDTH,LAYER1-sprites.DOGHEIGHT,sprites.DOGWIDTH,sprites.DOGHEIGHT)
dog1=dog(Dog1Rect)
dog2=dog(Dog2Rect)


hse=house()

LAYER1OBS=[dog1,dog2]
LAYER2OBS=[hse]


onscreen=[]

speed1=5
speed2=4
diff=3


def spawn(screen):
    match random.randint(1,2):
        case 1:
            new=LAYER1OBS[random.randint(0,len(LAYER1OBS)-1)]
            if not new in onscreen:
                new.reset(screen)
                onscreen.append(new)
        case 2:
            new=LAYER2OBS[random.randint(0,len(LAYER2OBS)-1)]
            if not new in onscreen:
                new.reset(screen)
                onscreen.append(new)
        case 3: 
            pass

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

    