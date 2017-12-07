# UNIVERSIDADE FEDERAL DA FRONTEIRA SUL
#  PROFESSOR: EMILIO WUERGES
#  MATÉRIA: PROGRAMAÇÃO I
#  ALUNO: FELIPE AUGUSTO DA SILVA
#  EMAIL: felipeaugustosilva94@gmail.com
#  DESENVOLVIDO NO AMBIENTE LINUX

# TRABALHO FINAL - Black Jack em Python

from Deck import *

class Player(object):
    def __init__(self):
        self.mao = []
        self.derrota = False

    def valor_mao(self):
        # Faz a soma dos valores das cartas com o maior valor do Ace
        valor_alto_ace = [
            Deck.valor_map[card[0]] if card[0] in Deck.valor_map else
            int(card[0]) for card in self.mao
        ]

        #  Faz a soma dos valores das cartas com o menor valor de Ace
        valor_baixo_ace = [
            Deck.valor_map_ace[card[0]] if card[0] in Deck.valor_map_ace else
            int(card[0]) for card in self.mao
        ]

        # Sempre returna o menor valor para o jogador
        if sum(valor_alto_ace) > 21:
            return sum(valor_baixo_ace)
        else:
            return sum(valor_alto_ace)
