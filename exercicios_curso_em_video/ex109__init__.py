def dobro(n=0, formato=False):
    res = n * 2
    return res if formato is False else moeda(res)


def aumentar(n=0, formato=False):
    res = n + (n * 10 / 100)
    return res if formato is False else moeda(res)


def moeda(n=0, moeda='€'):
    return f'{n}{moeda}'.replace('.',
                                 ',')  # O n sendo o valor que a pessoa importa no programa,e a moeda, sendo o tipo de moeda.
    # O replace serve para trocar neste caso o ponto final'.' por uma vírgula','