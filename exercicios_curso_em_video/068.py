from random import randint
from time import sleep
v = 0
print('-=-'*10)
print('Jogo do PAR ou ÍMPAR')
print('-=-'*10)
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'IiPp':
        sleep(0.2)
        tipo = str(input('Par ou ÍMPAR? [P/I]')).strip().upper()[0]
        sleep(0.3)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}',end='')
    sleep(0.2)
    print(' DEU \033[36mPAR!\033[m'if total % 2 ==0 else ' DEU \033[35mÍMPAR!\033[m')
    sleep(0.2)
    if tipo == 'P':
        if total % 2 == 0:
            print('Você \033[32mVENCEU!!!\033[m')
            v += 1
        else:
            print('Você \033[31mPERDEU!!!\033[m')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você \033[32mVENCEU!!!\033[m')
            v += 1
        else:
            print('Você \033[31mPERDEU!!!\033[m')
    print('Vamos jogar novamente')
print('GAME OVER! Você ganhou {} vezes!'.format(v))
