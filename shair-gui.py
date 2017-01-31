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


def load_image(name, colorkey=None):
    fullname = os.path.join("graphics", name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


time_a = 500
time_b = 600
artist = "Blink 182"
album  = "Take Off Your Pants"
song   = "The Rock Show"
a_on = True
b_on = False


pygame.init()
pygame.display.init()
#screen = pygame.display.set_mode((800,480),FULLSCREEN)
screen = pygame.display.set_mode((800,480))
pygame.display.set_caption("Chess Clock")

background = pygame.Surface(screen.get_size())
rect = background.fill((0, 0, 0))

clock_image, clock_rect = load_image("clock.jpg")
album_image, album_rect = load_image("toypaj.png")



clock = pygame.time.Clock()

font = pygame.font.Font("fonts/BowlbyOneSC.ttf", 34)

#mainloop
while True:
	clock.tick(1)
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()
			
		if event.type == USEREVENT:
			if time_a > 0:
				time_a += 1
			else:
				pygame.time.set_timer(USEREVENT, 0)

		elif event.type == (USEREVENT + 1):
			if time_b > 0:
				time_b += 1
			else:
				pygame.time.set_timer(USEREVENT, 0)			

		elif event.type == KEYDOWN:

			if event.key == K_a:
				if not a_on:
					# Set for 1 second (1000 milliseconds)
					pygame.time.set_timer(USEREVENT, 1000)
					a_on = True
				else:
					# The other one should turn on immediately
					pygame.time.set_timer(USEREVENT, 0)
					pygame.time.set_timer(USEREVENT+1, 1000)
					b_on = True
					a_on = False

			if event.key == K_b:
				if not b_on:
					pygame.time.set_timer(USEREVENT+1, 1000)
					b_on = True
				else:
					pygame.time.set_timer(USEREVENT+1, 0)
					pygame.time.set_timer(USEREVENT, 1000)
					a_on = True
					b_on = False

			if event.key == K_q:
				#time_a += 60 # add a minute from alloted time
				pygame.quit()

			if event.key == K_z:
				time_a -= 60 # subtract a minute

			if event.key == K_g:
				time_b += 60

			if event.key == K_n:
				time_b -= 60

			if event.key == K_PAUSE or event.key == K_p:
				#pause both timers
				pygame.time.set_timer(USEREVENT+1, 0)
				pygame.time.set_timer(USEREVENT, 0)
	
	# Format time into minutes:seconds
	time_a_str = "%d:%02d" % (int(time_a/60),int(time_a%60))

	time_a_txt = font.render(time_a_str, 1, (255, 255, 255))
	artist_txt = font.render(artist, 2, (255, 255, 255))
	album_txt = font.render(album, 2, (255, 255, 255))
	song_txt = font.render(song, 2, (255, 255, 255))

	album_image_rect = (000, 160)
	album_image = pygame.transform.scale(album_image, (200,200))

#        
	artist_rect = artist_txt.get_rect()
	artist_rect = (400, 160)
#        
	album_rect = album_txt.get_rect()
	album_rect = (400, 210)
#            
	song_rect = song_txt.get_rect()
	song_rect = (400, 260)


	time_a_rect = time_a_txt.get_rect()
	time_a_rect = (400, 310)

	


	screen.blit(background, rect)

	
	screen.blit(clock_image, clock_rect)

	screen.blit(album_image, album_image_rect)

	screen.blit(artist_txt, artist_rect)
	screen.blit(album_txt, album_rect)
	screen.blit(song_txt, song_rect)
	screen.blit(time_a_txt, time_a_rect)

	pygame.display.update()
#end mainloop	 
	

	

	

