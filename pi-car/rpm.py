import pygame
import socket
from string import *
import random
import datetime
import time
import obd
import _rpi_ws281x as ws


connection = obd.OBD() # auto-connects to USB or RF port

cmd = obd.commands.AMBIANT_AIR_TEMP # select an OBD command (sensor)

response = connection.query(cmd) # send the command, and parse the response

print(response.value) # returns unit-bearing values thanks to Pint
#print(response.value.to("mph")) # user-friendly unit conversions

pygame.init()
screen = pygame.display.set_mode((720, 480),pygame.FULLSCREEN)
#screen = pygame.display.set_mode((640, 480))
#screen = pygame.display.set_mode((720,480))


clock2 = pygame.time.Clock()
done = False

font = pygame.font.SysFont("44", 72)

songs='song'
artists='artist'
albums='album'


# LED configuration.
LED_CHANNEL    = 0
LED_COUNT      =24          # How many LEDs to light.
LED_FREQ_HZ    = 800000     # Frequency of the LED signal.  Should be 800khz or 400khz.
LED_DMA_NUM    = 5          # DMA channel to use, can be 0-14.
LED_GPIO       = 18         # GPIO connected to the LED signal line.  Must support PWM!
LED_BRIGHTNESS = 55        # Set to 0 for darkest and 255 for brightest
LED_INVERT     = 0          # Set to 1 to invert the LED signal, good if using NPN
							# transistor as a 3.3V->5V level converter.  Keep at 0
							# for a normal/non-inverted signal.

# Define colors which will be used by the example.  Each color is an unsigned
# 32-bit value where the lower 24 bits define the red, green, blue data (each
# being 8 bits long).
DOT_COLORS = [ 			0x200000,   # red
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

# Initialize all channels to off
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

# Wrap following code in a try/finally to ensure cleanup functions are called
# after library is initialized.







data=''
while not done:


    





		    
    try:
    
        fart
    except:
        print 'waiiting'
    b=open('data.txt','r')
    i=0
    for line in b.readlines():
        print line
        if len(line)>5:
            
            songs,artists,albums,stat,junk=split(line,"###")
    b.close()



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
    if temp=="None":
        #print 'NONEONEONEONEONEONEON'
        temp=str(random.randint(1,80))  
    

    
    


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
    if speeds=="None":
        speeds=str(random.randint(1,80))




    cmd = obd.commands.RPM # select an OBD command (sensor)

    response = connection.query(cmd) # send the command, and parse the response

    rpm=(response.value) # returns unit-bearing values thanks to Pint
    
    rpms=str(rpm)
    print rpms
    try:
	rpms,junk=split(rpms,' ')
    except:
	rpms=rpms
    if rpms=="None":
        rpms=str(random.randint(1000,6000))



    pp=random.randint(1,24)
		# Update each LED color in the buffer.
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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
            quit()
    #screen.fill((0,0,0))
#    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    



    rpmt = font.render(rpms, True, (255, 255, 0))
    screen.blit(rpmt,(475,320))
    



    tempt = font.render(temp, True, (255, 228, 0))
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
    clock2.tick(10)







'''

#Example of low-level Python wrapper for rpi_ws281x library.
# Author: Tony DiCola (tony@tonydicola.com), Jeremy Garff (jer@jers.net)
#
# This is an example of how to use the SWIG-generated _rpi_ws281x module.
# You probably don't want to use this unless you are building your own library,
# because the SWIG generated module is clunky and verbose.  Instead look at the
# high level Python port of Adafruit's NeoPixel Arduino library in strandtest.py.
#
# This code will animate a number of WS281x LEDs displaying rainbow colors.



try:
	offset = 0
	while True:
		

		# Delay for a small period of time.
		time.sleep(0.25)

		# Increase offset to animate colors moving.  Will eventually overflow, which
		# is fine.
		offset += 1

finally:
	# Ensure ws2811_fini is called before the program quits.
	ws.ws2811_fini(leds)
	# Example of calling delete function to clean up structure memory.  Isn't
	# strictly necessary at the end of the program execution here, but is good practice.
	ws.delete_ws2811_t(leds)

'''
