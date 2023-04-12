from random import randint
from time import sleep
from random import randint
print('...')
sleep(1)
print('Olá eu sou a \033[31mBESTA\033[m')
sleep(1)
print('...')
sleep(1)
print('Vou pensar em um número de 0 a 5...')
sleep(1)
print('...')
sleep(2)
print('Acredito que não vais conseguir adivinhar \033[31mHAHAHA\033[m')
sleep(1.5)
maquina = randint(0,5)
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é o teu palpite? '))
    palpite = palpite + 1
    if jogador == maquina:
        acertou = True
    else:
        if jogador < maquina:
            print('Mais...Tente mais uma vez.')
        elif jogador > maquina:
            print('Menos...Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpite))





