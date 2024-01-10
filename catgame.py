import pygame,os,pdb,sys
import sprites,obstacles,sqlconn

pygame.init()
WIDTH=400
HEIGHT=300
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Catgame")
FPS=60
curscreen="menu"

points=0
pointsinterval=250  #time interval to update points in milliseconds
lastpointinterval=0
downclickinterval=0

hitbox=True
downclicked=False

Ground=pygame.Rect(0,HEIGHT-sprites.GROUNDHEIGHT,sprites.GROUNDWIDTH,sprites.GROUNDHEIGHT)
skyx=0
bushx=0
obstaclearray=[]

#=======================MENU===============================
BASE_FONT = pygame.font.Font(None, 32) 
user_text = '' 
INPUT_RECT = pygame.Rect(20, 80, 140, 32) 
#=========================================================



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

def pyquit():
    pygame.quit()
    pdb.set_trace()
    quit()

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

def rectbelow():
    global catstate,catgravity
    for rect in obstacles.standablerect:
        if pygame.Rect.colliderect(Cat,rect) and catgravity>0:
            catgravity=0
            catstate="run"

def collisioncheck():
    global curscreen,catgravity
    if (pygame.Rect.collidelistall(Cat,obstacles.objrectlist))!=[]:
        curscreen="lose"
    if not downclicked:
        rectbelow()

def drawgame():
    global skyx,bushx
    SCREEN.blit(sprites.SKYSPRITE,(skyx,0))
    SCREEN.blit(sprites.SKYSPRITE,(skyx+sprites.SKYWIDTH,0))
    if skyx<-sprites.SKYWIDTH:
        skyx=0
    else: skyx-=obstacles.speed4
    SCREEN.blit(sprites.BUSHSPRITE,(bushx,Ground.x-sprites.GROUNDHEIGHT))
    SCREEN.blit(sprites.BUSHSPRITE,(bushx+sprites.BUSHWIDTH,Ground.x-sprites.GROUNDHEIGHT))
    if bushx<-sprites.SKYWIDTH:
        bushx=0
    else: bushx-=obstacles.speed3
    SCREEN.blit(sprites.GROUNDSPRITE,(Ground.x,Ground.y))
    obstacles.update(SCREEN)
    if hitbox==True:
        SCREEN.fill("green",Cat)
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
    global catgravity,catstate,curscreen,points,lastpointinterval,downclicked,downclickinterval
    timer=pygame.time.get_ticks()
    clock.tick(FPS)
    drawgame()
    for event in pygame.event.get():  
        if event.type==pygame.KEYDOWN:
            if (event.key==pygame.K_SPACE or event.key==pygame.K_UP) and catstate!="jump":
                catgravity= -9
                catstate="jump"
            if event.key==pygame.K_DOWN and not downclicked:
                catgravity+=3
                downclickinterval=timer
                downclicked=True
        if event.type == pygame.QUIT:
            pyquit()
    
    if downclicked:
        if timer-downclickinterval>250:
            downclicked=False
    

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
            pyquit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:  
                user_text = user_text[:-1] 
            elif event.key==pygame.K_RETURN:
                curscreen="game"
            elif event.key==pygame.K_SPACE:
                hitbox=not hitbox
                obstacles.hitbox=hitbox
            elif event.key==pygame.K_DELETE:
                pass
            elif event.key==pygame.K_TAB:
                pass
            elif len(user_text)<10: 
                user_text += event.unicode

    SCREEN.blit(sprites.MENUSPRITE,(0,0)) 
    text_surface = BASE_FONT.render(user_text, False, (78,105,111)) 
    SCREEN.blit(text_surface, (INPUT_RECT.x+5, INPUT_RECT.y+5)) 
    INPUT_RECT.w = max(100, text_surface.get_width()+10) 
    pygame.display.flip() 

def restart():
    global curscreen,points
    curscreen="menu"
    obstacles.restart(SCREEN)
    points=0
    Cat.y=Ground.y+1

def lose():
    global curscreen
    if user_text!="":
        sqlconn.update(user_text,points)
    SCREEN.blit(sprites.LOSESPRITE,(-20,-50))
    enter=BASE_FONT.render("[ENTER]: Retry",False,(255,255,255))
    space=BASE_FONT.render("[SPACE]: Leaderboard",False,(255,255,255))
    lose=BASE_FONT.render("YOU LOSE",False,(255,255,255))
    total=BASE_FONT.render("TOTAL: "+str(points),False,(255,255,255))
    SCREEN.blit(lose,(WIDTH/4-60,10))
    SCREEN.blit(total,(WIDTH/4-50,50))
    SCREEN.blit(enter,(WIDTH/4-80,80))
    SCREEN.blit(space,(WIDTH/4-80,110))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pyquit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                sqlconn.recieve()
                curscreen="leaderboard"
            if event.key==pygame.K_RETURN:
                restart()


def leaderboard():
    clock.tick(FPS)
    onetext=BASE_FONT.render((sqlconn.output[0][0]),False,(78,105,111))
    twotext=BASE_FONT.render((sqlconn.output[1][0]),False,(78,105,111))
    threetext=BASE_FONT.render((sqlconn.output[2][0]),False,(78,105,111))
    onescore=BASE_FONT.render(str(sqlconn.output[0][1]),False,(78,105,111))
    twoscore=BASE_FONT.render(str(sqlconn.output[1][1]),False,(78,105,111))
    threescore=BASE_FONT.render(str(sqlconn.output[2][1]),False,(78,105,111))
    SCREEN.blit(sprites.LEADERBOARDSPRITE,(0,0))
    SCREEN.blit(onetext,(125,85))
    SCREEN.blit(twotext,(125,165))
    SCREEN.blit(threetext,(125,245))
    SCREEN.blit(onescore,(275,85))
    SCREEN.blit(twoscore,(275,165))
    SCREEN.blit(threescore,(275,245))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pyquit()
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
            case "leaderboard":
                leaderboard()

if __name__=="__main__":
    start()