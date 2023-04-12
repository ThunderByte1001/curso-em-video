from random import randint
from time import sleep
computador = randint(0,5) #Aqui o computador esta a pensar de uma forma random o nº que vai escolher
print('--=--=--=--=--=----=--=--=--=--=----=--=--=--=--=--')
print('Vou pensar em um número de 0 a 5.Tente adivinhar...')
print('--=--=--=--=--=----=--=--=--=--=----=--=--=--=--=--')
n = int(input('Em que número eu pensei?')) #Aqui o jogador tenta adivinhar oque o nº em que o computador pensou
print('PROCESSANDO...')
sleep(2)
if n == computador: #Se o nº que o jogador escreveu corresponder ao que o computador pensou-
    print('Parabéns acertaste, pensei no número {}!'.format(computador)) #Tem aqui os seus parabéns!
else: # Senão acertou-
    print('Errouuu! Pensei no numero {} e não no {}!'.format(computador, n)) #Computador diz que o jogador errou!
