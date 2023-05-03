def ficha(jogo='<desconhecido>',gol= 0):
    print(f'O jogador {jogo} fez {gol} gol(s) no campeonato.')


#Programa Principal
nome = str(input('Nome do jogador: '))
gols = str(input('Número de gol(s): '))
if gols.isnumeric():#ver se o numero digitado é um numero
    gols= int(gols)#Se for realmente um numero escreve-se o numero com int
else:#Senao for um numero atribui-se como '0' como está representado na linha de baixo
    gols = 0
if nome.strip() == '':#Se eu tirei todos os espaços com o strip, e ele ficou vazio
    ficha(gol=gols) #Chame-se a ficha para este ficar igual ao 'gols'
else:#Se nao ficar vazio mesmo com o strip entao chama-se a ficha com nome e gols
    ficha(nome,gols)