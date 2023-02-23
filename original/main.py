#import the pygame library 
import pygame 
import random

#anchor the pygame screen so you see it in codio.
#Click on the arrow in the upper left corner to display in a new browser tab.
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0)
#start the pygame module 
pygame.init() 
#variables for screen size: 
screen_width=1250
screen_height=600 

#color code constants 
GREEN = (0, 255, 0)
#other variable initializers (fonts, text, images, etc)
startscreen=False
font1 = pygame.font.SysFont("comicsansms", 100)
Title = font1.render("Five Nights at Freddy's", True, (255, 255, 255))
Info = font1.render("Press Space To play", True, (255, 255, 255))
foxymoves = 0
Map = pygame.image.load('New Piskel (1).png')
Map = pygame.transform.scale(Map,(400,300))
Mapusage = False
x=-400
y=0
You = pygame.image.load('You.png')
You = pygame.transform.scale(You,(30,30))
#open map variables
openMap = pygame.image.load('New Piskel (2).png')
x2=0
y2=0
#Foxy variables and ai
foxy = pygame.image.load('New Piskel (3).png')
foxy = pygame.transform.scale(foxy,(20,20))
foxyy=10
foxyx=50
foxyattacks=False
foxywins = False
foxyjumpscare = pygame.image.load('New Piskel (7).png')
foxyjumpscare = pygame.transform.scale(foxyjumpscare,(200,200))
foxycounterjs = 0
#door variables
#print
rightdooropen=False
leftdooropen=False
font = pygame.font.SysFont("comicsansms", 50)
rightdoor = font.render("The right door is closed", True, (255, 255, 255))
leftdoor = font.render("The left door is closed", True, (255, 255, 255))
#other variables
l=0
frames=0
jumpscaretimer = 0
timecounter = 0
counter=0
counter1=0
gameoverfont = pygame.font.SysFont("comicsansms", 100)
gameover1=False
gameoverdisplay = gameoverfont.render("Game Over", True, (255, 0, 0))
clock2 = font.render("12:00 AM", True, (255, 255, 255))
winfont = pygame.font.SysFont("comicsansms", 100)
win=False
windisplay = winfont.render("6:00 AM", True, (255, 255, 255))
#Freddy variables and ai
freddy = pygame.image.load('New Piskel (6).png')
freddy = pygame.transform.scale(freddy,(20,20))
freddyy=10
freddyx=160
freddyheight=100
freddywidth=100
freddycounter = 0
freddymoves = 0
freddyplacing = 0
freddywins = False
batterypercent = "100%"
freddyjumpscare = pygame.image.load('New Piskel (9).png')
freddyjumpscare = pygame.transform.scale(freddyjumpscare,(freddywidth,freddyheight))
# bonnie variables and ai
bonnie = pygame.image.load('New Piskel (5).png')
office = pygame.image.load('ooffice.png')
office = pygame.transform.scale(office,(1000,500))
bonnie = pygame.transform.scale(bonnie,(20,20))
bonniey=10
bonniex=190
bonniecounter = 0
bonniewins = False
bonniemoves = 0
bonnieplacing = 0
bonniejumpscare = pygame.image.load('New Piskel (8).png')
batterydisplay = gameoverfont.render("100%", True, (255, 255, 255))
#chica variables
chica = pygame.image.load('New Piskel (4).png')
chica = pygame.transform.scale(chica,(20,20))
chicay=10
chicax=250
chicacounter = 0
chicamoves = 0
chicawins = False
chicaplacing = 0
chicajumpscare = pygame.image.load('New Piskel (11).png')
#battery functions
Batterypertick = 100
batterypercent = 100
batterypercent = str(batterypercent)
batterydisplay = gameoverfont.render(batterypercent, True, (255, 255, 255))
def battery(batterypercent,batterydisplay,freddywins):
  """this function will use an integer and decrease the value and put it in a string to put into a display statement and print it"""
  batterypercent=int(batterypercent)
  batterypercent-=1
  batterypercent=str(batterypercent)
  batterydisplay = gameoverfont.render(batterypercent, True, (255, 255, 255))
  screen.blit(batterydisplay,(600, 100))
  Batterypertick=100
  batterypercent=int(batterypercent)
  if batterypercent<=0:
    freddywins = True
  batterypercent=str(batterypercent)
  return(batterypercent,Batterypertick,batterydisplay,freddywins)
def Mapinuse(freddyx,freddyy,freddy,foxyx,foxyy,foxy,bonniex,bonniey,bonnie,chicax,chicay,chica,openMap,Map,clock2,x2,y2,x,y):
    """this function is used to display where the animatronics are"""
    x=35
    screen.blit(Map, (x,y))
    screen.blit(openMap, (x2, y2))
    screen.blit(clock2,(600, 0))
    screen.blit(freddy, (freddyx, freddyy))
    screen.blit(bonnie, (bonniex, bonniey))
    screen.blit(chica, (chicax, chicay))
    screen.blit(foxy, (foxyx, foxyy))
    screen.blit(You, (250,250))
def animatronicmovement(moving,counter,placing,x_,y_,sprite,wins,x1,x2,x3,y1,y2,y3,rightdoor,placementy,placementx,gameover,jumpscaretimer,animatronic):
  """This function is to move bonnie and chica around the map with their coordinates and cause jumpscares"""
  if moving >= 20:
    placing = placing + 1
    moving = 0
  if placing == 0:
    placementy=y_
    placementx=x_
  if placing == 1:
    placementy=y1
    placementx=x1
  if placing==2:
    placementy=y2
    placementx=x2
  if placing==3:
    placementy=y3
    placementx=x3
  if placing == 4:
    if rightdooropen == True:
      placing = 0
    if rightdooropen == False:
      wins = True
      if wins==True:
        screen.fill((50,0,0))
        screen.blit(animatronic, (500, 250))
        jumpscaretimer = jumpscaretimer + 1
        if jumpscaretimer >= 100:
          wins = False
          gameover = True
  bonniewins=str(wins)
  return(wins,moving,counter,placementx,placementy,placing,gameover,jumpscaretimer)
#create a screen with dimensions 
screen = pygame.display.set_mode((screen_width, screen_height)) 
#set the screen caption 
pygame.display.set_caption("Fnaf in Pygame") 
#the clock will be used to regulate the frame rate 
clock = pygame.time.Clock() 
#This function call updates the screen 
pygame.display.update() 

  #sets the frame rate
clock.tick(60) 
  #variable to control the game loop 
keep_playing=True 

#Game Loop - needed to keep updating and redrawing the screen 
while keep_playing==True:
  screen.fill((0, 0, 0))
  pressed = pygame.key.get_pressed()
  if startscreen!=True:
    screen.blit(Title,(50, 0))
    screen.blit(Info,(50, 200))
    if pressed[pygame.K_SPACE]:
      gocounter=0
      batterypercent=100
      batterypercent=str(batterypercent)
      Batterypertick=100
      startscreen=True
      gameover1=False
      foxywins=False
      freddywins = False
      bonniewins = False
      chicawins=False
      foxyattacks = False
      foxymoves = 0
      freddyattacks = False
      freddymoves = 0
      freddycounter = 0
      bonnieattacks = False
      bonniemoves = 0
      bonniecounter = 0
      chicaattacks = False
      chicamoves = 0
      chicacounter = 0
      chicaplacing = 0
      freddyplacing = 0
      bonnieplacing = 0
      timecounter = 0
      counter1 = 0
      chicacounter = 0
      freddycounter = 0
      bonniecounter = 0
      batterydisplay = gameoverfont.render(batterypercent, True, (255, 255, 255))
      foxycounterjs = 0
  #iterates over the current list of events(checks for events)  
  for event in pygame.event.get(): 
    #will stop the game loop if escape is pressed 
    if event.type == pygame.QUIT: 
      keep_playing = False
        
  #all items drawn to the screen go her
  if startscreen==True:
    if gameover1!=True and foxywins!=True and freddywins!=True and bonniewins!=True and chicawins!=True and timecounter<21600:
      #doors opening/closing
      screen.blit(office, (0,0))
      batteryuse=[False,False,False]
      if leftdooropen==True:
        batteryuse[0] = True
      if rightdooropen==True:
        batteryuse[1]=True
      if Mapusage ==True:
        batteryuse[-1]= True
      batteryusage = batteryuse.count(True)
      Batterypertick-=batteryusage
      screen.blit(batterydisplay,(600, 100))
      if Batterypertick<=0:
        f=battery(batterypercent,batterydisplay,freddywins)
        batterypercent=f[0]
        batterydisplay=f[2]
        Batterypertick=f[1]
        freddywins=f[3]
      screen.blit(clock2,(600, 0))
      timecounter= timecounter + 1 
      counter1=counter1+1
      freddycounter = freddycounter + 1
      bonniecounter = bonniecounter + 1
      chicacounter = chicacounter + 1
      while counter1>=1200:
        foxymoves=random.randint(0,25)
        counter1=0
      while freddycounter>=1200:
        freddymoves=random.randint(0,25)
        freddycounter=0
      while bonniecounter>=1200:
        bonniemoves=random.randint(0,25)
        bonniecounter=0
      while chicacounter>=1200:
        chicamoves=random.randint(0,25)
        chicacounter=0
      if pressed[pygame.K_w]:
        Mapinuse(freddyx,freddyy,freddy,foxyx,foxyy,foxy,bonniex,bonniey,bonnie,chicax,chicay,chica,openMap,Map,clock2,x2,y2,x,y)
        Mapusage =True
      elif not pressed[pygame.K_w]:
        x=-400
        screen.blit(Map, (x,y))
        screen.blit(clock2,(600, 0))
        screen.blit(openMap, (x2, y2))
        Mapusage = False
      if pressed[pygame.K_d]:
      
        screen.blit(rightdoor,(575,450 ))
        screen.blit(openMap, (x2, y2))
        rightdooropen = True
        screen.blit(clock2,(600, 0))
        Mapusage = False
      if pressed[pygame.K_a]:
      
        screen.blit(leftdoor,(0,450 ))
        screen.blit(openMap, (x2, y2))
        leftdooropen = True
        screen.blit(clock2,(600, 0))
      if not pressed[pygame.K_a]:
        leftdooropen = False
      if not pressed[pygame.K_d]:
        rightdooropen = False

      if pressed[pygame.K_a] and pressed[pygame.K_d]:
      
        screen.blit(leftdoor,(0,450 ))
        screen.blit(openMap, (x2, y2))
        screen.blit(rightdoor,(575,450 ))
        leftdooropen = True
        rightdooropen = True
        screen.blit(clock2,(600, 0))

      if pressed[pygame.K_a] and pressed[pygame.K_w]:
        leftdooropen = True
        Mapusage =True
      
        Mapinuse(freddyx,freddyy,freddy,foxyx,foxyy,foxy,bonniex,bonniey,bonnie,chicax,chicay,chica,openMap,Map,clock2,x2,y2,x,y)
        screen.blit(leftdoor,(0,450 ))
      if pressed[pygame.K_d] and pressed[pygame.K_w]:
        rightdooropen = True
        Mapusage =True
      
        Mapinuse(freddyx,freddyy,freddy,foxyx,foxyy,foxy,bonniex,bonniey,bonnie,chicax,chicay,chica,openMap,Map,clock2,x2,y2,x,y)
        screen.blit(rightdoor,(575,450 ))

      if pressed[pygame.K_d] and pressed[pygame.K_w] and pressed[pygame.K_a] :
        rightdooropen = True
        leftdooropen = True
        Mapusage =True
        screen.blit(rightdoor,(575,450 ))
        screen.blit(leftdoor,(0,450 ))
        x=35
        Mapinuse(freddyx,freddyy,freddy,foxyx,foxyy,foxy,bonniex,bonniey,bonnie,chicax,chicay,chica,openMap,Map,clock2,x2,y2,x,y)
      if foxymoves>=24:
        foxyattacks=True
      if foxyattacks==True:
        counter=counter+1
        foxy = pygame.image.load('New Piskel.png')
        if counter>=120:
          if leftdooropen==True:
            foxycounterjs = foxycounterjs + 1
            if foxycounterjs >= 60 and leftdooropen== True:
              foxyattacks=False
              foxy = pygame.image.load('New Piskel (3).png')
              foxycounterjs=0
          if leftdooropen==False and foxyattacks==True:
              foxywins = True
              foxycounterjs = 0
              foxymoves = 0
      if foxyattacks!=True:
        foxy = pygame.image.load('New Piskel (3).png')
      if freddymoves >= 24:
        freddyplacing = freddyplacing + 1
        freddymoves = 0
      if freddyplacing == 0:
          freddyy=10
          freddyx=160
      if freddyplacing == 1:
          freddyy=100
          freddyx=110
      if freddyplacing==2:
          freddyy=120
          freddyx=50
      if freddyplacing==3:
          freddyy=200
          freddyx=110
      if freddyplacing == 4:
          freddyy=225
          freddyx=175
      if freddyplacing == 5:
          if leftdooropen == True:
            freddyplacing = 0
          if leftdooropen == False:
            freddywins = True
    l=animatronicmovement(bonniemoves,bonniecounter,bonnieplacing,190,10,bonniejumpscare,bonniewins,300,300,335,10,150,225,rightdoor,bonniey,bonniex,gameover1,jumpscaretimer,bonniejumpscare)
    bonniewins=l[0]
    bonniemoves=l[1]
    bonniecounter=l[2]
    bonniex=l[3]
    bonniey= l[4]
    bonnieplacing =l[5]
    gameover1=l[6]
    jumpscaretimer=l[7]
    k=animatronicmovement(chicamoves,chicacounter,chicaplacing,220,10,chicajumpscare,chicawins,330,330,335,10,150,275,rightdoor,chicay,chicax,gameover1,jumpscaretimer,chicajumpscare)
    chicawins=k[0]
    chicamoves=k[1]
    chicacounter=k[2]
    chicax=k[3]
    chicay=k[4]
    chicaplacing=k[5]
    gameover1=k[6]
    jumpscaretimer=k[7]
    if timecounter <= 3600:
      clock2 = font.render("12:00 AM", True, (255, 255, 255))
    if timecounter >= 3600:
      clock2 = font.render("1:00 AM", True, (255, 255, 255))
    if timecounter >= 7200:
      clock2 = font.render("2:00 AM", True, (255, 255, 255))
    if timecounter >= 10800:
      clock2 = font.render("3:00 AM", True, (255, 255, 255))
    if timecounter >= 14400:
      clock2 = font.render("4:00 AM", True, (255, 255, 255))
    if timecounter >= 18000:
      clock2 = font.render("5:00 AM", True, (255, 255, 255))
    if foxywins==True:
        screen.fill((0,0,0))
        screen.blit(foxyjumpscare, (500, 250))
        jumpscaretimer = jumpscaretimer + 1
        if jumpscaretimer >= 100:
          foxywins= False
          gameover1 = True
          jumpscaretimer = 0
          foxywins=False
          foxymoves=0
    if freddywins==True:
      screen.fill((0,0,0))
      freddyjumpscare = pygame.transform.scale(freddyjumpscare,(freddywidth,freddyheight))
      screen.blit(office, (1000, 500))

      if frames<=30:
        screen.blit(freddyjumpscare, (100, 100))
        freddywidth+=10
        freddyheight+=10
        frames+=1
      jumpscaretimer = jumpscaretimer + 1
      if jumpscaretimer >= 60:
        freddywins = False
        gameover1 = True
    if gameover1==True :
      screen.fill((0,0,0))
      screen.blit(gameoverdisplay,(300,200 ))
      gocounter+=1
      if gocounter>=600:
        startscreen=False
    if timecounter >= 21600:
      screen.fill((0,0,0))
      screen.blit(windisplay,(300,200))
      startscreen=False
  #This function call updates the screen 
  pygame.display.update() 
  #sets the frame rate
  clock.tick(60) 