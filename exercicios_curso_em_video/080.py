valores = []
for c in range(0,5):
    valor = int(input('Digite um valor: '))
    if c == 0 or valor > valores[-1]:
        valores.append(valor)
    else:
        pos = 0
        while pos < len(valores):
            if valor <= valores[pos]:
                valores.insert(pos,valor)
                break
            pos += 1
print('-='*30)
print(f'Os valores digitados em ordem foram {valores}')




