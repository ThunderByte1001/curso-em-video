#JOGO DO PEDRA PAPEL OU TESOURA

import random
from time import sleep
computador = random.randint(0,2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogada = int(input('Qual é a sua jogada? '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
sleep(1)

if computador == 0 and jogada == 1:#COMPUTADOR PEDRA JOGADOR PAPEL

    print('''-=--=--=--=--=--=--=--=-
Computador jogou PEDRA
Jogador jogou PAPEL
-=--=--=--=--=--=--=--=-
    JOGADOR VENCE!''')
elif computador == 1 and jogada == 1:#COMPUTADOR PAPEL JOGADOR PAPEL
    print('''-=--=--=--=--=--=--=--=-
Computador jogou PAPEL
Jogador jogou PAPEL
-=--=--=--=--=--=--=--=-
    NINGUEM GANHOU A RONDA!''')
elif computador == 2 and jogada == 1:#COMPUTADOR TESOURA JOGADOR PAPEL
    print('''-=--=--=--=--=--=--=--=-
Computador jogou TESOURA
Jogador jogou PAPEL
-=--=--=--=--=--=--=--=-
    COMPUTADOR VENCE!''')
elif computador == 0 and jogada == 2:#COMPUTADOR PEDRA JOGADOR TESOURA
    print('''-=--=--=--=--=--=--=--=-
Computador jogou PEDRA
Jogador jogou TESOURA
-=--=--=--=--=--=--=--=-
    COMPUTADOR VENCE!''')
elif computador == 2 and jogada == 2:#COMPUTADOR TESOURA JOGADOR TESOURA
    print('''-=--=--=--=--=--=--=--=-
Computador jogou TESOURA
Jogador jogou TESOURA
-=--=--=--=--=--=--=--=-
    NINGUEM GANHOU A RONDA!''')
elif computador == 1 and jogada == 2:#COMPUTADOR PAPEL JOGADOR TESOURA
    print('''-=--=--=--=--=--=--=--=-
Computador jogou PAPEL
Jogador jogou TESOURA
-=--=--=--=--=--=--=--=-
    JOGADOR VENCE!''')
elif computador == 0 and jogada == 0:#COMPUTADOR PEDRA JOGADOR PEDRA
    print('''-=--=--=--=--=--=--=--=-
Computador jogou PEDRA
Jogador jogou PEDRA
-=--=--=--=--=--=--=--=-
    NINGUEM GONHOU A RONDA!''')
elif computador == 1 and jogada == 0:#COMPUTADOR PAPEL JOGADOR PEDRA
    print('''-=--=--=--=--=--=--=--=-
Computador jogou PAPEL
Jogador jogou PEDRA
-=--=--=--=--=--=--=--=-
    COMPUTADOR GANHOU A RONDA!''')
elif computador == 2 and jogada == 0:#COMPUTADOR TESOURA JOGADOR PEDRA
    print('''-=--=--=--=--=--=--=--=-
Computador jogou TESOURA
Jogador jogou PEDRA
-=--=--=--=--=--=--=--=-
    JOGADOR GANHOU A RONDA!''')
else:
    print('Opção \033[31mINVÁLIDA!\033[m')




#elif computador == 1 and jogada == 0:
 #   print('''Computador jogou PAPEL
#Jogador jogou PEDRA
#-=--=--=--=--=--=--=--=-
 #   COMPUTADOR VENCE!''')




#print('-=-'*8)
#print('JOGADOR VENCE!')