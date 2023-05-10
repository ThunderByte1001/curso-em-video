def metade(n=0):
    return n / 2


def dobro(n=0):
    return n * 2


def aumentar(n=0):
    return n + (n * 10 / 100)


def moeda(n=0,moeda='€'):
    return f'{n}{moeda}'.replace('.',',')#O n sendo o valor que a pessoa importa no programa,e a moeda, sendo o tipo de moeda.
    #O replace serve para trocar neste caso o ponto final'.' por uma vírgula','