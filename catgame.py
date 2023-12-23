import pygame,os,pdb
import sprites

pygame.init()
WIDTH=400
HEIGHT=300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Catgame")
FPS=60

curscreen="game"

Ground=pygame.Rect(0,HEIGHT-sprites.GROUNDHEIGHT,sprites.GROUNDWIDTH,sprites.GROUNDHEIGHT)


#==========================CAT===========================
CATFRAMES=[
    sprites.CATSPRITE1,
    sprites.CATSPRITE2,
    sprites.CATSPRITE3,
    sprites.CATSPRITE4,
    sprites.CATSPRITE5,
    sprites.CATSPRITE6,
    sprites.CATSPRITE7
]
Cat=pygame.Rect(100,50,sprites.CATWIDTH,sprites.CATHEIGHT)
curcatframe=CATFRAMES[0]
catframeindex=0
catstate="run"

catgravity=0
#========================================================

def catanimate():
    match catstate:
        case "run":
            global curcatframe,catframeindex
            catframeindex+=0.15
            if catframeindex>6:
                catframeindex=0.0
            curcatframe=CATFRAMES[int(catframeindex)]
        case "jump":
            curcatframe=CATFRAMES[0]

def drawgame():
    screen.fill((255,255,255))
    screen.blit(sprites.GROUNDSPRITE,(Ground.x,Ground.y))
    catanimate()
    screen.blit(curcatframe,(Cat.x,Cat.y))
    pygame.display.update()

def game():
    global catgravity,catstate
    clock.tick(FPS)
    drawgame()
    for event in pygame.event.get():  
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE and catstate!="jump":
                catgravity= -10 
                catstate="jump"      
        if event.type == pygame.QUIT:
            pygame.quit()
            pdb.set_trace()
    catgravity+=0.5
    Cat.y+=catgravity
    if Cat.bottom>=Ground.y:
        Cat.bottom=Ground.y
        catstate="run"
   

    

def lose():
    return

def start():
    while True:
        match curscreen:
            case "game":
                game()
            case "lose":
                lose()

if __name__=="__main__":
    start()