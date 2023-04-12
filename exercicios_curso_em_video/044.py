preço = float(input('Preço das compras: '))
print('''FORMAS DE PAGAMENTO 
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input('Qual é a opção?'))
desconto =  preço - (preço * 10 / 100)
desconto2 = preço - (preço * 5 / 100)
juro = preço +(preço* 20 /100)
if opção == 1:
    print('Sua compra de {}€ vai custar {:.2f}€ no final.'.format(preço,desconto))
elif opção == 2:
    print('Sua compra de {}€ vai custar {:.2f}€ no final.'.format(preço, desconto2))
elif opção == 3:
    print('Sua compra de {}€ continua a custar {:.2f}€ no final.'.format(preço,preço))
elif opção == 4:
    parcelas = int(input('Quantas parcelas:'))
    totalpar = juro / parcelas
    print('A sua compra sera parcelada em {}x de {:.2f}€ COM JUROS!'.format(parcelas,totalpar))
    print('Sua compra de {}€ fica a custar {:.2f}€ pelo motivo dos 20% de juros!'.format(preço, juro))
else:
    print('\033[31mOpção NEGADA!\033[m Por Favor tente novamente!')
