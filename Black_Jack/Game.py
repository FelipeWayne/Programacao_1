# UNIVERSIDADE FEDERAL DA FRONTEIRA SUL
#  PROFESSOR: EMILIO WUERGES
#  MATÉRIA: PROGRAMAÇÃO I
#  ALUNO: FELIPE AUGUSTO DA SILVA
#  EMAIL: felipeaugustosilva94@gmail.com
#  DESENVOLVIDO NO AMBIENTE LINUX

# TRABALHO FINAL - Black Jack em Python  

from Player import *


class Game(object):
    def __init__(self):
        self.dealer = Player()
        self.player = Player()
        self.deck = Deck()
        self.gameover = False
        self.player_turno = True

    def start(self):
        self.game_setup()
        self.ler_mao()

        self.player_jogada()
        self.dealer_jogada()

        self.avaliar_final()

    def avaliar_final(self):

        self.ler_ambas_mao()
        print ("*****************************************")
        if self.player.derrota:
            print ('Você perdeu com ' + str(self.player.valor_mao()))
        elif self.dealer.derrota:
            print ('Dealer perdeu com ' + str(self.dealer.valor_mao()))
        elif self.dealer.valor_mao() >= self.player.valor_mao():
            print ('Você tem ' + str(self.player.valor_mao()))
            print ('O Dealer tem ' + str(self.dealer.valor_mao()))
            print ('Você perdeu!')
        else:
            print ('Você tem ' + str(self.player.valor_mao()))
            print ('O Dealer tem ' + str(self.dealer.valor_mao()))
            print ('Você ganhou!')


    def player_jogada(self):

        while self.player_turno and not self.gameover:

            move = self.decisao_player()

            if move == 'n':
                self.player_turno = False
            else:
                self.distribuir_carta(self.player, self.deck.draw_card())
                self.player.derrota = self.verifica_derrota(self.player)
                self.gameover = self.player.derrota

            print ("*****************************************")
            self.ler_mao()
            print ("*****************************************")

    def dealer_jogada(self):
        while not self.dealer.derrota and not self.gameover:

            if self.dealer.valor_mao() < 17:
                self.distribuir_carta(self.dealer, self.deck.draw_card())
                self.dealer.derrota = self.verifica_derrota(self.dealer)
                self.gameover = self.dealer.derrota
            else:
                self.gameover = True

    def verifica_derrota(self, player):
        if player.valor_mao() > 21:
            return True
        else:
            return False

    # Pergunta para o jogador se ele deseja mais uma carta ou não
    def decisao_player(self):
        print ('Deseja mais uma carta (S/N)? ')

        while True:
            resposta = input('> ').lower()
            if resposta == 's' or resposta == 'n':
                return resposta
            else:
                print ('Resposta invalida')

    def ler_mao(self):
        print ('O jogador tem ' + ', '.join([carta[0] + carta[1] for carta in self.player.mao]))
        print ('O Dealer tem ' + self.dealer.mao[0][0] + self.dealer.mao[0][1])

    def ler_ambas_mao(self):
        print ('O jogador tem ' + ', '.join([carta[0] + carta[1] for carta in self.player.mao]))
        print ('O Dealer tem ' + ', '.join([carta[0] + carta[1] for carta in self.dealer.mao]))

    def game_setup(self):
        print ("*****************************************")
        print ("Vamos jogar BlackJack!")

        for i in range(0,2):
            self.distribuir_carta(self.dealer, self.deck.draw_card())
            self.distribuir_carta(self.player, self.deck.draw_card())

    def distribuir_carta(self, player, carta_aleatoria):
        player.mao.append(carta_aleatoria)
