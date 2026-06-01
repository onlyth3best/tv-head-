#trying out some pygame code for the actual rPi5 thingy ;DD
# never used pygame before so trying to animate on my laptop before transferring to rPi5
import pygame
import os
import sys


# note!!! !!! ! TO SELF EDIT ANIMATIONS (centre, too fast)
#original #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\
o1 = pygame.image.load(os.path.join(os.path.dirname(__file__), 'example', 'fallout1.png'))
idle1 = pygame.transform.scale(o1, (o1.get_width() * 2, o1.get_height() * 2))
idle1_rect = idle1.get_rect()

o2 = pygame.image.load(os.path.join(os.path.dirname(__file__), 'example', 'fallout2.png'))
idle2 = pygame.transform.scale(o2, (o2.get_width() * 2, o2.get_height() * 2))
idle2_rect = idle2.get_rect()

o3 = pygame.image.load(os.path.join(os.path.dirname(__file__), 'example', 'fallout3.png'))
idle3 = pygame.transform.scale(o3, (o3.get_width() * 2, o3.get_height() * 2))
idle3_rect = idle3.get_rect()

o4 = pygame.image.load(os.path.join(os.path.dirname(__file__), 'example', 'fallout4.png'))
idle4 = pygame.transform.scale(o4, (o4.get_width() * 2, o4.get_height() * 2))
idle4_rect = idle4.get_rect()

o5 = pygame.image.load(os.path.join(os.path.dirname(__file__), 'example', 'fallout5.png'))
idle5 = pygame.transform.scale(o5, (o5.get_width() * 2, o5.get_height() * 2))
idle5_rect = idle5.get_rect()

o6 = pygame.image.load(os.path.join(os.path.dirname(__file__), 'example', 'fallout6.png'))
idle6 = pygame.transform.scale(o6, (o6.get_width() * 2, o6.get_height() * 2))
idle6_rect = idle6.get_rect()

o7 = pygame.image.load(os.path.join(os.path.dirname(__file__), 'example', 'fallout7.png'))
idle7 = pygame.transform.scale(o7, (o7.get_width() * 2, o7.get_height() * 2))
idle7_rect = idle7.get_rect()

o8 = pygame.image.load(os.path.join(os.path.dirname(__file__), 'example', 'fallout7.png'))
idle8 = pygame.transform.scale(o8, (o8.get_width() * 2, o8.get_height() * 2))
idle8_rect = idle8.get_rect()

# annoyed
o9 = pygame.image.load(os.path.join(os.path.dirname(__file__), 'example', 'fallout7.png'))
idle9 = pygame.transform.scale(o9, (o9.get_width() * 2, o9.get_height() * 2))
idle9_rect = idle9.get_rect()

o10 = pygame.image.load(os.path.join(os.path.dirname(__file__), 'example', 'fallout7.png'))
idle10 = pygame.transform.scale(o10, (o10.get_width() * 2, o10.get_height() * 2))
idle10_rect = idle10.get_rect()

#happy
o11 = pygame.image.load(os.path.join(os.path.dirname(__file__), 'example', 'fallout7.png'))
idle11 = pygame.transform.scale(o11, (o11.get_width() * 2, o11.get_height() * 2))
idle11_rect = idle11.get_rect()

o12 = pygame.image.load(os.path.join(os.path.dirname(__file__), 'example', 'fallout7.png'))
idle12 = pygame.transform.scale(o12, (o12.get_width() * 2, o12.get_height() * 2))
idle12_rect = idle12.get_rect()
#animations, arrays #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\

idleAnim = [
    idle1, idle2, idle3, idle4, idle5, idle6, idle7, idle8
]

annoyedAnim = [
    idle9, idle10
]

happyAnim = [
    idle11, idle12
]

#---
current_image_index = 0
image = idleAnim[current_image_index]
pygame.init()

#~ ~ ~ ~ ~ ~ ~
import pygame.font
pixFont = pygame.font.Font(((os.path.join(os.path.dirname(__file__), 'example', 'Minecraft.ttf'))), 25)

text_dir = 1
clock = pygame.time.Clock()
switch_time = 150  #this in milliseconds (=1 second), fps speed
last_switch = pygame.time.get_ticks()

#~ ~ ~ ~ ~ ~ ~

screen = pygame.display.set_mode((740, 580))
pygame.display.set_caption('fallout : tv-head display, test')
font = pixFont
text = font.render('> <', True, (255, 255, 255))

text_rect = text.get_rect()
text_rect.center = (screen.get_width() // 2, screen.get_height() - 50)
idle1_rect.center = (screen.get_width() / 2, screen.get_height() / 2)


# - - - - - - - - - - - - - - - - - . * * * * * * * * * * * * * * * * * #
#things to be set later:
isTilted = False
    #either will randomly change
    #or based on directional tilt
    #…or perhaps another input; will decide

#- - - - - - -
# main loop
running = True
while running:
    #clock - text mechanism
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # text
    text_rect.x += 2
    if text_rect.left > screen.get_width():
        text_rect.x = -150

    # -- -- - -- -- - -- -- - -- -- - -- -- - -- -
    screen.fill((0, 0, 0))
    screen.blit(image, (idle1_rect))
    screen.blit(text, text_rect) #drawing text - screen.blit(text, (text_rect))
    pygame.display.update() #updating display

    current_time = pygame.time.get_ticks()
    if current_time - last_switch > switch_time:
        current_image_index = (current_image_index + 1) % len(idleAnim) #change idleAnim to another
        image = idleAnim[current_image_index]
        last_switch = current_time

#to quit
pygame.quit()
sys.exit()