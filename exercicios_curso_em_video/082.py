num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um valor: ')))
    questao = str(input('Quer continuar? [S/N]')).strip().upper()
    if questao == 'N':
        break
for i,v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 ==1:
        impares.append(v)
print(f'A lista completa é {num}')
print(f'A lista dos pares é {pares}')
print(f'A lista dsos impares é {impares}')