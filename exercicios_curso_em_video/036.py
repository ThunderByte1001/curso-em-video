casa = float(input('Valor da casa: '))
salario = float(input('Salário do comprador: '))
anos = int(input('Quantos anos de financiamento? '))
prestaçao = casa / (anos * 12)
print('Para pagar uma casa de {:.2f}€ em {} anos'.format(casa, anos))

