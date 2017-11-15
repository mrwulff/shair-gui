import pygame
import socket
from string import *
import random
import datetime
import time
import obd
import socket



try:
    import _rpi_ws281x as ws
    from rpi_TM1638 import TMBoards
    hasgpio=True

    DIO = 17
    CLK = 27
    STB = 22,23

    TM = TMBoards(DIO, CLK, STB, 0)
    LED_CHANNEL    = 0
    LED_COUNT      =24          # How many LEDs to light.
    LED_FREQ_HZ    = 800000     # Frequency of the LED signal.  Should be 800khz or 400khz.
    LED_DMA_NUM    = 5          # DMA channel to use, can be 0-14.
    LED_GPIO       = 18         # GPIO connected to the LED signal line.  Must support PWM!
    LED_BRIGHTNESS = 255        # Set to 0 for darkest and 255 for brightest
    LED_INVERT     = 0          # Set to 1 to invert the LED signal, good if using NPN
                                                            # transistor as a 3.3V->5V level converter.  Keep at 0
                                                            # for a normal/non-inverted signal.

    # Define colors which will be used by the example.  Each color is an unsigned
    # 32-bit value where the lower 24 bits define the red, green, blue data (each
    # being 8 bits long).
    DOT_COLORS = [          0x200000,   # red
                                    0x000000,   # black
                                    0x201000,   # orange
                                    0x202000,   # yellow
                                    0x002000,   # green
                                    0x002020,   # lightblue
                                    0x000020,   # blue
                                    0x100010,   # purple
                                    0x200010 ]  # pink


    # Create a ws2811_t structure from the LED configuration.
    # Note that this structure will be created on the heap so you need to be careful
    # that you delete its memory by calling delete_ws2811_t when it's not needed.
    leds = ws.new_ws2811_t()


    for channum in range(2):
        channel = ws.ws2811_channel_get(leds, channum)
        ws.ws2811_channel_t_count_set(channel, 0)
        ws.ws2811_channel_t_gpionum_set(channel, 0)
        ws.ws2811_channel_t_invert_set(channel, 0)
        ws.ws2811_channel_t_brightness_set(channel, 0)

    channel = ws.ws2811_channel_get(leds, LED_CHANNEL)

    ws.ws2811_channel_t_count_set(channel, LED_COUNT)
    ws.ws2811_channel_t_gpionum_set(channel, LED_GPIO)
    ws.ws2811_channel_t_invert_set(channel, LED_INVERT)
    ws.ws2811_channel_t_brightness_set(channel, LED_BRIGHTNESS)

    ws.ws2811_t_freq_set(leds, LED_FREQ_HZ)
    ws.ws2811_t_dmanum_set(leds, LED_DMA_NUM)

    # Initialize library with LED configuration.
    resp = ws.ws2811_init(leds)
    if resp != ws.WS2811_SUCCESS:
            message = ws.ws2811_get_return_t_str(resp)
            raise RuntimeError('ws2811_init failed with code {0} ({1})'.format(resp, message))






except:
    print 'windows...'
    hasgpio=False






try:
    connection = obd.OBD() # auto-connects to USB or RF port
    

    cmd = obd.commands.AMBIANT_AIR_TEMP # select an OBD command (sensor)
    

    response = connection.query(cmd) # send the command, and parse the response
    hasobd=True

    none2(response.value) # returns unit-bearing values thanks to Pint
    #print '^^^'
    if none2=='None':
        hasobd=False
#print(response.value.to("mph")) # user-friendly unit conversions
except:
    print 'OBD FAIL'
    hasobd=False
    

pygame.init()
#screen = pygame.display.set_mode((720, 480),pygame.FULLSCREEN)
#screen = pygame.display.set_mode((640, 480))
screen = pygame.display.set_mode((720,480))


clock2 = pygame.time.Clock()
done = False

font = pygame.font.SysFont("44", 72)
fonts = pygame.font.SysFont("44", 34)




# LED configuration.


# Initialize all channels to off


# Wrap following code in a try/finally to ensure cleanup functions are called
# after library is initialized.

songs='song'
artists='artist'
albums='album'


i=0

count=0
data=''
page=1
pages=5

xpos=32
xxpos=105
ypos=381
offset=90
choice=0
tchoice=4

def menu():
    global xpos
    global xxpos
    global choice
    global ypos
    #print ypos
    #print socket.gethostbyname(socket.gethostname())


    bg = pygame.image.load('image/bgmenu.png')
    screen.blit(bg, (00, 0))

    more = pygame.image.load('image/next.png')
    screen.blit(more, (421, 381))

    if choice<4:
        select = pygame.image.load('image/lowlight.png')
        screen.blit(select, (85, xxpos+(choice*offset)))
    else:
        select = pygame.image.load('image/nexth.png')
        screen.blit(select, (421,381))
    


    
    albumt = font.render("Menu", True, (255, 228, 0))
    screen.blit(albumt,(188,xpos))


    albumt = font.render("Reconnect All", True, (255, 228, 0))
    screen.blit(albumt,(188,xpos+offset))

    albumt = font.render("OBDII Info", True, (255, 228, 0))
    screen.blit(albumt,(188,xpos+(offset*2)))


    albumt = font.render("Metadata Info", True, (255, 228, 0))
    screen.blit(albumt,(188,xpos+(offset*3)))


    albumt = font.render("Network Info", True, (255, 228, 0))
    screen.blit(albumt,(188,xpos+(offset*4)))

    albumt = font.render(">", True, (255, 228, 0))
    screen.blit(albumt,(655,xpos+(offset*4)))


    if hasobd==False:
        more = pygame.image.load('image/fail.png')
        pygame.transform.scale(more,(150,100))

        screen.blit(more, (90, 200))
    


    pygame.display.flip()

def menu2():



    bg = pygame.image.load('image/bgmenu.png')
    screen.blit(bg, (00, 0))


    
    albumt = font.render("Menu2", True, (255, 228, 0))
    screen.blit(albumt,(188,xpos))




    pygame.display.flip()

def reconnect():
    try:
        print 'doing stuff'

        connection = obd.OBD() # auto-connects to USB or RF port
        

        cmd = obd.commands.AMBIANT_AIR_TEMP # select an OBD command (sensor)
        

        response = connection.query(cmd) # send the command, and parse the response
        hasobd=True
    except:
        print "no obd.  windows"


    
def obd():
    print 'obd stuff'
def music():
    print 'lalalalla'
def network():
    print 'pinginig'


    bg = pygame.image.load('image/blank.png')
    screen.blit(bg, (00, 0))


    
    albumt = fonts.render("Menu2", True, (255, 228, 0))
    screen.blit(albumt,(188,xpos))


    ip=socket.gethostbyname(socket.gethostname())

    albumt = fonts.render(ip, True, (255, 228, 0))
    screen.blit(albumt,(188,xpos+50))



    pygame.display.flip()
    
        
while not done:
    #print choice,' choice'
    #print page,' page'
    if page>pages:
        page=0
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
            pygame.display.quit()
            done = True
            quit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            i=i+1



        if event.type == pygame.KEYDOWN and event.key == pygame.K_4:
            page=page+1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            choice=choice-1
            print '+5'

        if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
            choice=choice+1




        if event.type == pygame.KEYDOWN and event.key == pygame.K_5:
            ypos=ypos+10


        if event.type == pygame.KEYDOWN and event.key == pygame.K_6:
            ypos=ypos-9
            #print '-3'

        if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
            if page==1:
                if choice==0:
                    print "Reconnect all shit"
                    reconnect()
                if choice==1:
                    print 'OBD STUFF'
                    obd()
                if choice==2:
                    print "MUSIC STUFF"
                    music()


                if choice==3:
                    print "network"
                    page=5
                    network()
            


            
    if choice>tchoice:
        choice=0
    if choice<0:
        choice=tchoice

    if page==1:
        menu()

    if page==5:
        network()



    if page==0:
    

        count=count+1
        if count>101:
            count=0
        






        
        i=0
        if count==100:
            print '100 BITCHES'
            b=open('data.txt','r')
            for line in b.readlines():
                #print line
                if len(line)>5:
                    
                    songs,artists,albums,stat,junk=split(line,"###")
            b.close()


        if hasobd==True:
            cmd = obd.commands.AMBIANT_AIR_TEMP # select an OBD command (sensor)

            response = connection.query(cmd) # send the command, and parse the response
            try:
                temp=(response.value.to("fahrenheit")) # returns unit-bearing values thanks to Pint
            except:
                temp=(response.value) 
            temp=str(temp)

            try:
                temp,junk=split(temp,'.')
            except:
                temp=temp


            cmd = obd.commands.SPEED # select an OBD command (sensor)

            response = connection.query(cmd) # send the command, and parse the response

            try:
                speed=(response.value.to("mph")) # returns unit-bearing values thanks to Pint
            except:
                speed=(response.value)
            speeds=str(speed)
            try:
                speeds,junk=split(speeds,' ')
            except:
                speeds=speeds


            cmd = obd.commands.RPM # select an OBD command (sensor)

            response = connection.query(cmd) # send the command, and parse the response

            rpm=(response.value) # returns unit-bearing values thanks to Pint
            
            rpms=str(rpm)
            try:
                rpms,junk=split(rpms,' ')
            except:
                rpms=rpms
            if rpms=="None":
                rpms=str(random.randint(600,4000))
                rpms=rpms+'.0'

            rpmst,junk=split(rpms,'.')





        #print hasobd
        if hasobd==False:
            tempt=str(random.randint(1,80))
            speeds=str(random.randint(1,80))
            rpms=str(random.randint(600,4000))
            rpms=rpms
            rpmst=rpms
            
        

        ##########WTF
        


        
            






        #print rpmst
        pp=int(rpmst)/150
        pp=int(pp)
        pp=pp-5
        #print pp

        if hasgpio==True:# Update each LED color in the buffer.


            for i in range(pp,0,-1):
                    # Pick a color based on LED position and an offset for animation.
                    #color = DOT_COLORS[(i + offset) % len(DOT_COLORS)]
                    if i<8:
                            color=DOT_COLORS[3]
                    if i<16 and pp>7:
                            color=DOT_COLORS[4]
                    if i>15:
                            color=DOT_COLORS[5]
                    # Set the LED color buffer value.
                    ws.ws2811_led_set(channel, i, color)
            for i in range(24,pp,-1):
                    color=0x000000
                    ws.ws2811_led_set(channel, i ,color)
            # Send the LED color data to the hardware.
            resp = ws.ws2811_render(leds)
            if resp != ws.WS2811_SUCCESS:
                    message = ws.ws2811_get_return_t_str(resp)
                    raise RuntimeError('ws2811_render failed with code {0} ({1})'.format(resp, message))



        bg = pygame.image.load('image/bgb.png')
        screen.blit(bg, (00, 0))


        #screen.fill((0,0,0))
    #    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes





        ar=random.randint(0,99999999)
        br=random.randint(0,99999999)
        
        mode=['OilTEMP','RPM',"  SPEED",'INTAKE',"Throttle"]
        if hasgpio==True:
            TM.clearDisplay()

            ar= i%len(mode)
            print ar
            TM.segments[0] = str(mode[ar] )      # display '0' on the display 1 (2nd 7-segment display of the 1st board)


            TM.segments[8] = str(br)


        
        



        rpmt = font.render(rpms, True, (255, 255, 0))
        screen.blit(rpmt,(475,320))
        



        tempt = font.render(tempt, True, (255, 228, 0))
        screen.blit(tempt,(120,400))



        speedt = font.render(speeds, True, (255, 128, 100))
        screen.blit(speedt,(120, 320))


        clockd=time.strftime("%I:%M %p")
        clockt = font.render(clockd, True, (0, 255, 255))
        screen.blit(clockt,(475,400))



        songt = font.render(songs, True, (255, 228, 0))
        screen.blit(songt,(188,60))



        albumt = font.render(albums, True, (255, 228, 0))
        screen.blit(albumt,(188,150))


        artistt = font.render(artists, True, (255, 228, 0))
        screen.blit(artistt,(188,230))


      
       
        pygame.display.flip()

    clock2.tick(20)























# coding=utf-8
from time import sleep


i=0
while 1==1:

    

    aa=raw_input('CLICK')

    i=i+1
