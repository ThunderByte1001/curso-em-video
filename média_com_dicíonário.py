from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['escolariedade'] = int(input('Ano de escolariedade: '))
#3print(dados)
dados['1ºNota'] = float(input('A 1ºNota: '))
dados['2ºNota'] = float(input('A 2ºNota: '))
soma = dados['1ºNota'] + dados['2ºNota']
dados['media'] = soma / 2
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
if dados['media'] > 10:
        print('APROVADO!')
else:
    print('REPROVADO!')
print(dados)