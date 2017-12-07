# UNIVERSIDADE FEDERAL DA FRONTEIRA SUL
#  PROFESSOR: EMILIO WUERGES
#  MATÉRIA: PROGRAMAÇÃO I
#  ALUNO: FELIPE AUGUSTO DA SILVA
#  EMAIL: felipeaugustosilva94@gmail.com
#  DESENVOLVIDO NO AMBIENTE LINUX

# TRABALHO FINAL - Black Jack em Python  

import random

class Deck(object):
    # Pra quando o Ace valer 11
    valor_map = {'J':10, 'Q':10, 'K':10,'A':11}
    #Para quando o Ace valer 1
    valor_map_ace = {'J':10, 'Q':10, 'K':10,'A':1}

    def __init__(self):
        self.deck = []
        self.cria_deck()

    def cria_deck(self):
        suites = ["♣", "♦", "♥", "♠"]
        valores = [str(i) for i in range(2,11)] + ['J', 'Q', 'K', 'A']

        for suite in suites:
            for valor in valores:
                self.deck.append((valor, suite))

    def draw_card(self):
        carta_aleatoria = random.randint(0, len(self.deck)-1)
        return self.deck.pop(carta_aleatoria)
