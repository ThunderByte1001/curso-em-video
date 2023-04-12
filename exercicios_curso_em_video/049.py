#Tabuada de uma forma mais fácil!!!
from time import sleep
n = int(input('Digite um número para ver a sua tabuada: '))
for c in range(1,11):
    sleep(0.2)
    print('{} x {:2} = {}'.format(n,c,(n*c)))