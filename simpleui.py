import pygame
import socket
from string import *


UDP_IP = "127.0.0.1"
UDP_PORT =5555

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))



pygame.init()
#screen = pygame.display.set_mode((640, 480),pygame.FULLSCREEN)
screen = pygame.display.set_mode((640, 480))


clock = pygame.time.Clock()
done = False

font = pygame.font.SysFont("comicsansms", 72)

songd='song'
artistd='artist'
albumd='album'
coreasal
while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
            quit()
    screen.fill((0,0,0))
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    if "coreminm" in data:
        
        songd= data
        junk,songd=split(songd,'coreminm')
    if "coreasar" in data:
        artistd=data
        junk,artistd=split(artistd,"coreasar")
        
    if "coreasal" in data:
        
        albumd=data
        junk,albumd=split(albumd,"coreasal")

        
    text = font.render(songd, True, (0, 128, 0))
    #screen.fill((255, 255, 255))
    screen.blit(text,(320 - text.get_width() // 2, 50))

    text2 = font.render(artistd, True, (0, 128, 0))
    #screen.fill((255, 255, 255))
    screen.blit(text2,(320 - text2.get_width() // 2, 150))

    text3 = font.render(albumd, True, (0, 128, 0))
    #screen.fill((255, 255, 255))
    screen.blit(text3,(320 - text3.get_width() // 2, 250))
    
    pygame.display.flip()
    clock.tick(60)







