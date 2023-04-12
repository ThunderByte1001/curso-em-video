pares = list()
impares = list()
valores = list()
for v in range(1,8):
    valor = int(input(f'Digite o {v}º valor: '))
    if valor % 2 == 0:
        pares.append(valor)
        pares.sort()
    else:
        impares.append(valor)
        impares.sort()
    numeros_pares_ordenados= valores.sort()
print('-='*25)
print(f'Os valores pares digitados foram: {pares}')
print(f'Os valores ímpares digitados foram {impares}')



