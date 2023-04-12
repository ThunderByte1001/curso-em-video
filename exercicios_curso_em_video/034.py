salario = float(input('Qual é o salário do funcionário? '))
if salario > 1000:
    novo = salario + (salario * 10 / 100)
if salario <= 1000:
    novo = salario + (salario * 15 / 100)
print('Quem ganhava cerca de \033[35m{:.2f}\033[m, passa a ganhar \033[36m{:.2f}\033[m agora!'.format(salario,novo ))
