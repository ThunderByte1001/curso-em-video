pessoa = dict()
galera = list()
soma = idade = 0
pessoas = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    pessoas += 1
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Errou! Por favor, digite apenas M ou F!')
    pessoa['idade'] = int(input('Idade: '))
    soma = soma + pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('Errou! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-='*30)
print(f'O grupo tem {pessoas} pessoas.')
media = soma / len(galera)
print(f'A média de idades do grupo é de {media:5.2f} anos')
print('As mulheres cadastradas foram ',end='')
for p in galera:
    if p['sexo'] in 'F':
        print(f' {p["nome"]}',end='')
print()
print('Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('   ',end='')
        for k,v in p.items():
            print(f'{k} = {v};',end='')
        print()
print('<< ENCERRADO >>')



