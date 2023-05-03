from time import sleep
lista = []
cont= 0
n = ''
while True:
    n = int(input('Digite um número para ver a sua tabuada: '))
    cont = cont +1
    tabuada = []
    for c in range(1,11):
        sleep(0.2)
        print('{} x {:2} = {}'.format(n,c,(n*c)))
    lista.append(tabuada)
    questao = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if questao == 'N':
        sleep(0.7)
        print('Finalizando...')
        sleep(1)
        print('Até uma próxima!')
        break
print(f'Ao todo foram apresentadas {cont} tabuadas dos numeros {lista}.')
