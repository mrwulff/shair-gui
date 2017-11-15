import pygame
import socket
from string import *
import random
import datetime
import time
import obd

connection = obd.OBD() # auto-connects to USB or RF port

cmd = obd.commands.AMBIANT_AIR_TEMP # select an OBD command (sensor)

response = connection.query(cmd) # send the command, and parse the response

print(response.value) # returns unit-bearing values thanks to Pint
#print(response.value.to("mph")) # user-friendly unit conversions

pygame.init()
#screen = pygame.display.set_mode((640, 480),pygame.FULLSCREEN)
#screen = pygame.display.set_mode((640, 480))
screen = pygame.display.set_mode((720,480))


clock = pygame.time.Clock()
done = False

font = pygame.font.SysFont("44", 72)

songd='song'
artistd='artist'
albumd='album'



while not done:
    cmd = obd.commands.AMBIANT_AIR_TEMP # select an OBD command (sensor)

    response = connection.query(cmd) # send the command, and parse the response

    temp=(response.value) # returns unit-bearing values thanks to Pint
    temp=str(temp)
    if temp=="None":
        #print 'NONEONEONEONEONEONEON'
        temp=str(random.randint(1,80))  
    

    
    


    cmd = obd.commands.SPEED # select an OBD command (sensor)

    response = connection.query(cmd) # send the command, and parse the response

    speed=(response.value) # returns unit-bearing values thanks to Pint
    speeds=str(speed)

    if speeds=="None":
        speeds=str(random.randint(1,80))




    cmd = obd.commands.RPM # select an OBD command (sensor)

    response = connection.query(cmd) # send the command, and parse the response

    rpm=(response.value) # returns unit-bearing values thanks to Pint
    
    rpms=str(rpm)
    print rpms
    if rpms=="None":
        rpms=str(random.randint(1000,6000))







    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            screen.close()
            quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
            pygame.quit()
            quit()
    #screen.fill((0,0,0))




    bg = pygame.image.load('image/bgb.png')
    screen.blit(bg, (00, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
            quit()
    #screen.fill((0,0,0))
 #   data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes




    rpmt = font.render(rpms, True, (255, 255, 0))
    screen.blit(rpmt,(475,310))
    



    tempt = font.render(temp, True, (255, 228, 0))
    screen.blit(tempt,(120,400))



    speedt = font.render(speeds, True, (255, 128, 100))
    screen.blit(speedt,(120, 320))


    clockd=time.strftime("%I:%M %p")
    clockt = font.render(clockd, True, (0, 255, 255))
    screen.blit(clockt,(475,400))



    songt = font.render(songd, True, (255, 228, 0))
    screen.blit(songt,(188,60))



    albumt = font.render(albumd, True, (255, 228, 0))
    screen.blit(albumt,(188,150))


    artistt = font.render(artistd, True, (255, 228, 0))
    screen.blit(artistt,(188,230))












   
    pygame.display.flip()
    clock.tick(10)
