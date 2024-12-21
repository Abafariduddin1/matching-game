import pygame
import random
import sys

pygame.init()
screen = pygame.display.set_mode((900, 500))
pygame.display.set_caption("Matching Game Layout")

font = pygame.font.SysFont("Italic", 40)


subway = pygame.image.load("L.5/ssurfer.png")
candy = pygame.image.load("L.5/ccrush.jpg")
temple = pygame.image.load("L.5/trun.png")
ludo = pygame.image.load("L.5/ludo.png")
screen.blit(ludo,(120,50))
screen.blit(temple,(120,160))
screen.blit(candy,(120,270))
screen.blit(subway,(120,380))

te = font.render("Temple Run",False,"white")
lu = font.render("Ludo",False,"white")
ca = font.render("Candy Crush",False,"white")
su = font.render("Subway Surfers",False,"white")
screen.blit(te,(600, 85))
screen.blit(lu,(600,185))
screen.blit(su,(600,285))
screen.blit(ca,(600,400))

image_positions = [(100, 80), (100, 180), (100, 280), (100, 380)]
text_positions = [(600, 80), (600, 180), (600, 280), (600, 380)]
text_items = ["Subway Surfers", "Temple Run", "Candy Crush", "Ludo"]


while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousepos=pygame.mouse.get_pos()
            pygame.draw.circle(screen,"white",mousepos,4)
        if event.type == pygame.MOUSEBUTTONUP:
            mousepos2 = pygame.mouse.get_pos()
            pygame.draw.circle(screen,"white",mousepos2,4)   
            pygame.draw.line(screen,"white",mousepos,mousepos2,2)     
        pygame.display.update()

