from time import sleep
def contagem10(txt):
    print('-='*30)
    print(txt)



contagem10('Contagem de 1 até 10 de 1 em 1')
for c in range(1,11):
    sleep(0.3)
    print(c ,end=' ')
sleep(0.3)
print('FIM!')

contagem10('Contagem de 10 até 0 de 2 em 2')
for x in range(10,0,-1):
    if x % 2 == 0:
        sleep(0.3)
        print(x,end=' ')

sleep(0.3)
print('0',end=' ')
print('FIM!')
#Aqui
contagem10('Agora é sua vez de personalizar a contagem!')

inicio = 0
fim = 0
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem10(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
for c in range(inicio, fim+1 , passo):#+1
    sleep(0.3)
    print(c, end=' ')

if inicio > fim:
    for c in range(fim,inicio+1,passo):#-1
        sleep(0.3)
        print(c, end=' ')
if inicio > fim:
    print(f'{fim}',end=' ')
print('FIM!')
contagem10('')


