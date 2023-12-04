import pygame
from tabuleiro import rodar
from regras import mostrar_instrucoes

# Inicialização do Pygame
pygame.init()

# Definição da resolução da janela
resolution = (1400, 800)
tela = pygame.display.set_mode(resolution)
pygame.display.set_caption("Mancala")

# Cores
black = (0, 0, 0)
green = (44, 130, 87)
corTabuleiro = (222, 184, 135)

def draw_button(rect, text):
    pygame.draw.rect(tela, green, rect, border_radius=20)
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, black)
    text_rect = text_surface.get_rect(center=rect.center)
    tela.blit(text_surface, text_rect)

def draw_game_name():
    font = pygame.font.Font(None, 100)
    text_surface = font.render("Mancala", True, black)
    text_rect = text_surface.get_rect(center=(resolution[0] // 2, 200))
    tela.blit(text_surface, text_rect)

# Tamanho da janela
window_width, window_height = resolution

# Definição dos botões
button_width, button_height = 200, 50
button_spacing = 10  # Espaçamento entre botões
button_texts = ["Jogar", "Instruções", "Sair"]  # Adicione mais botões conforme necessário

# Calcula a altura total dos botões e espaçamentos
total_height = len(button_texts) * button_height + (len(button_texts) - 1) * button_spacing

# Calcula a posição inicial vertical dos botões
start_y = (window_height - total_height) // 2

# Lista para armazenar os retângulos dos botões
button_rects = []

# Cria os retângulos dos botões e armazena na lista
for i, text in enumerate(button_texts):
    rect = pygame.Rect((window_width - button_width) // 2, start_y + i * (button_height + button_spacing), button_width, button_height)
    button_rects.append(rect)

# Loop principal
def run():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for rect, text in zip(button_rects, button_texts):
                    if rect.collidepoint(event.pos):
                        if text == "Jogar":
                            rodar()  # Certifique-se de que a função rodar está implementada corretamente
                        elif text == "Instruções":
                            mostrar_instrucoes()
                        elif text == "Sair":
                            running = False

        # Preenche a tela com a cor de fundo
        tela.fill(green)
        pygame.draw.rect(tela, corTabuleiro, (50, 50, window_width - 100, window_height - 100), border_radius=30)

        # Desenha o nome do jogo
        draw_game_name()

        # Desenha os botões
        for rect, text in zip(button_rects, button_texts):
            draw_button(rect, text)

        # Atualiza a tela
        pygame.display.flip()
