lista1 = list()
lista2 = list()
lista3 = list()
for p in range(0, 3):
    valor = int(input(f'Digite um valor para [0, {p}]: '))
    lista1.append(valor)
for p in range(0, 3):
    valor2 = int(input(f'Digite um valor para [1, {p}]: '))
    lista2.append(valor2)
for p in range(0, 3):
    valor3 = int(input(f'Digite um valor para [2, {p}]: '))
    lista3.append(valor3)
print('-='*30)
print(f'[{lista1[0]:^5}]',f'[{lista1[1]:^5}]',f'[{lista1[2]:^5}]')
print(f'[{lista2[0]:^5}]',f'[{lista2[1]:^5}]',f'[{lista2[2]:^5}]')
print(f'[{lista3[0]:^5}]',f'[{lista3[1]:^5}]',f'[{lista3[2]:^5}]')
