#Validação de dados nestecaso de gêneros 
genero = str(input('Informe o seu gênero: [M/F] ')).strip().upper()[0]
print(genero)
while genero not in 'MF':
    genero = str(input('Dados INVÁLIDOS. Por Favor, informe seu gênero: ')).strip().upper()[0]
print('Gênero {} registrado com Sucesso!'.format(genero))

