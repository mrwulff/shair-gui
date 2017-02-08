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


import pygame
from pygame.locals import *
import os, sys
from string import *
from shutil import copyfile


phone='k'
phone='b'

scale=4

blur=1

if phone=='k':
    phonex=1242*scale
    phoney=2208*scale
    column=5
    dock=5
    icon_size=180*scale
    dock_pos=1967
    icon_offset=57
    icon_spacing=237
    icon_y_offset=120
    icon_y_spacing=300


    icon_d_spaciing=237
    icon_d_offset=57
if phone=='b':
    phonex=750*scale
    phoney=1334*scale
    column=4
    dock=5
    icon_size=120*scale
    dock_pos=1169*scale
    #icon_offset=28
    #icon_spacing=144
    #icon_y_offset=176
    #icon_y_spacing=156



    icon_offset=53*scale
    icon_spacing=174*scale
    icon_y_offset=56*scale
    icon_y_spacing=176*scale

    icon_d_spacing=145*scale
    icon_d_offset=25*scale

    


def generate_screen(dock,screen,pl,d,theme_name,directory):
    for a in range(len(dock)):
        #print dock[a]

        icon_image, icon_rect = load_image(d+dock[a]+'-large.png')
        icon_image = pygame.transform.scale(icon_image, (icon_size,icon_size))
        pygame.display.update()



            
        icon_rect = ((a*icon_d_spacing)+icon_d_offset, dock_pos)





        icon_image2 = icon_image.copy()
        # this works on images with per pixel alpha too
        alpha = 255
        

        #icon_image2.fill((0, 0, 0, alpha), None, pygame.BLEND_RGBA_MULT)
        if d==directory:
            mask = pygame.image.load("mask.png").convert_alpha()
            
            mask = pygame.transform.scale(mask, (icon_size,icon_size))
            print icon_image.get_width()
            print mask.get_width()
            
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
                if phone=='k':
                    
                    icon_image = pygame.transform.scale(icon_image, (icon_size,icon_size))
                if phone=='b':
                    icon_image = pygame.transform.scale(icon_image, (icon_size,icon_size))
                #icon_image = pygame.transform.set_alpha(50)
                #pygame.display.update()


                nb=b
                
                while nb>(column-1):
                    nb=nb-column
                if b%column==0:
                    y=y+1
                #print nb*15,(y*160)+10,page[a][b]


                icon_rect = ((nb*icon_spacing)+icon_offset, (y*icon_y_spacing)+icon_y_offset)
                                #print d
                if d==directory:
                    mask = pygame.image.load("mask.png").convert_alpha()
                    mask = pygame.transform.scale(mask, (icon_size,icon_size))
                    icon_image = pgext.color.alphaMask(icon_image, mask, 1)

                    
                    screen.blit(icon_image, icon_rect)
                else:
                    screen.blit(icon_image, icon_rect)

            if type(page[a][b])==plistlib._InternalDict:
                print 'FOLDER'


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
    print name
    fullname = os.path.join("", name)
    try:
        #image = pygame.image.load('picture/com.sopressata.imojistickers.png')
        image = pygame.image.load(name)
        #pygame.image.set_alpha(50)
    except pygame.error, message:
        print 'Cannot load image:', name
        #image = pygame.image.load(name)
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
                
                while nb>column-1:
                    nb=nb-column
                if b%column==0:
                    y=y+1
                sc=icon_size
                fx= (nb*icon_spacing)+icon_offset
                fy=(y*icon_y_spacing)+icon_y_offset
               
                if cat=="buttonBar":
                    fy=fy+dock_pos-120
                    if phone=='b':
                        fy=fy
                        
                #icon_rect = ((nb*174)+54, (y*176)+56)



                
                img2=img.crop((fx,fy,fx+sc,fy+sc))
                if page[a][b]=='com.apple.mobiletimer':
                    img2.save(directory2+'ClockIconBackgroundSquare@2x.png')
                    
                img2.save(directory+page[a][b]+'-large.png')

def pilll2(pl,img,cat,directory):
    

    page = pl[cat]
    print page,'omg',len(page)
    #for a in range(len(page)):
    for a in range(len(page)):
        print 'page '+str(a)
        y=-1
        
        if 1==1:

            if type(page[a])==str:
                #print "OMGOMG2"


                fx= (a*icon_d_spacing)+icon_d_offset
                fy=dock_pos
                sc=icon_size

                    
                
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


    screen = pygame.display.set_mode((phonex,phoney),pygame.SRCALPHA)
    
    pygame.display.set_caption("Iphone")

    background = pygame.Surface(screen.get_size())
    rect = background.fill((200, 50, 250))

    clock_image, clock_rect = load_image(bg)

    
    clock_image = pygame.transform.scale(clock_image, (phonex,phoney))

    screen.blit(clock_image, clock_rect)

    #white = Color('pink')

    #screen.fill(white)





    #pygame.display.update()



    clock = pygame.time.Clock()

    #pl = plistlib.readPlist("IconSupportState.plist")
    #biplist.readPlist
    if phone=='k':
        pl = biplist.readPlist("IconSupportState.plist.kevin")
    if phone=='b':
        pl = biplist.readPlist("IconSupportState.plist.britt")
    #dock = pl["buttonBar"]
    dock = pl["buttonBar"]




    
    clock_image, clock_rect = load_image(bg)
    clock_image = pygame.transform.scale(clock_image, (phonex,phoney))
    screen.blit(clock_image, clock_rect)
    
    
    generate_screen(dock,screen,pl,'picture/',theme_name,directory)



    

        #page=page+1
    pygame.display.update()
    pygame.image.save(screen, "screenshot.jpeg")
    screen_image, screen_rect = load_image("screenshot.jpeg")
    screen_image = pygame.transform.scale(screen_image, (int(phonex*.75),int(phoney*.75)))
    #screen.blit(screen_image, screen_rect)

    pygame.display.update()


    img = Image.open("screenshot.jpeg")
    pilll(pl,img,"iconLists",directory)
    pilll2(pl,img,"buttonBar",directory)

    white = Color('white')

    screen.fill(white)



    newbg=raw_input('custom back ground')
    clock_image, clock_rect = load_image(newbg)
    if len(newbg)==0:
        
        clock_image, clock_rect = load_image(bg)
    
    clock_image = pygame.transform.scale(clock_image, (phonex,phoney))

    #mode = clock_image.mode
    #size = clock_image.size
    #data = clock_image.tobytes()

    pil_image = pygame.image.tostring(clock_image,'RGBA')

    print type(pil_image)
    pil_image = Image.frombytes("RGBA",(phonex,phoney),pil_image)


    #pil_image2 = Image.open(pil_image)
    pil_image2=pil_image
    #pil_image2=pil_image.filter(ImageFilter.BLUR)
    i=0
    while i<blur:
        pil_image2=pil_image2.filter(ImageFilter.GaussianBlur(10))
        i=i+1
        print i
    converter = ImageEnhance.Color(pil_image2)
    pil_image2 = converter.enhance(.5)
    ####py_image = pygame.image.fromstring(data, size, mode)
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
    copyfile('Info.plist',directory4a+'/Info.plist' )  
    
    
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
    if a=='':
        b='unnamed.jpg'
        b='3.jpg'
        graphics(b)
        
    if a=='1':
        b=raw_input('file? ')
        if len(b)==0:
            b='unnamed'
        graphics(b)
    else:
        b=raw_input('directory?')
        dire(b+'/')
        
    
#graphics('imgur/086_0eFgozw.jpg')
main()

