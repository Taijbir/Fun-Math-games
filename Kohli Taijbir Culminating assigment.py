import pygame
pygame.init()
#Fonts Used
myfont= pygame.font.SysFont("exo_font.zip", 50)
myfontAns= pygame.font.SysFont("exo_font.zip", 35)
myfontIns= pygame.font.SysFont("exo_font.zip", 30)
win = pygame.display.set_mode((800,600))
pygame.display.set_caption("Kohli Taijbir Culminating assigment game1 level 1")
#Variables
clock = pygame.time.Clock()
display_width = 800
display_height = 600
#Colors
white=(255,255,255)
black = (0,0,0)
red= (200,0,0)
green=(0,200,0)
bright_red =(255,0,0)
bright_green= (0,255,0)
blue = (135, 206, 235)
bright_blue=(0,0,255)

#music
music = pygame.mixer.music.load('Kahoot Lobby Music.ogg')
pygame.mixer.music.play(loops=-1)

#images in The Fraction Game
twoFifths = pygame.image.load('2-5.png')
oneThrids = pygame.image.load('1-3.png')
threeFourths = pygame.image.load('3-4.png')
oneSixths = pygame.image.load('1-6.png')
twoSevens = pygame.image.load('2-7.png')
threeFifths = pygame.image.load('3-5.png')
fourteenFifteens = pygame.image.load('14-15.png')

plus = pygame.image.load('plus.png')
plusRe = pygame.transform.scale(plus, (50, 50))

equal = pygame.image.load('equal.png')
equalRe = pygame.transform.scale(equal, (50, 50))
#images in "What time is it?"
twoOclock =pygame.image.load('2Oclock.png')
twoORe = pygame.transform.scale(twoOclock, (100, 100))

threeOeight = pygame.image.load('3O8.png')
threeOeightRe = pygame.transform.scale(threeOeight, (100, 100))

threeOclock = pygame.image.load('3Oclock.png')
threeOclockRe = pygame.transform.scale(threeOclock, (100, 100))

midnight =  pygame.image.load('midnight.png')
midnightRe  =  pygame.transform.scale(midnight, (100, 100))

tenTen= pygame.image.load('10.10.png')
tenTenRe  =  pygame.transform.scale(tenTen, (150, 150))

sixOclock =  pygame.image.load('6.Oclock.jpg')
sixOclockRe  =  pygame.transform.scale(sixOclock, (150, 150))

twelveFifsix = pygame.image.load('12.56.png')
twelveFifsixRe  =  pygame.transform.scale(twelveFifsix, (100, 100))

nineOclock = pygame.image.load('nineOclock.png')
nineOclockRe  =  pygame.transform.scale(nineOclock, (100, 100))

eightFifeight = pygame.image.load('eightFifeight.png')
eightFifeightRe = pygame.transform.scale(eightFifeight, (100, 100))

elevelev = pygame.image.load('elev.elev.png')
elevelevtRe = pygame.transform.scale(elevelev, (100, 100))

sevThri = pygame.image.load('sevThri.png')
sevThritRe = pygame.transform.scale(sevThri, (100, 100))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
def Title_button(msg,x,y,w,h,ic,ac,action=None):
    mouse =pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(win,ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            if action == "play fraction":
                fractionLoop()
                intro = False
            elif action == "play time":
                timeLoop()
                intro = False
            elif action == "quit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(win,ic,(x,y,w,h))
    smallText= pygame.font.SysFont("exo_font.zip",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), y+(h/2))
    win.blit(textSurf, textRect)

def lev2button(msg,x,y,w,h,ic,ac,action=None):
    mouse =pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(win,ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            if action == "play fraction lev2":
                fractionLev2()
                intro = False
            elif action == "play time lev2":
                timeLooplev2()
                intro = False
            elif action == "quit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(win,ic,(x,y,w,h))
    smallText= pygame.font.SysFont("exo_font.zip",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), y+(h/2))
    win.blit(textSurf, textRect)
    
def ans_button(msg,x,y,w,h,ic,ac,action=None):
    mouse =pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(win,ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            if action == "Right":
                text_Right=myfont.render("Correct",1,(0,0,0))
                win.blit(text_Right,(380,500))
            elif action == "Wrong":
                text_Wrong=myfont.render("Wrong",1,(0,0,0))
                win.blit(text_Wrong,(380,500))
    else:
        pygame.draw.rect(win,ic,(x,y,w,h))
    smallText= pygame.font.SysFont("exo_font.zip",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), y+(h/2))
    win.blit(textSurf, textRect)

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        win.fill(blue)
        largeText = pygame.font.SysFont("exo_font.zip", 115)
        TextSurf, TextRect = text_objects("Fun Math Games", largeText)
        TextRect.center = ((800/2),(600/2))
        win.blit(TextSurf, TextRect)
        Title_button("Fraction Game",150,450,100,50,green,bright_green, "play fraction")
        Title_button("What Time is it?",350,450,100,50,green,bright_green, "play time")
        Title_button("QUIT",550,450,100,50,red,bright_red,"quit")
        pygame.display.update()
        clock.tick(15)
    
def fractionLoop():
    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        win.fill(white)
        win.blit(twoFifths, (30, 30))
        ans_button("2/5",108, 55, 40, 30,blue,bright_blue,"Right")
        ans_button("3/5",158, 55, 40, 30,blue,bright_blue,"Wrong")
        ans_button("5/2",208, 55, 40, 30,blue,bright_blue,"Wrong")
        win.blit(oneThrids, (30, 140))
        ans_button("1/3",158, 155, 40, 30,blue,bright_blue,"Right")
        ans_button("1/4",108, 155, 40, 30,blue,bright_blue,"Wrong")
        ans_button("3/2",208, 155, 40, 30,blue,bright_blue,"Wrong")
        win.blit(threeFourths, (30, 270))
        ans_button("3/4",208, 285, 40, 30,blue,bright_blue,"Right")
        ans_button("2/4",158, 285, 40, 30,blue,bright_blue,"Wrong")
        ans_button("3/5",108, 285, 40, 30,blue,bright_blue,"Wrong")
        win.blit(oneSixths, (30, 420))
        ans_button("1/6",208, 435, 40, 30,blue,bright_blue,"Right")
        ans_button("6/7",158, 435, 40, 30,blue,bright_blue,"Wrong")
        ans_button("2/12",108, 435, 40, 30,blue,bright_blue,"Wrong")
        win.blit(twoSevens, (440, 70))
        ans_button("2/7",520, 85, 40, 30,blue,bright_blue,"Right")
        ans_button("2/6",570, 85, 40, 30,blue,bright_blue,"Wrong")
        ans_button("7/12",620, 85, 40, 30,blue,bright_blue,"Wrong")
        win.blit(threeFifths, (440, 220))
        ans_button("3/5",570, 235, 40, 30,blue,bright_blue,"Right")
        ans_button("2/6",520, 235, 40, 30,blue,bright_blue,"Wrong")
        ans_button("7/12",620, 235, 40, 30,blue,bright_blue,"Wrong")
        win.blit(fourteenFifteens, (440, 370))
        ans_button("14/15",570, 385, 40, 30,blue,bright_blue,"Right")
        ans_button("15/16",520, 385, 40, 30,blue,bright_blue,"Wrong")
        ans_button("12/12",620, 385, 40, 30,blue,bright_blue,"Wrong")
        text_1=myfont.render("Fraction Game - Level 1",1,(0,0,0))
        win.blit(text_1,(230,10))
        text_subFrac=myfontAns.render("Choose the fraction which fits with the the photo",1,(0,0,0))
        win.blit(text_subFrac,(100,550))
        lev2button("Level 2",550,500,100,50,green,bright_green, "play fraction lev2")
        lev2button("QUIT",150,500,100,50,red,bright_red,"quit")
        pygame.display.update()
def timeLoop():
    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        win.fill(white)
        text_timeTitle=myfont.render("What Time is it? - Level 1",1,(0,0,0))
        win.blit(text_timeTitle,(230,10))
        text_subTime=myfontAns.render("Choose the time which corresponds with the photo.",1,(0,0,0))
        win.blit(text_subTime,(100,550))
        win.blit(twoORe, (30, 30))
        ans_button("2:00",135, 75, 40, 30,blue,bright_blue,"Right")
        ans_button("3:00",185, 75, 40, 30,blue,bright_blue,"Wrong")
        ans_button("1:00",235, 75, 40, 30,blue,bright_blue,"Wrong")
        win.blit(threeOeightRe, (30, 160))
        ans_button("3:08",235, 175, 40, 30,blue,bright_blue,"Right")
        ans_button("8:03",185, 175, 40, 30,blue,bright_blue,"Wrong")
        ans_button("8:30",135, 175, 40, 30,blue,bright_blue,"Wrong")
        win.blit(threeOclockRe, (30, 290))
        ans_button("3:00",235, 325, 40, 30,blue,bright_blue,"Right")
        ans_button("12:15",185, 325, 40, 30,blue,bright_blue,"Wrong")
        ans_button("3:15",135, 325, 40, 30,blue,bright_blue,"Wrong")
        win.blit(midnightRe, (30, 420))
        ans_button("12:00",235, 450, 40, 30,blue,bright_blue,"Right")
        ans_button("12:12",185, 450, 40, 30,blue,bright_blue,"Wrong")
        ans_button("1::00",135, 450, 40, 30,blue,bright_blue,"Wrong")
        win.blit(tenTenRe, (440, 70))
        ans_button("10:10",620, 100, 40, 30,blue,bright_blue,"Right")
        ans_button("2:10",570, 100, 40, 30,blue,bright_blue,"Wrong")
        ans_button("10:02",670, 100, 40, 30,blue,bright_blue,"Wrong")
        win.blit(sixOclockRe, (450, 220))
        ans_button("6:00",670, 250, 40, 30,blue,bright_blue,"Right")
        ans_button("12:06",570, 250, 40, 30,blue,bright_blue,"Wrong")
        ans_button("6:12",620, 250, 40, 30,blue,bright_blue,"Wrong")
        win.blit(twelveFifsixRe, (450, 370))
        ans_button("12:56",620, 400, 40, 30,blue,bright_blue,"Right")
        ans_button("11:00",670, 400, 40, 30,blue,bright_blue,"Wrong")
        ans_button("11:56",570, 400, 40, 30,blue,bright_blue,"Wrong")
        lev2button("Level 2",550,500,100,50,green,bright_green, "play time lev2")
        lev2button("QUIT",150,500,100,50,red,bright_red,"quit")
        pygame.display.update()
def fractionLev2():
    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        win.fill(white)
        text_1=myfont.render("Fraction Game - Level 2",1,(0,0,0))
        win.blit(text_1,(230,10))
        text_subFrac=myfontIns.render("Pick the fraction which fits with the the photo. Find the simplest answer",1,(0,0,0))
        win.blit(text_subFrac,(30,550))
        win.blit(oneThrids, (30, 50))
        win.blit(oneThrids, (170, 50))
        win.blit(plusRe, (115, 60))
        win.blit(equalRe, (270, 60))
        ans_button("2/3",340, 60, 50, 50,blue,bright_blue,"Right")
        ans_button("2/4",400, 60, 50, 50,blue,bright_blue,"Wrong")
        ans_button("3/4",460, 60, 50, 50,blue,bright_blue,"Wrong")
        win.blit(threeFourths, (30, 170))
        win.blit(threeFourths, (170, 170))
        win.blit(plusRe, (115, 180))
        win.blit(equalRe, (270, 180))
        ans_button("3/2",400, 180, 50, 50,blue,bright_blue,"Right")
        ans_button("2/3",340, 180, 50, 50,blue,bright_blue,"Wrong")
        ans_button("2/4",460, 180, 50, 50,blue,bright_blue,"Wrong")
        win.blit(oneSixths, (30, 290))
        win.blit(oneSixths, (170, 290))
        win.blit(plusRe, (115, 300))
        win.blit(equalRe, (270, 300))
        ans_button("1/3",460, 300, 50, 50,blue,bright_blue,"Right")
        ans_button("2/6",340, 300, 50, 50,blue,bright_blue,"Wrong")
        ans_button("2/3",400, 300, 50, 50,blue,bright_blue,"Wrong")
        win.blit(oneThrids, (30, 410))
        win.blit(oneSixths, (170, 410))
        win.blit(plusRe, (115, 420))
        win.blit(equalRe, (270, 420))
        ans_button("1/2",400, 420, 50, 50,blue,bright_blue,"Right")
        ans_button("3/6",340, 420, 50, 50,blue,bright_blue,"Wrong")
        ans_button("2/6",460, 420, 50, 50,blue,bright_blue,"Wrong")
        lev2button("QUIT",150,500,100,50,red,bright_red,"quit")
        pygame.display.update()
def timeLooplev2():
    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        win.fill(white)
        text_timeTitle=myfont.render("What Time is it? - Level 2",1,(0,0,0))
        win.blit(text_timeTitle,(230,10))
        text_subTime=myfontAns.render("Choose the time which corresponds with the photo.",1,(0,0,0))
        win.blit(text_subTime,(100,550))
        win.blit(nineOclockRe, (30, 30))
        ans_button("9:00",185, 75, 40, 30,blue,bright_blue,"Right")
        ans_button("4:00",135, 75, 40, 30,blue,bright_blue,"Wrong")
        ans_button("12:00",235, 75, 40, 30,blue,bright_blue,"Wrong")
        win.blit(eightFifeightRe, (30, 160))
        ans_button("8:58",235, 175, 40, 30,blue,bright_blue,"Right")
        ans_button("8:55",185, 175, 40, 30,blue,bright_blue,"Wrong")
        ans_button("11:40",135, 175, 40, 30,blue,bright_blue,"Wrong")
        win.blit(sevThritRe, (30, 290))
        ans_button("7:30",135, 325, 40, 30,blue,bright_blue,"Right")
        ans_button("6:35",185, 325, 40, 30,blue,bright_blue,"Wrong")
        ans_button("3:15",235, 325, 40, 30,blue,bright_blue,"Wrong")
        win.blit(elevelevtRe, (30, 420))
        ans_button("11:11",185, 450, 40, 30,blue,bright_blue,"Right")
        ans_button("12:12",135, 450, 40, 30,blue,bright_blue,"Wrong")
        ans_button("1::11",235, 450, 40, 30,blue,bright_blue,"Wrong")
        lev2button("QUIT",150,500,100,50,red,bright_red,"quit")
        pygame.display.update()
game_intro()
pygame.quit()
