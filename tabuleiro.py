import pygame
from partida import realiza_jogada, verifica_fim, valida_jogada

WIDTH = 1400
HEIGHT = 800

window_size = (WIDTH, HEIGHT)
tela = pygame.display.set_mode(window_size)

pygame.display.set_caption("Mancala")

pygame.font.init()
font = pygame.font.Font(None,50)


corTabuleiro = (222,184,135)
corCasa = (106,75,53)

def verificaClique(tabuleiro,pos,turno):
    x, y = pos[0], pos[1]
    casa = -1
    jogador = -1

    # Converte a coordenada x do clique numa casa de 0 a 5.
    if x >= 185 and x <= 1215 and y >= 100 and y <= 700:
        if x <= 340:
            casa = 0
        elif x > 360 and x <= 515:
            casa = 1
        elif x > 535 and x <= 690:
            casa = 2
        elif x > 710 and x <= 865:
            casa = 3
        elif x > 885 and x <= 1040:
            casa = 4
        elif x > 1060 and x <= 1215:
            casa = 5

        # Detecta a fileira clicada a partir da coordenada y.
        # Dependendo da fileira clicada, mantém a casa igual ou a converte para um intervalo de 6 até 11, para as casas da fileira superior.
        if y > 450:
            jogador = 0
        elif y < 350 and casa >= 0:
            jogador = 1
            casa = 11 - casa
        else:
            casa = -1
    
    # Printa a casa se for clicada corretamente, e retorna um erro se a região clicada for fora de uma casa.
    if valida_jogada(tabuleiro,jogador,casa,turno):
        #Lista criada para turno poder ser alterado dentro da realiza jogada
        turno_lista = [0]
        turno_lista[0] = turno
        realiza_jogada(tabuleiro,jogador,casa,turno_lista)
        turno = turno_lista[0]
        return turno
    else:
        print(f'x,y = {x,y}')
        print('Selecione uma casa valida.')
        return turno

def desenhaPecaCasa(qtd,x,y):
    tela.blit(font.render(str(qtd), True, (255,0,0)),(x,y))

    for i in range(qtd):
        pos = i//4
        pygame.draw.circle(tela,(255,255,255),(x+20+30*(i%4),y+50+(25*pos)),12)
        pygame.draw.circle(tela,(255,0,0),(x+20+30*(i%4),y+50+(25*pos)),10)

def desenhaPecaMancala(qtd,x,y):
    tela.blit(font.render(str(qtd), True, (255,0,0)),(x,y-5))
    
    for i in range(qtd):
        pos = i//2
        pygame.draw.circle(tela,(255,255,255),(x+20+30*(i%2),y+50+(25*pos)),12)
        pygame.draw.circle(tela,(255,0,0),(x+20+30*(i%2),y+50+(25*pos)),10)


def desenhaTabuleiro(tabuleiro):
    # Tabuleiro
    pygame.draw.rect(tela,corTabuleiro,(50,50,WIDTH-100,HEIGHT-100),border_radius=30)
    pygame.draw.line(tela,(0,0,0),(100,HEIGHT/2),(1300,HEIGHT/2),5)

    # Mancala da esquerda
    pygame.draw.rect(tela,corCasa,(75,100,100,HEIGHT-200),border_radius=30)
    desenhaPecaMancala(tabuleiro[2][1],85,110)

    #Mancala da direita
    pygame.draw.rect(tela,corCasa,(WIDTH-175,100,100,HEIGHT-200),border_radius=30)
    desenhaPecaMancala(tabuleiro[2][0],WIDTH-165,110)

    #Casas
    for i in range(6):
        pygame.draw.rect(tela,corCasa,(185+(175*i),100,155,250),border_radius=30)
        desenhaPecaCasa(tabuleiro[1][5-i],190+(175*i),110)
        pygame.draw.rect(tela,corCasa,(185+(175*i),450,155,250),border_radius=30)
        desenhaPecaCasa(tabuleiro[0][i],190+(175*i),460)

def atualizaTabuleiro(tabuleiro):
    # Cor de fundo
    tela.fill((44, 130, 87))

    # Desenha tabuleiro
    desenhaTabuleiro(tabuleiro)
    
    # Atualizar a tela
    pygame.display.flip()

def rodar():

    tabuleiro = [[4]*6,[4]*6, [0, 0]]
    dicionario = {}
    turno = 0
    partida = 1

    pygame.init()

    # Loop do jogo
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                turno = verificaClique(tabuleiro,pygame.mouse.get_pos(),turno)
                tabuleiro, dicionario, partida = verifica_fim(tabuleiro, dicionario, partida)

        atualizaTabuleiro(tabuleiro)
