#Dodle Jump
#Created by Suraj Saripalli

import pygame
import time
import random

pygame.init()
s = pygame.display.set_mode((1362, 800))
pygame.display.set_caption("Dodle Jums")
pos = (15, 960)
bg = pygame.image.load("dodle.png")
womp = pygame.image.load("wompwomp.jpg").convert_alpha()
clock = pygame.time.Clock()
og_x = 0
og_y = 700
og_man_x = -50
og_man_y = 580
up = False
down = True
jumper = 75
score = 0
font = pygame.font.Font(None, 256)

s.blit(bg, (0,0))
gaming = True
    
def hitboxes(jums):
    global dodle_man
    pygame.draw.rect(s,( 255, 0, 0), dodle_man.collision_rect, 2) #Test hitboxes for dodle_man
    for platform in jums:
        '''Test hitboxes for jums'''
        pygame.draw.rect(s, (0, 255, 0), platform, 2)
    
class Dodle_man(pygame.sprite.Sprite):
    def __init__(self, image, scale, x, y):
        pygame.sprite.Sprite.__init__(self)
        og_image = pygame.image.load(image).convert_alpha()
        w = int(og_image.get_width() * scale)
        h = int(og_image.get_height() * scale)
        self.image = pygame.transform.scale(og_image, (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collision_rect = self.rect.copy()
        self.collision_rect.width = 45
        self.collision_rect.height = self.rect.height - 55
        self.collision_rect.y = self.rect.y
        self.collision_rect.x = self.rect.x
        self.collision_rect.centerx = self.rect.centerx

class Jums(pygame.sprite.Sprite):
    def __init__(self, image, scale, x, y):
        pygame.sprite.Sprite.__init__(self)
        og_image = pygame.image.load(image).convert_alpha()
        w = int(og_image.get_width() * scale)
        h = int(og_image.get_height() * scale)
        self.image = pygame.transform.scale(og_image, (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

            

def objects():
    dodle_man = Dodle_man("dodle_man.png", 0.5, og_man_x, og_man_y)
    jums = pygame.sprite.Group()
    jum = Jums("jums.png", 0.125, og_x, og_y)
    jum1 = Jums("jums.png", 0.125, random.randint(0,350), random.randint(570,580))
    jum2 = Jums("jums.png", 0.125, random.randint(400,600), random.randint(480,500))
    jum3 = Jums("jums.png", 0.125, random.randint(700,1000), random.randint(525,550))
    jum4 = Jums("jums.png", 0.125, random.randint(900,1200), random.randint(400,500))
    jum5 = Jums("jums.png", 0.125, random.randint(1000,1250), random.randint(300,600))
    jum6 = Jums("jums.png", 0.125, random.randint(700,1000), random.randint(200, 300))
    jum7 = Jums("jums.png", 0.125, random.randint(500,1000), random.randint(150,200))
    jum8 = Jums("jums.png", 0.125, random.randint(500,1000), random.randint(50, 100))
    jums.add(jum, jum1, jum2, jum3, jum4, jum5, jum6, jum7, jum8)
    sprites = pygame.sprite.Group()
    sprites.add(dodle_man)
    sprites.add(jums)

    return jums, sprites, dodle_man

jums, sprites, dodle_man = objects()

while gaming == True:
    bottom = pygame.Rect(dodle_man.collision_rect.left, dodle_man.collision_rect.bottom, dodle_man.collision_rect.width, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gaming = False
            
    if up:
        dodle_man.collision_rect.y -= 100
        dodle_man.rect.y -= 100
        up = False
        down = True
    
    if down:
        dodle_man.collision_rect.y += 5
        dodle_man.rect.y += 5
        for platform in jums:
            if bottom.colliderect(platform.rect):
                score += 1
                down = False
                up = True
    
    if dodle_man.rect.y > 801:
        score_display = font.render(f"Score: {score}", True, (0,0,0))
        s.blit(womp, (0,0))
        s.blit(score_display, (300, 600))
        pygame.display.flip()
        time.sleep(2)
        gaming = False
    
    if bottom.y < -35:
        dodle_man.rect.x = og_man_x
        dodle_man.collision_rect.x = og_man_x
        dodle_man.rect.y = og_man_y
        dodle_man.collision_rect.y = og_man_y
        time.sleep(1)
        jums, sprites, dodle_man = objects()
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        dodle_man.collision_rect.x += 10
        dodle_man.rect.x += 10
    if keys[pygame.K_LEFT]:
        dodle_man.collision_rect.x -= 10
        dodle_man.rect.x -= 10
            
    s.blit(bg, (0,0))
    sprites.draw(s)
    pygame.display.flip()
    clock.tick(50)
    
pygame.quit()
