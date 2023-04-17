pessoas = {'Nome':'Gustavo','sexo':'M','idade':22}
print(f'O {pessoas["Nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())# Mostra as chaves dentro de pessoas
print(pessoas.values())# Mostra os valores dentro de pessoas
print(pessoas.items())# Mostra as chaves e os valores dentro de pessoas
for k in pessoas.keys():# Aqui o 'k' equivale a keys(chaves)= para cada chave em pessoas, mostra cada chave (Tradução)
    print(k)
for v in pessoas.values():# 'v' valores
    print(v)
for k,v in pessoas.items(): #'k' e 'v' chaves e valores
    print(f'{k} = {v}')
del pessoas['sexo']#Aqui apaga a chave sexo e o seu valor
pessoas['Nome'] = 'Leandro'# Muda o valor da chave 'Nome' que era Gustavo, para Leandro
pessoas['peso'] = 87.5 #Adiciona mais uma chave e um valor ao final da estrutura pessoas!
print(pessoas)
brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf':'São Paulo', 'Sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(brasil)#Lista com dicionários
print(brasil[0]['uf'])# Forma de mostrar os valores das chaves de cada elemento
print(brasil[1]['Sigla'])
print(brasil[1])
print(brasil[0])
estado= dict()
brasil1 = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla']= str(input('Sigla do Estado: '))
    brasil1.append(estado.copy())
for e in brasil:#Este 'e' vem de estado
    for k1,v1 in e.items():
        print(f'O campo {k1} tem valor {v1}.')


