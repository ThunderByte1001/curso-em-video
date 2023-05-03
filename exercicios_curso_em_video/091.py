from time import sleep
from random import randint
from operator import itemgetter
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}
ranking = list()
print('valores sorteados:')
for key,valor in jogo.items():
    print(f'{key} tirou {valor} no dado.')
    sleep(1)
print('-='*16)
print('  == RANKING DOS JOGADORES ==')
ranking = sorted(jogo.items(),key=itemgetter(1),reverse=True)#O sorted serve para por em crescente
for i, v in enumerate(ranking):# o 'i' é o índice e o 'v' é o valor
    print(f'    {i+1} lugar: {v[0]} com {v[1]}.')
    sleep(1)
