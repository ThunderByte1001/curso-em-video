from random import randint
maquina = randint(0,1)
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpite = palpite + 1
    if jogador == maquina:
        acertou = True
    else:
        if jogador < maquina:
            print('Mais...Tente mais uma vez.')
        elif jogador > maquina:
            print('Menos...Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpite))
