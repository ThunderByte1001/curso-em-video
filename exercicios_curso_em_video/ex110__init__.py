def metade(n=0, formato= False):
    res =  n / 2
    return res if formato is False else moeda(res)


def dobro(n=0,formato = False):
     res = n * 2
     return res if formato is False else moeda(res)


def aumentar(n=0,taxa = 0,formato = False):
    res = n + (n * taxa / 100)
    return res if formato is False else moeda(res)


def reduzir(n= 0,taxa_1 = 0,formato=False):
    res = n - (n * taxa_1 / 100)
    return res if formato is False else moeda(res)


def moeda(n=0,moeda='€'):
    return f'{n}{moeda}'.replace('.',',')#O n sendo o valor que a pessoa importa no programa,e a moeda, sendo o tipo de moeda.
    #O replace serve para trocar neste caso o ponto final'.' por uma vírgula','


def preço(n = 0,formato=False):
    res = n
    return res if formato is False else moeda(res)
def resumo(n=0,taxa = 0,taxa_1 = 0):

    print('-'*25)
    print('     Resumo do Valor')
    print('-'*25)
    print(f'Preço analisado: \t{preço(n,True)}')#A '\t' é para ajustar os valores todos ao mesmo nível!
    print(f'Dobro do preço: \t{dobro(n,True)}')
    print(f'Metade do preço: \t{metade(n,True)}')
    print(f'{taxa}‰ de aumento: \t{aumentar(n,taxa,True)}')
    print(f'{taxa_1}% de redução: \t{reduzir(n,taxa_1,True)}')
    print('-'*24)





