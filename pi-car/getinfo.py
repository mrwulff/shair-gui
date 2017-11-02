
import pygame
import socket
from string import *
import random
import datetime
import time
import obd



UDP_IP = "127.0.0.1"
#UDP_IP = "192.168.0.112"
#UDP_IP="192.168.0.112"
UDP_PORT =5555

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP


songd='song'
artistd='artist'
albumd='album'


while True:
    
    data, addr = sock.recvfrom(1024)



  


    if "coreminm" in data:

        songd= data
        junk,songd=split(songd,'coreminm')
    if "coreasar" in data:
        artistd=data
        junk,artistd=split(artistd,"coreasar")

    if "coreasal" in data:

        albumd=data
        junk,albumd=split(albumd,"coreasal")

    print songd,artistd,albumd
  
   
    #pygame.display.flip()
    #clock2.tick(60)

