import pygame

from src.tabuleiro import Tabuleiro

pygame.init()

LARGURA = 800
ALTURA = 800


tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Xadrez Python")

tabuleiro = Tabuleiro(tela)

rodando = True

while rodando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tabuleiro.desenhar()

    pygame.display.flip()

pygame.quit()