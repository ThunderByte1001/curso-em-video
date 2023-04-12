valores = []
while True:
    valor = (int(input(f'Digite um valor: ')))
    questao= ' '
    if valor in valores:
        print('Este valor já foi escolhido...Não vou adicionar!')
    else:
        print('Valor adicionado com sucesso...')
        valores.append(valor)
        valores == valores.sort()
    while questao not in 'SN':
        questao = str(input('Quer continuar? [S/N]')).strip().upper()
    if questao == 'N':
        break
print('-='*20)
print(f'Os valores foram {valores}')



