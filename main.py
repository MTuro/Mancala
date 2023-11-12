import pygame
import sys
from tabuleiro import *

pygame.init()

# Configs da janela

# Loop do jogo
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    draw()
