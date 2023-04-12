import pygame
import random

# Inicializa o Pygame
pygame.init()

# Define as cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)

# Define o tamanho da tela
LARGURA = 400
ALTURA = 400

# Define o tamanho do bloco
TAMANHO_BLOCO = 10

# Cria a tela
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo da Cobrinha")


# Função para desenhar a cobra
def desenhar_cobra(lista_cobra):
    for bloco in lista_cobra:
        x = bloco[0]
        y = bloco[1]
        pygame.draw.rect(tela, VERDE, [x, y, TAMANHO_BLOCO, TAMANHO_BLOCO])


# Função para gerar comida aleatória
def gerar_comida():
    x = round(random.randrange(0, LARGURA - TAMANHO_BLOCO) / 10.0) * 10.0
    y = round(random.randrange(0, ALTURA - TAMANHO_BLOCO) / 10.0) * 10.0
    return (x, y)


# Função principal do jogo
def jogo():
    # Define a posição inicial da cobra
    pos_x = LARGURA / 2
    pos_y = ALTURA / 2

    # Define o movimento inicial da cobra
    mov_x = 0
    mov_y = 0

    # Cria a lista da cobra
    cobra = []
    tamanho_cobra = 1

    # Gera a primeira comida
    comida_x, comida_y = gerar_comida()

    # Loop principal do jogo
    jogo_ativo = True
    while jogo_ativo:
        # Verifica se o jogador quer sair
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogo_ativo = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    mov_x = -TAMANHO_BLOCO
                    mov_y = 0
                elif evento.key == pygame.K_RIGHT:
                    mov_x = TAMANHO_BLOCO
                    mov_y = 0
                elif evento.key == pygame.K_UP:
                    mov_x = 0
                    mov_y = -TAMANHO_BLOCO
                elif evento.key == pygame.K_DOWN:
                    mov_x = 0
                    mov_y = TAMANHO_BLOCO

        # Move a cobra
        pos_x += mov_x
        pos_y += mov_y

        # Verifica se a cobra atingiu a parede
        if pos_x < 0 or pos_x > LARGURA - TAMANHO_BLOCO or pos_y < 0 or pos_y > ALTURA - TAMANHO_BLOCO:
            jogo_ativo = False

        # Verifica se a cobra comeu a comida
        if pos_x == comida_x and pos_y == comida_y:
            comida_x, comida_y = gerar_comida()
            tamanho_cobra += 1

        # Atualiza a lista da cobra
        cabeca_cobra = []
        cabeca_cobra.append(pos_x)
