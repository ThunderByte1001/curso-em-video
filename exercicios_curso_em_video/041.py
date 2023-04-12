ano = int(input('Ano de nascimento: '))
anos = 2023 - ano
print('O atleta tem {} anos'.format(anos))
if anos <= 9:
    print('Classificação: MIRIM.')
elif anos > 9 and anos <= 14:
    print('Classificação: INFANTIL.')
elif anos > 14 and anos <= 19:
    print('Classificação: JUNIOR.')
elif anos > 19 and anos <= 20:
    print('Classificação: SÊNIOR.')
else:
    print('Classificação: MASTER.')