def contador(i,f,p):
    '''
    ->Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    '''
    c = i
    while c <= f:
        print(f'{c}',end='..')
        c += p
    print('FIM!')

def somar(a,b,c=0):# Aqui como se pode observar o 'c' recebe o 0 de modo a que pode-se fazer uma soma de só dois numeros!
    s = a+b+c
    print(f'A soma de {a} com {b} e {c} vale {s}')


def subtrair(a=0,b=0,c=0):
    sub = a - b - c
    print(f'A subtração de {a} com {b} e {c} é {sub}')
    print(f'A subtração vale {sub}')


contador(0,10,1)
help(contador)
somar(3,5,6)
somar(3,5)
subtrair(45,3)
subtrair(70,30,3)
subtrair(6,5)
subtrair(a=5,b=2)
print('-='*25)
def funçao():
    n1 = 4
    print(f'N1 dentro vale {n1}')


n1 = 2
funçao()
print(f'N1 fora vale {n1}')



