def realiza_jogada(tabuleiro, jogador, coluna, turno):
  #Passa coluna, apenas quando é o jogador 2, para index correto da lista
  if jogador == 1:
    coluna = coluna - 6

  #Faz uma cópia do tabuleiro.
  tabuleiroNovo = tabuleiro

  #Passa a quantidade de peças da casa seleciona para variável pecas.
  pecas = tabuleiroNovo[jogador][coluna]

  #Zera a casa selecionada para a jogada.
  tabuleiroNovo[jogador][coluna] = 0

  #Variável auxiliar para loop de quem esta realizando jogada.
  aux = coluna + 1

  #Variável que armazena o jogador oponente nesta rodada.
  oponente = 1 - jogador

  #Salva a casa em que a ultima peça cai
  ultima_peca = (20, 20)

  #Loop da jogada.
  while pecas > 0:

    #Loop que distribui as peças nas casas e mancala do jogador desta rodada.
    for i in range(aux, 7):
      if pecas <= 0:
        break
      if i == 6:
        tabuleiroNovo[2][jogador] += 1
        pecas -= 1
        ultima_peca = (2, jogador)
        break
      tabuleiroNovo[jogador][i] += +1
      pecas -= 1
      ultima_peca = (jogador, i)

    #Loop que distribui as peças nas casas do jogador oponente.
    for i in range(0, 6):
      if pecas <= 0:
        break
      tabuleiroNovo[oponente][i] += 1
      pecas -= 1
      ultima_peca = (oponente, i)

    aux = 0

  #Salva jogador e coluna de onde cai a ultima peça
  if(ultima_peca != None):
    jogador1, coluna = ultima_peca

  #Caso caia na mancala, jogador tem direito a mais uma jogada
  if jogador1 == 2:
    turno[0] = jogador

  #Caso não caia na mancala, turno vai para proximo jogador
  else:
    turno[0] = 1 - turno[0]

  #Chama função que faz a captura de peça
  captura_peca(tabuleiro,jogador,jogador1,coluna)
  
  #Retorna tabuleiro para ser renderizado.
  return tabuleiroNovo

def verifica_fim(tabuleiro):
  # Soma das peças das casas de cada fileira
  soma_j1 = sum(tabuleiro[0])
  soma_j2 = sum(tabuleiro[1])

  # Se alguma das fileiras não tiver nenhuma peça, retorna o tabuleiro gerado pela função pega_todas_pecas. Caso contrário, retorna o tabuleiro original.
  if soma_j1 == 0 or soma_j2 == 0:
    print("Fim de jogo.")
    return pega_todas_pecas(tabuleiro)
  return tabuleiro

def valida_jogada(tabuleiro, jogador, coluna, turno):
  #Retorna False se casa estiver vazia.
  if coluna < 0:
    return False
  if jogador == 1 and turno == 1:
    if coluna < 6 or tabuleiro[jogador][coluna - 6] == 0:
      return False
    elif 6 <= coluna <= 11:
      return True
  elif jogador == 0 and turno == 0:
    if coluna > 5 or tabuleiro[jogador][coluna] == 0:
      return False
    elif 0 <= coluna <= 5:
      return True  
  else:
    return False

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

def captura_peca(tabuleiro,jogador,jogador2,coluna):
  #Clona o tabuleiro
  tabuleiroNovo = tabuleiro

  #Confere se a ultima peça cai numa casa do jogador daquela rodada
  if jogador != jogador2:
    return tabuleiroNovo
  
  #Confere se cai na mancala
  elif jogador2 == 2:
    return tabuleiroNovo

  #jogador 2 -> 5,4,3,2,1,0
  #jogador 1 -> 0,1,2,3,4,5

  if jogador == 0 and tabuleiroNovo[jogador][coluna] == 1:
    tabuleiroNovo[2][0] += tabuleiroNovo[1][-1*(coluna-5)]
    tabuleiroNovo[1][-1*(coluna-5)] = 0

  elif jogador == 1 and tabuleiroNovo[jogador][coluna] == 1:
    tabuleiroNovo[2][1] += tabuleiroNovo[0][-1*(coluna-5)]
    tabuleiroNovo[0][-1*(coluna-5)] = 0
  
  return tabuleiroNovo