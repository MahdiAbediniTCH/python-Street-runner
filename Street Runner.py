import pygame
from time import time,sleep
from random import choice
import os
pygame.init()
pygame.mixer.init()
#variables
window=pygame.display.set_mode((600,750))
orange=(255,140,0)
yellow=(255,192,0)
aqua=(0,192,255)
grey=(125,125,125)
playedagain=False
pygame.font.init()
#sounds
sound1=pygame.mixer.Sound('sounds\\gameover.wav')
sound2=pygame.mixer.Sound('sounds\\obstacle_pass.wav')
sound3=pygame.mixer.Sound('sounds\\start_sound.wav')
sound4=pygame.mixer.Sound('sounds\\highscore_sound.flac')
music=pygame.mixer.Sound('sounds\\music.wav')
sound2.set_volume(0.4)
sound1.set_volume(0.2)
sound4.set_volume(0.6)
music.set_volume(0.8)
pygame.mixer.music.load('c.wma')
pygame.mixer.music.play(loops=1000)
pygame.mixer.music.set_volume(0.17)
pygame.display.set_caption("Street runner")
#functions
def draw_obstacle(x,y):
    pygame.draw.circle(window,orange,(x,y),35)
    pygame.draw.circle(window,(255,255,255),(x,y),30,9)
    pygame.draw.circle(window,(255,255,255),(x,y),15,7)
def draw_circle(x):
    pygame.draw.circle(window,aqua,(x,670),40)
    pygame.draw.circle(window,(255,255,255),(x-15,653),8)
    pygame.draw.circle(window,(255,255,255),(x+15,653),8)
    pygame.draw.circle(window,(0,0,0),(x-15,651),4)
    pygame.draw.circle(window,(0,0,0),(x+15,651),4)
#fonts
myfont=pygame.font.SysFont('Comic Sans MS',40)
myfont2=pygame.font.SysFont('Comic Sans MS',50,True)
myfont3=pygame.font.SysFont('Comic Sans MS',30,True)
myfont4=pygame.font.SysFont('Comic Sans MS',30)
myfont5=pygame.font.SysFont('Comic Sans MS',25)
text1=myfont.render('Press enter to start',True,(255,255,255))
#highscore file
if os.path.exists('HIGHSCORE.txt'):
    file=open('HIGHSCORE.txt','r+')
else:
    file=open('HIGHSCORE.txt','w')
    file.write('0')
    file.close()
    file=open('HIGHSCORE.txt','r+')
#mainloop
while True:
    '''pygame.mixer.music.pause()
    pygame.mixer.music.play()'''
    #highscore file
    try :
        file.seek(0)
        highscore=int(file.read())
    except:
        file.seek(0)
        file.write('0')
        file.seek(0)
        highscore=int(file.read())
    #variables
    window.fill((0,0,0))
    NHcounter=0
    nhshown=False
    started=False
    circlexpos=300
    done=False
    #start scene
    while not started:
        window.blit(text1,(120,300))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                file.close()
                pygame.quit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    started=True
                    #sound
                    sound3.play()
        pygame.display.update()
    #variables
    obsypos1=-35
    obsxpos1=choice([300,220,380])
    obsypos2=-296
    obsxpos2=choice([300,220,380])
    obsypos3=-557
    obsxpos3=choice([300,220,380])
    obsypos4=-818
    obsxpos4=choice([300,220,380])
    lineypos1=682.5
    lineypos2=495
    lineypos3=307.5
    lineypos4=120
    lineypos5=-67.5
    score=0
    ticker=100
    lmnp=True
    s4np=True
    #innerloop
    while not done:
        pygame.mixer.music.set_volume(0.4)
        #additions
        lineypos1+=4
        lineypos2+=4
        lineypos3+=4
        lineypos4+=4
        lineypos5+=4
        obsypos1+=4
        obsypos2+=4
        obsypos3+=4
        obsypos4+=4
        #draws
        window.fill(grey)
        ###
        pygame.draw.rect(window,yellow,((0,0),(175,750)))
        pygame.draw.rect(window,yellow,((425,0),(600,750)))
        ###
        pygame.draw.polygon(window,(255,255,255),((285,lineypos1),(315,lineypos1),(315,lineypos1-120),(285,lineypos1-120),(285,lineypos1)))
        pygame.draw.polygon(window,(255,255,255),((285,lineypos2),(315,lineypos2),(315,lineypos2-120),(285,lineypos2-120),(285,lineypos2)))
        pygame.draw.polygon(window,(255,255,255),((285,lineypos3),(315,lineypos3),(315,lineypos3-120),(285,lineypos3-120),(285,lineypos3)))
        pygame.draw.polygon(window,(255,255,255),((285,lineypos4),(315,lineypos4),(315,lineypos4-120),(285,lineypos4-120),(285,lineypos4)))
        pygame.draw.polygon(window,(255,255,255),((285,lineypos5),(315,lineypos5),(315,lineypos5-120),(285,lineypos5-120),(285,lineypos5)))
        ###
        draw_circle(circlexpos)
        ###
        draw_obstacle(obsxpos1,obsypos1)
        draw_obstacle(obsxpos2,obsypos2)
        draw_obstacle(obsxpos3,obsypos3)
        draw_obstacle(obsxpos4,obsypos4)
        #change the place of shapes when they passed borders
        if lineypos1-120>=750:
            lineypos1=-67.5
        if lineypos2-120>=750:
            lineypos2=-67.5
        if lineypos3-120>=750:
            lineypos3=-67.5
        if lineypos4-120>=750:
            lineypos4=-67.5
        if lineypos5-120>=750:
            lineypos5=-67.5
        ###
        if obsypos1>=785:
            obsypos1=-296
            obsxpos1=choice([300,220,380])
            score+=5
            #sound
            sound2.play()
            #speed improvement
            if ticker<1300:
                ticker+=10
        if obsypos2>=785:
            obsypos2=-296
            obsxpos2=choice([300,220,380])
            score+=5
            #sound
            sound2.play()
        if obsypos3>=785:
            obsypos3=-296
            obsxpos3=choice([300,220,380])
            score+=5
            #sound
            sound2.play()
        if obsypos4>=785:
            obsypos4=-296
            obsxpos4=choice([300,220,380])
            score+=5
            #sound
            sound2.play()
        #eventloop
        for event in pygame.event.get():
            pcircx=circlexpos
            if event.type==pygame.QUIT:
                done=True
                file.close()
                pygame.quit()
            #key movements
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT and circlexpos+80<=380:
                    circlexpos+=80
                    #sound
                if event.key==pygame.K_LEFT and circlexpos-80>=220:
                    circlexpos-=80
                    #sound
        #when lost =>
        if (710>obsypos1>595 and circlexpos==obsxpos1) or (710>obsypos2>595 and circlexpos==obsxpos2) or (710>obsypos3>595 and circlexpos==obsxpos3) or (710>obsypos4>595 and circlexpos==obsxpos4):
            #sound
            #showing how died
            if 710>obsypos1>595:
                if pcircx==obsxpos1:
                    obsypos1+=5
                elif pcircx<obsxpos1:
                    pcircx+=15
                elif pcircx>obsxpos1:
                    pcircx-=15
            ###
            elif 710>obsypos2>595:
                if pcircx==obsxpos2:
                    obsypos2+=5
                elif pcircx<obsxpos2:
                    pcircx+=15
                elif pcircx>obsxpos2:
                    pcircx-=15
            ###
            elif 710>obsypos3>595:
                if pcircx==obsxpos3:
                    obsypos3+=5
                elif pcircx<obsxpos3:
                    pcircx+=15
                elif pcircx>obsxpos3:
                    pcircx-=15
            ###
            elif 710>obsypos4>595:
                if pcircx==obsxpos4:
                    obsypos4+=5
                elif pcircx<obsxpos4:
                    pcircx+=15
                elif pcircx>obsxpos4:
                    pcircx-=15
            #draws (for showing how died)
            window.fill(grey)
            ###
            pygame.draw.rect(window,yellow,((0,0),(175,750)))
            pygame.draw.rect(window,yellow,((425,0),(600,750)))
            ###
            pygame.draw.polygon(window,(255,255,255),((285,lineypos1),(315,lineypos1),(315,lineypos1-120),(285,lineypos1-120),(285,lineypos1)))
            pygame.draw.polygon(window,(255,255,255),((285,lineypos2),(315,lineypos2),(315,lineypos2-120),(285,lineypos2-120),(285,lineypos2)))
            pygame.draw.polygon(window,(255,255,255),((285,lineypos3),(315,lineypos3),(315,lineypos3-120),(285,lineypos3-120),(285,lineypos3)))
            pygame.draw.polygon(window,(255,255,255),((285,lineypos4),(315,lineypos4),(315,lineypos4-120),(285,lineypos4-120),(285,lineypos4)))
            pygame.draw.polygon(window,(255,255,255),((285,lineypos5),(315,lineypos5),(315,lineypos5-120),(285,lineypos5-120),(285,lineypos5)))
            ###
            draw_circle(pcircx)
            ###
            draw_obstacle(obsxpos1,obsypos1)
            draw_obstacle(obsxpos2,obsypos2)
            draw_obstacle(obsxpos3,obsypos3)
            draw_obstacle(obsxpos4,obsypos4)
            pygame.display.update()
            pygame.mixer.music.pause()
            sound1.play()
            sleep(1)
            #gameover window
            window.fill((0,0,0))
            text2=myfont2.render('Game over',True,(255,255,255))
            window.blit(text2,(185,250))
            #highscore check
            if score>highscore:
                text3= myfont.render('New Highscore! : '+str(int(score)),True,(255,255,255))
                window.blit(text3,(140,320))
                file.truncate(0)
                file.write(str(score))
            ###
            else:
                text4=myfont.render('\t Score : '+str(int(score))+' \t',True,(255,255,255))
                window.blit(text4,(180,320))
            text5=myfont3.render('Press R to play again',True,(255,255,0))
            text6=myfont3.render('Press Esc to quit',True,(255,0,0))
            window.blit(text5,(160,420))
            window.blit(text6,(190,460))
            pygame.display.update()
            #getting input(r or esc)
            no_input=True
            while no_input:
                if lmnp:
                    #music.play(loops=1000)
                    lmnp=False
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        music.stop()
                        sound1.play()
                        sleep(1)
                        file.close()
                        pygame.quit()
                        done=True
                    if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_r:
                            no_input=False
                            done=True
                            #sounds
                            sound3.play()
                            music.stop()
                            pygame.mixer.music.set_volume(0.17)
                            sleep(0.5)
                            pygame.mixer.music.play(loops=10000)
                            playedagain=True
                        elif event.key==pygame.K_ESCAPE:
                            music.stop()
                            sound1.play()
                            sleep(1)
                            file.close()
                            pygame.quit()
                            done=True
        else:
            #in-game texts
            text7=myfont4.render('Score : '+str(score),True,(255,255,255))
            if score>highscore:
                text8=myfont4.render('High : '+str(score),True,(255,255,255))
                if NHcounter<ticker*2 and nhshown==False:
                    #sound
                    if s4np:
                        sound4.play()
                        s4np=False
                    text9=myfont5.render('New Highscore!',True,(255,255,255))
                    window.blit(text9,(215,20))
                    NHcounter+=1
                if NHcounter>=ticker*2:
                    nhshown=True
            ###
            else:
                text8=myfont4.render('High : '+str(highscore),True,(255,255,255))
            window.blit(text8,(5,70))
            window.blit(text7,(5,20))
        #textfile seek
        file.seek(0)
        #controlling speed
        pygame.time.Clock().tick(ticker)
        #update
        pygame.display.update()

