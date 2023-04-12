lista = list()
dado = list()
pessoas = maior = menor =0
while True:
    dado.append(str(input('Nome: ')))
    pessoas += 1
    dado.append(float(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    lista.append(dado[:])
    dado.clear()
    questao = str(input('Quer continuar? ')).strip().upper()[0]
    if questao == 'N':
        break
print('-='*20)
print(f'Ao todo,você cadastrou {pessoas} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de', end='')
for p in lista:
    if p[1] == maior:
        print(f' [{p[0]}]', end='')
print()
print(f'O menor peso foi de {menor}Kg. Peso de', end='')
for p in lista:
    if p[1] == menor:
       print(f' [{p[0]}] ', end='')
print()

