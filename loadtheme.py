import plistlib
import biplist

import numpy

from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
        

from pygame.locals import *

import pgext
import os

from shutil import copyfile
import glob







###private/var/mobile/Library/SpringBoard






# Copyright 2011 Scrambled Code Studios
# Licensed under GPL v3

# Graphics under Creative Commons 3.0 attribution license

# Fonts from Google Code are under their respective licenses

# Requires:
# Python interpreter: www.python.org
# Pygame library: www.pygame.org

# A simple chess clock program

import pygame
from pygame.locals import *
import os, sys
from string import *
from shutil import copyfile




def generate_screen(dock,screen,pl,d,theme_name,directory):
    for a in range(len(dock)):
        #print dock[a]

        icon_image, icon_rect = load_image(d+dock[a]+'-large.png')
        icon_image = pygame.transform.scale(icon_image, (180,180))
        #pygame.display.update()


        

        icon_rect = ((a*237)+57, 1967)



        icon_image2 = icon_image.copy()
        # this works on images with per pixel alpha too
        alpha = 255
        

        #icon_image2.fill((0, 0, 0, alpha), None, pygame.BLEND_RGBA_MULT)
        if d==directory:
            mask = pygame.image.load("mask.png").convert_alpha()
            icon_image = pgext.color.alphaMask(icon_image, mask, 1)





        screen.blit(icon_image, icon_rect)


    #white = Color('blue')

    #screen.fill(white)




    


    page = pl["iconLists"]
    #for a in range(len(page)):
    for a in range(1):
        print 'page '+str(a)
        y=-1
        
        for b in range(len(page[a])):
            
        #for b in range(1):
            #print type(page[a][b])
            if type(page[a][b])==str:
            
                #print page[a][b]
                'hello'
                icon_image, icon_rect = load_image(d+page[a][b]+'-large.png')
                icon_image = pygame.transform.scale(icon_image, (180,180))
                #icon_image = pygame.transform.set_alpha(50)
                #pygame.display.update()


                nb=b
                
                while nb>4:
                    nb=nb-5
                if b%5==0:
                    y=y+1
                #print nb*15,(y*160)+10,page[a][b]


                
                icon_rect = ((nb*237)+57, (y*300)+120)
                #print d
                if d==directory:
                    mask = pygame.image.load("mask.png").convert_alpha()
                    icon_image = pgext.color.alphaMask(icon_image, mask, 1)
                    #mask = pygame.transform.scale(mask, (180,180))
                    #masked=icon_image.copy()
                    #masked.blit(mask, (0, 0), None, pygame.BLEND_RGBA_MULT)
                    
                    screen.blit(icon_image, icon_rect)
                    #screen.flip()
                else:
                    screen.blit(icon_image, icon_rect)

            if type(page[a][b])==plistlib._InternalDict:
                print 'FOLDER'
                #print len((page[a][b]))
                #for c in range(len(page[a][b])):
                    #print (page[a][b][c])
                #print (page[a][b]['iconLists'])
                #print (page[a][b]['displayName'])

def generate_gradient(from_color, to_color, height, width):
    channels = []
    for channel in range(3):
        from_value, to_value = from_color[channel], to_color[channel]
        channels.append(
            numpy.tile(
                numpy.linspace(from_value, to_value, width), [height, 1],
            ),
        )
    return numpy.dstack(channels)

def load_image(name, colorkey=None):
    fullname = os.path.join("", name)
    try:
        #image = pygame.image.load('picture/com.sopressata.imojistickers.png')
        image = pygame.image.load(name)
        #pygame.image.set_alpha(50)
    except pygame.error, message:
        print 'Cannot load image:', name
        image = pygame.image.load(name)
        image = pygame.image.load('picture/com.sopressata.imojistickers-large.png')
        #raise SystemExit, message
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    pygame.mouse.get_cursor()
    return image, image.get_rect()


def pilll(pl,img,cat,directory):
    

    page = pl[cat]
    #for a in range(len(page)):
    for a in range(1):
        print 'page '+str(a)
        y=-1
        
        for b in range(len(page[a])):
            
        #for b in range(1):
            #print type(page[a][b])
            if type(page[a][b])==str:
                #print "OMGOMG"
                nb=b
                
                while nb>4:
                    nb=nb-5
                if b%5==0:
                    y=y+1
                sc=180
                fx= (nb*237)+57
                fy=(y*300)+120
                if cat=="buttonBar":
                    fy=fy+1976-120
                
                img2=img.crop((fx,fy,fx+sc,fy+sc))
                if page[a][b]=='com.apple.mobiletimer':
                    img2.save(directory2+'ClockIconBackgroundSquare@2x.png')
                    
                img2.save(directory+page[a][b]+'-large.png')

def pilll2(pl,img,cat,directory):
    

    page = pl[cat]
    #for a in range(len(page)):
    for a in range(len(page)):
        print 'page '+str(a)
        y=-1
        
        if 1==1:

            if type(page[a])==str:
                #print "OMGOMG2"


                fx= (a*237)+57
                fy=1966
                sc=180
                
                img2=img.crop((fx,fy,fx+sc,fy+sc))
                
                img2.save(directory+page[a]+'-large.png')
    

def graphics(bg):





        
    theme_name=bg
    #theme_name=raw_input('Theme Name: ')

    directory='themes/'+theme_name+'/IconBundles/'
    global directory2
    directory2='themes/'+theme_name+'/Bundles/com.apple.springboard/'
    directory3='themes/'+theme_name+'/Bundles/com.apple.mobileicons.framework/'
    directory4='themes/'+theme_name+'/'
    directory4a='themes/'+theme_name+'_bg/'
    directory5='themes/'+theme_name+'_bg/AnemoneHTML/'


    if not os.path.exists(directory):
        os.makedirs(directory)
    if not os.path.exists(directory2):
        os.makedirs(directory2)

    if not os.path.exists(directory3):
        os.makedirs(directory3)
    if not os.path.exists(directory5):
        os.makedirs(directory5)


        
    copyfile('Info.plist',directory4+'Info.plist' )  
    copyfile('mask.png',directory3+'AppIconMask@3x~iphone.png' )







    pygame.init()
    pygame.display.init()
    #screen = pygame.display.set_mode((800,480),FULLSCREEN)
    screen = pygame.display.set_mode((1242,2208),pygame.SRCALPHA)
    
    pygame.display.set_caption("Iphone")

    background = pygame.Surface(screen.get_size())
    rect = background.fill((200, 50, 250))

    clock_image, clock_rect = load_image(bg)
    clock_image = pygame.transform.scale(clock_image, (1242,2208))
    screen.blit(clock_image, clock_rect)

    #white = Color('pink')

    #screen.fill(white)





    #pygame.display.update()



    clock = pygame.time.Clock()

    #pl = plistlib.readPlist("IconSupportState.plist")
    #biplist.readPlist
    pl = biplist.readPlist("IconSupportState.plist")
    #dock = pl["buttonBar"]
    dock = pl["buttonBar"]




    
    clock_image, clock_rect = load_image(bg)
    clock_image = pygame.transform.scale(clock_image, (1242,2208))
    screen.blit(clock_image, clock_rect)
    
    
    generate_screen(dock,screen,pl,'picture/',theme_name,directory)



    

        #page=page+1
    pygame.display.update()
    pygame.image.save(screen, "screenshot.jpeg")
    screen_image, screen_rect = load_image("screenshot.jpeg")
    screen_image = pygame.transform.scale(screen_image, (int(1242*.7),int(2208*.75)))
    screen.blit(screen_image, screen_rect)

    pygame.display.update()


    img = Image.open("screenshot.jpeg")
    pilll(pl,img,"iconLists",directory)
    pilll2(pl,img,"buttonBar",directory)

    white = Color('white')

    screen.fill(white)




    clock_image, clock_rect = load_image(bg)
    clock_image = pygame.transform.scale(clock_image, (1242,2208))

    #mode = clock_image.mode
    #size = clock_image.size
    #data = clock_image.tobytes()

    pil_image = pygame.image.tostring(clock_image,'RGBA')

    print type(pil_image)
    pil_image = Image.frombytes("RGBA",(1242,2208),pil_image)


    #pil_image2 = Image.open(pil_image)

    pil_image2=pil_image.filter(ImageFilter.BLUR)
    i=0
    while i<1:
        pil_image2=pil_image2.filter(ImageFilter.GaussianBlur(10))
        i=i+1
        print i
    converter = ImageEnhance.Color(pil_image2)
    pil_image2 = converter.enhance(0.1)
    #py_image = pygame.image.fromstring(data, size, mode)
    pil_image2.save('omg.jpg')




    mode = 'RGBA'
    size = pil_image2.size
    data = pil_image2.tobytes()

    clock_image = pygame.image.fromstring(data, size, mode)



    
    screen.blit(clock_image, clock_rect)


    generate_screen(dock,screen,pl,directory,theme_name,directory)



    time=0
    #screen.blit(clock_image, clock_rect)
    pygame.display.update()
    pygame.image.save(screen, 'screens/'+bg)
    pygame.display.update()
    print 'ok'
    pygame.image.save(screen,directory5+'/bg.jpg')
    copyfile('index.html',directory5+'/index.html' )
    copyfile('Info.plist',directory4a+'/index.html' )  
    
    
    #os.system('img2.png')

def dire(b):
    

    os.chdir(b)
    f=[]
    for file in glob.glob("*.jpg"):
        f.append(file)
    print f
    os.chdir("..")
    for a in range(len(f)):
        graphics(b+'/'+f[a])
    #graphics()



def main():
    a=raw_input('1?')
    if a=='1':
        b=raw_input('file? ')
        if len(b)==0:
            b='imgur/089_J8isla6.jpg'
        graphics(b)
    else:
        b=raw_input('directory?')
        dire(b+'/')
        
    
#graphics('imgur/086_0eFgozw.jpg')
main()

