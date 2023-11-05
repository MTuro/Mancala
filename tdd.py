import unittest
from mancala import realiza_jogada, verifica_fim, valida_jogada, pega_todas_peças, captura_peça

#testa realiza jogada
def test_realiza_jogada():
    tabuleiro = [[4] * 6, [4] * 6, [0, 0]]
    realiza_jogada(tabuleiro, 0, 2)
    assert tabuleiro == [[4, 4, 0, 1, 5, 5], [4] * 6, [0, 0]]

#testa verifica fim
def test_verifica_fim_false():
    tabuleiro = [[4] * 6, [4] * 6, [0, 0]]
    assert not verifica_fim(tabuleiro)

def test_verifica_fim_true():
    tabuleiro = [[0] * 6, [0] * 6, [0, 0]]
    assert verifica_fim(tabuleiro)

#testa valida jogada
def test_valida_jogada_valid():
    tabuleiro = [[4] * 6, [4] * 6, [0, 0]]
    assert valida_jogada(tabuleiro, 0, 2)

def test_valida_jogada_invalid_casa_vazia():
    tabuleiro = [[4] * 6, [4] * 6, [0, 0]]
    assert not valida_jogada(tabuleiro, 0, 5)

def test_valida_jogada_invalid_jogador_1_casa_inferior():
    tabuleiro = [[4] * 6, [4] * 6, [0, 0]]
    assert not valida_jogada(tabuleiro, 1, 2)

def test_valida_jogada_invalid_jogador_2_casa_superior():
    tabuleiro = [[4] * 6, [4] * 6, [0, 0]]
    assert not valida_jogada(tabuleiro, 0, 3)

#testa pega todas as peças
def test_pega_todas_peças():
    tabuleiro = [[0] * 6, [4, 4, 0, 1, 5, 5], [0, 0]]
    pega_todas_peças(tabuleiro, 0)
    assert tabuleiro == [[0] * 6, [0] * 6, [0, 0]]

#testa captura peça
def test_captura_peça():
    tabuleiro = [[0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 0], [0, 0]]
    captura_peça(tabuleiro, 0, 5)
    assert tabuleiro == [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 1]]
    
