from time import sleep

def maior(* num):
    print('-='*25)
    cont=maior=0
    print('\nAnalisando os valores passados... ')
    sleep(0.3)
    for valor in num:
        print(f'{valor} ',end='',flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor> maior:
                maior=valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


maior(3,4,10,2)
maior(2,11,4)
maior(5)
maior()