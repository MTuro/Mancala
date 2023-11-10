def realiza_jogada():{
    
}


########################## verifica fim ##################################
jogador1 = [4,4,4,4,4,4,0]
jogador2 = [4,4,4,4,4,4,0]

def somar_elementos(lista):
  soma = 0
  for numero in lista:
    soma += numero
  return soma


soma_jogador1 = somar_elementos(jogador1)
soma_jogador2 = somar_elementos(jogador2)

def verifica_fim():
    if soma_jogador1 == 0 or soma_jogador2 == 0:
        return pega_todas_pecas()
    return
##############################################################################



def valida_jogada():{
    
}

def pega_todas_pecas(tabuleiro):
    # Soma todas as peças de cada jogador, incluindo as peças em suas Mancalas
    soma_final1 = sum(tabuleiro[0]) + tabuleiro[2][0]
    soma_final2 = sum(tabuleiro[1]) + tabuleiro[2][1]

    # Cria um tabuleiro final onde em cada mancala há a quantidade exata de peças que cada jogador possuía na jogada final, e zera as outras casas.
    tabuleiroFinal = [[0]*6,[0]*6,[soma_final1,soma_final2]]

    # A pontuação final de cada jogador é o número de peças em cada Mancala, que pode ser acessado por tabuleiroFinal[2].
    print(f"FIM DE JOGO.\nJogador 1: {tabuleiroFinal[2][0]} pontos.\nJogador 2: {tabuleiroFinal[2][1]} pontos.\n")

    # Print do resultado do jogo.
    if soma_final1 > soma_final2:
      print("O jogador 1 foi o vencedor.")
    elif soma_final1 < soma_final2:
      print("O jogador 2 foi o vencedor.")
    else:
      print("Empate.")

    # Retorna o tabuleiro final para ser renderizado.
    return tabuleiroFinal

def captura_peca ():{
    
}
