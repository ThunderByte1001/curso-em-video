#Tabuada ifinita de valores escolhidos, acabando quando se digita um número inferior a 0!!!
from time import sleep
n = 0
while True:
    print('----------------------------------')
    sleep(0.2)
    n = int(input('Quer ver a tabuada de qual valor? '))
    if 0 > n:
        break
    for c in range(1, 11):
        sleep(0.3)
        print('{} x {:2} = {}'.format(n, c, n*c))
sleep(0.3)
print('Acabou')