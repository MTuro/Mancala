import pygame

WIDTH = 1400
HEIGHT = 800

window_size = (WIDTH, HEIGHT)
tela = pygame.display.set_mode(window_size)
pygame.display.set_caption("Mancala")

corTabuleiro = (222,184,135)
corCasa = (106,75,53)

def desenhaTabuleiro():
    # Tabuleiro
    pygame.draw.rect(tela,corTabuleiro,(50,50,WIDTH-100,HEIGHT-100),border_radius=30)
    pygame.draw.line(tela,(0,0,0),(100,HEIGHT/2),(1300,HEIGHT/2),5)
    pygame.draw.rect(tela,corCasa,(75,100,100,HEIGHT-200),border_radius=30)
    pygame.draw.rect(tela,corCasa,(WIDTH-175,100,100,HEIGHT-200),border_radius=30)

    for i in range(6):
        pygame.draw.rect(tela,corCasa,(185+(175*i),100,155,250),border_radius=30)
        pygame.draw.rect(tela,corCasa,(185+(175*i),450,155,250),border_radius=30)

def atualizaTabuleiro():
    # Cor de fundo
    tela.fill((44, 130, 87))

    # Desenha tabuleiro
    desenhaTabuleiro()
    
    # Atualizar a tela
    pygame.display.flip()