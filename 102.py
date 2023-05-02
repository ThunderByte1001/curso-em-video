def factorial(n, show=False):
    '''
    -> Calcula o fatorial de um número.
    :param n: O número a ser escolhido.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    '''
    if show == 0:
        f = 1
        for c in range(n, 0, -1):
            f *= c
        print(f'{f}')
        return f
    elif show == True:
        f = 1
        for c in range(n, 0, -1):
            f *= c
            if c == 1:
                print(f'{c} = {f}')
            else:
                print(f'{c} x ', end='')
        return f

# Programa principal
factorial(5,show=False)
