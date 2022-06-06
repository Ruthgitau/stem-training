import pygame


pygame.init()
screen= pygame.display.set_mode((800,600))

background = pygame.image.load("background.png")
icon = pygame.image.load("space-invader-icon.png")

pygame.display.set_icon(icon)
pygame.display.set_caption("spaceInvader")

while True:
    screen.blit(background,(10,10))
    pygame.display.update()
