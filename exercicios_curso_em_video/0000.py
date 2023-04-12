#n1 = int(input('Digite um número: '))
#n2 = int(input('Digite outro número: '))
#if n1 > n2:
 #   print(f'{n1} é maior que {n2}')
#else:
 #   print(f'{n2} é maior que {n1}')


from random import randint
v1 = randint(0,10)
v2 = randint(0,10)
print(f'Os valores sorteados foram: {v1} {v2}')
if v1 > v2:
    print(f'O maior número é o {v1}')
else:
    print(f'O maior número é {v2}')
if v1 < v2:
    print(f'O menor número é {v1}')
else:
    print(f'O menor número é {v2}')