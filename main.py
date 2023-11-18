import pygame
import sys
from tabuleiro import *

tabuleiro = [[4] * 6, [4] * 6, [0, 0]]
turno = 0

pygame.init()

# Loop do jogo
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            verificaClique(tabuleiro,pygame.mouse.get_pos(),turno)

    atualizaTabuleiro(tabuleiro)
