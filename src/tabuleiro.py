import pygame

class Tabuleiro:

    def __init__(self, tela):
        self.tela = tela

        self.tamanho = 800
        self.tamanho_casa = self.tamanho // 8

    def desenhar(self):

        for linha in range(8):
            for coluna in range(8):

                if (linha + coluna) % 2 == 0:
                    cor = (240, 217, 181)
                else:
                    cor = (181, 136, 99)

                x = coluna * self.tamanho_casa
                y = linha * self.tamanho_casa

                pygame.draw.rect(self.tela, cor, (x, y, self.tamanho_casa, self.tamanho_casa))

