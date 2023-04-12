n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('O número {} é maior que o {}.'.format(n1,n2))
elif n1 < n2:
    print('O número {} é maior que o {}.'.format(n2,n1))
else:
    print('Os números {} e {} são iguais!'.format(n1,n2))
