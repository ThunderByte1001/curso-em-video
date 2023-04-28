from time import sleep
novamente = ' '
print('-----------------Tabuada------------------')
for c in range (0,3):
    num = int(input('Qual o valor que deseja ver a sua tabuada? '))
    for c in range(0, 11):
        sleep(0.2)
        print(f'{num} x {c} = {num * c}')










