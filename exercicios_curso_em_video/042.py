n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input(('Terceiro segmento: ')))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos acima PODEM FORMAR um triângulo ',end='')
    if n1 == n2 == n3:#TODOS OS LADOS IGUAIS
        print('Equilátero!')
    if n1 != n2 and n2 != n3:
        print('Escaleno!')
    else:
        print('Isosceles')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO!')
