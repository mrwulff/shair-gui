# coding=utf-8
from time import sleep
from rpi_TM1638 import TMBoards
#import pygame
#import math
import random


DIO = 17
CLK = 27
STB = 22,23

TM = TMBoards(DIO, CLK, STB, 0)

i=0
while 1==1:

    a=random.randint(0,99999999)
    b=random.randint(0,99999999)
    
    mode=['OilTEMP','RPM',"  SPEED",'INTAKE',"Throttle"]
    
    TM.clearDisplay()

    a= i%len(mode)
    print a
    TM.segments[0] = str(mode[a] )      # display '0' on the display 1 (2nd 7-segment display of the 1st board)


    TM.segments[8] = str(b)

    aa=raw_input('CLICK')

    i=i+1
