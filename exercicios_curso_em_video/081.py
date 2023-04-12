valores = []
cont = 0
while True:
    valor = (int(input(f'Digite um valor: ')))
    questao= ' '
    cont +=1
    if valor in valores:
        print('Este valor já foi escolhido...Não vou adicionar!')
    else:
        print('Valor adicionado com sucesso...')
        valores.append(valor)
        valores == valores.sort(reverse=True)
    while questao not in 'SN':
        questao = str(input('Quer continuar? [S/N]')).strip().upper()
    if questao == 'N':
        break
print('-='*20)
print(f'Os valores em ordem decrescente foram {valores}')
print(f'Foram digitados {cont} números!')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')

