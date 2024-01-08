import pygame,os,pdb,sys
import sprites,obstacles,sqlconn

'''
sprites
stores sprites and their height and width

obstacles
restart() - restarts position of obstacles
update() - updates pos of obstacles, adds more if there arent enough on screen

'''

pygame.init()
WIDTH=400
HEIGHT=300
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Catgame")
FPS=60
curscreen="menu"

points=0
pointsinterval=500  #time interval to update points in milliseconds
lastpointinterval=0

hitbox=True

#=======================MENU===============================
BASE_FONT = pygame.font.Font(None, 32) 
user_text = '' 
INPUT_RECT = pygame.Rect(20, 80, 140, 32) 
#=========================================================

Ground=pygame.Rect(0,HEIGHT-sprites.GROUNDHEIGHT,sprites.GROUNDWIDTH,sprites.GROUNDHEIGHT)
#Wall=pygame.Rect(500,)
obstaclearray=[]

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
Cat=pygame.Rect(50,50,sprites.CATWIDTH-30,sprites.CATHEIGHT-30)
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

def collisioncheck():
    global curscreen,catgravity,catstate
    rectlist=[]
    for obj in obstacles.onscreen:
        if obj.type!="house":
            rectlist.append(obj.rect)
    if (pygame.Rect.collidelistall(Cat,rectlist))!=[]:
        curscreen="lose"
    for rect in obstacles.standablerect:
        if pygame.Rect.colliderect(Cat,rect) and catgravity>0:
            catgravity=0
            catstate="run"

def drawgame():
    SCREEN.fill((255,255,255))
    SCREEN.blit(sprites.GROUNDSPRITE,(Ground.x,Ground.y))
    obstacles.update(SCREEN,Cat,curscreen)
    if hitbox==True:
        SCREEN.fill("purple",Cat)
    catanimate()
    collisioncheck()
    SCREEN.blit(curcatframe,(Cat.x-15,Cat.y-30))
    if user_text=="":
        finaltext=str(points)
    else:
        finaltext=user_text+" : "+str(points)
    text_surface = BASE_FONT.render(finaltext, False, (0,0,0)) 
    SCREEN.blit(text_surface, (5, 5)) 
    pygame.display.update()

def game():
    global catgravity,catstate,curscreen,points,lastpointinterval
    timer=pygame.time.get_ticks()
    clock.tick(FPS)
    drawgame()
    for event in pygame.event.get():  
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE and catstate!="jump":
                catgravity= -9
                catstate="jump"
            if event.key==pygame.K_z:
                curscreen="lose"
            if event.key==pygame.K_x:
                print(obstacles.onscreen)
        if event.type == pygame.QUIT:
            pygame.quit()
            pdb.set_trace()
        
    if timer-lastpointinterval>pointsinterval:
        lastpointinterval=timer
        points+=1

    catgravity+=0.3
    Cat.y+=catgravity

    if Cat.bottom>=Ground.y:
        Cat.bottom=Ground.y
        catstate="run"
   
def menu():
    global user_text,curscreen,hitbox
    clock.tick(FPS)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit() 
            pdb.set_trace()    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:  
                user_text = user_text[:-1] 
            elif event.key==pygame.K_RETURN:
                curscreen="game"
            elif event.key==pygame.K_SPACE:
                hitbox=not hitbox
                obstacles.hitbox=hitbox
            elif len(user_text)<10: 
                user_text += event.unicode

    SCREEN.blit(sprites.MENUSPRITE,(0,0)) 
    text_surface = BASE_FONT.render(user_text, True, (78,105,111)) 
    SCREEN.blit(text_surface, (INPUT_RECT.x+5, INPUT_RECT.y+5)) 
    INPUT_RECT.w = max(100, text_surface.get_width()+10) 
    pygame.display.flip() 

def restart():
    global curscreen,points
    if user_text!="":
        sqlconn.update(user_text,points)
    curscreen="menu"
    obstacles.restart(SCREEN)
    points=0
    Cat.y=Ground.y+1

def lose():
    SCREEN.fill((191,255,128))
    lose=BASE_FONT.render("YOU LOSE",False,(0,0,0))
    SCREEN.blit(lose,(WIDTH/2,HEIGHT/2))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            pdb.set_trace()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RETURN:
                restart()


def start():
    clock.tick(FPS)
    while True:
        match curscreen:
            case "game":
                game()
            case "lose":
                lose()
            case "menu":
                menu()


if __name__=="__main__":
    start()

