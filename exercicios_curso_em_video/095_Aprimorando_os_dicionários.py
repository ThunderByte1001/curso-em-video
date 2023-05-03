#programa que consiste em perguntar nome de jogadores, quantas partidas cada um fez,e quantos golos cada um fez por partida.
from time import sleep
dados = dict()
time = list()
dados_2= dict()
resp = ' '
while True:
    dados.clear()
    dados['nome'] = str(input('Nome do jogador: '))
    dados['partidas'] = int(input(f'Quantas partidas {dados["nome"]}, jogou? '))
    #dados['nome'] =
    gols_por_partida = []
    total_de_gols = 0

    for c in range(dados['partidas']):
        gol = int(input(f'Quantos gols na partida {c + 1}? '))
        gols_por_partida.append(gol)
        total_de_gols += gol

    dados['gols'] = gols_por_partida
    dados['total'] = total_de_gols

    time.append(dados.copy())
    while True:
            resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
            if resp in 'SN':
                break
            print('Opção inválida. Por favor, responda S ou N.')

    if resp == 'N':#Este 'if' tem de estar sempre fora do while True associado ao questionamento se o usuario quer continuar ou não!
        break#Porque se estive-se dentro do while True, este não serviria para o objetivo pretendido que é encerrar o programa!
print('-='*30)
print('cod ', end='')
for i in  dados.keys():
    sleep(0.5)
    print(f'{i:<15}', end='')
print()
print('-='*30)
for k, v in enumerate(time):
    sleep(0.5)
    print(f'{k:>3}', end='')
    for d in v.values():
        sleep(0.5)
        print(f'{str(d):<15}', end='')
    print()

print('-='*30)
sleep(0.8)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERROU! Não existe jogador com código {busca}!')
    else:
        sleep(0.8)
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            sleep(0.3)
            print(f'   No jogo {i} fez {g} gols.')
    print('-='*30)
    sleep(0.8)
print('<< VOLTE SEMPRE >>')




