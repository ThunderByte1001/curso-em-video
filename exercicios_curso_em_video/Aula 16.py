lanche = ('Hamburger','Suco','Pizza','Bolo','Batata Frita')#Aqui temos uma tupla!
#del(lanche)    del()...Serve para apagar uma variavel
for comida in lanche:
    if comida != lanche[1]:#Se comida for difente da posição 1(Suco),mostrar o print abaixo
        print(f'Vou comer {comida}!')#Este
    else:#Senão
        print(f'Vou beber {comida}!')#Aqui para a posição 1(Suco)só para trocar o comer por beber
print(len(lanche),end='')#Aqui demosnstra quantas posições esta tupla tem
print(' Posições')
for pos, comida in enumerate(lanche):#Aqui enumera a posição 'pos' sendo a posição
    if comida != lanche[1]:
        print(f'Eu vou comer {comida} na posição {pos}')
    else:
        print(f'Eu vou beber {comida} na posição {pos}')
print(sorted(lanche))#Por ordem alfabética
print('Comi bué!')
a = (5,4,3,2) #Tupla com números
b = (1,0)
c = a + b #É como se cola-se as duas tuplas não somando!
d = b + a # Cola as duas tuplas, mas agora a primeira tupla neste caso sendo o b
print(c)
print(d)
print(c.count(5))#Contara quantas vezes um número aparece dentro de 'c',neste caso apenas 1 vez!
print(c.index(3))#Mostra em que posição está o número solicitado apenas na primeira ocorrência

