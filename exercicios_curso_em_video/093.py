from time import sleep
dados = dict()
dados['nome'] = str(input('Nome do Jogador: '))
dados['partidas'] = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
gols_por_partida = []
total_de_gols = 0
for c in range(0, dados['partidas']):
    gol = int(input(f'Quantos gols na partida {c+1}? '))
    gols_por_partida.append(gol)
    total_de_gols += gol
dados['gols'] = gols_por_partida
goles = gols_por_partida
dados['total'] = total_de_gols
print('-='*30)
sleep(1)
print(dados)
print('-='*30)
for k, v in dados.items():
    sleep(0.3)
    print(f'O campo {k} tem o valor {v}')

print('-='*30)
sleep(0.3)
print(f'O jogador {dados["nome"]} jogou {dados["partidas"]} partidas.')
for i,v in enumerate(dados['gols']):
    sleep(0.3)
    print(f' => Na partida {i}, fez {v} gols.')
sleep(0.3)
print(f'Foi um total de {total_de_gols} gols.')