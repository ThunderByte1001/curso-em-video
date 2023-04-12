#Contagem regressiva para fogo de artifício
from time import sleep
for c in range(10, -1,-1):
    sleep(1)
    print(c)
sleep(1)
print('BUM! BUM! POOOW!')