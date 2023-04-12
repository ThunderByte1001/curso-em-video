alturamaior = 0
alturamenor = 0
for p in range(1,5):
    altura = float(input('Qual a altura da {}ª pessoa: '.format(p)))
    if p ==1:
        alturamaior = altura
        alturamenor = altura
    else:
        if altura > alturamaior:
            alturamaior = altura
        if altura < alturamenor:
            alturamenor = altura
print('A altura maior é de {:.2f}m.'.format(alturamaior))
print('A altura menor é de {:.2f}m.'.format(alturamenor))
