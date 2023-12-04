import pygame

def mostrar_instrucoes():
    # Inicialização do Pygame
    pygame.init()

    # Definição da resolução da janela
    resolution = (1400, 800)
    tela = pygame.display.set_mode(resolution)
    pygame.display.set_caption("Instruções")

    # Cores
    black = (0, 0, 0)
    green = (44, 130, 87)
    corTabuleiro = (222, 184, 135)

    # Regras do Mancala
    regras_mancala = (
        "Regras do Mancala:",
        "",
        "1. Objetivo do Jogo:",
        "   - Capturar mais pedras do que o oponente.",
        "",
        "2. Tabuleiro:",
        "   - Dois lados, cada um com seis poços e uma Mancala.",
        "",
        "3. Início do Jogo:",
        "   - Inicialmente, quatro pedras são colocadas em cada poço.",
        "",
        "4. Turno do Jogador:",
        "   - Os jogadores alternam os turnos.",
        "   - Em seu turno, um jogador escolhe um de seus poços e colhe todas as pedras dele.",
        "   - O jogador então coloca uma pedra em cada poço em sentido anti-horário, pulando a Mancala do oponente.",
        "",
        "5. Captura de Pedras:",
        "   - Se a última pedra do turno do jogador cair em sua própria Mancala, ele recebe um turno extra.",
        "   - Se a última pedra for colocada em um poço vazio do jogador, ele captura todas as pedras no poço oposto, além da pedra que foi originalmente colocada.",
        "",
        "6. Fim do Jogo:",
        "   - O jogo termina quando todos os poços de um jogador estão vazios.",
        "   - O jogador que ainda tem pedras em seus poços coleta todas as pedras restantes.",
        "   - O jogador com mais pedras em sua Mancala no final é o vencedor.",
        "",
        "7. Empate:",
        "   - Um empate ocorre se ambos os jogadores tiverem a mesma quantidade de pedras no final.",
        ""
    )

    # Loop principal
    rodando = True
    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if voltar_button_rect.collidepoint(event.pos):
                    rodando = False  # Se o botão "Voltar" for clicado, encerra o loop

        # Preenche a tela com a cor de fundo
        tela.fill(green)
        pygame.draw.rect(tela, corTabuleiro, (50, 50, 1400 - 100, 800 - 100), border_radius=30)

        # Desenha o conteúdo das instruções
        font = pygame.font.Font(None, 24)
        y_position = 100
        for linha in regras_mancala:
            text = font.render(linha, True, black)
            text_rect = text.get_rect(left=100, top=y_position)
            tela.blit(text, text_rect)
            y_position += 20

        # Desenha o botão "Voltar"
        font = pygame.font.Font(None,36)
        voltar_button_rect = pygame.Rect((resolution[0] - 200) // 2, resolution[1] - 125, 200, 50)
        pygame.draw.rect(tela, green, voltar_button_rect, border_radius=20)
        voltar_text = font.render("Voltar", True, black)
        voltar_text_rect = voltar_text.get_rect(center=voltar_button_rect.center)
        tela.blit(voltar_text, voltar_text_rect)

        # Atualiza a tela
        pygame.display.flip()
