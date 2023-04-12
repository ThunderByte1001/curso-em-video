'''teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:]) # Estes dois pontos fazem uma cópia
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)'''
'''galera = [['Joao', 19], ['Ana', 16], ['Joaquim',70]]
print(galera[0]) #Amostrará oque fica dentro da primeira lista nesta caso a 0 que é Joao e os 19
print(galera)#Amostrará toda a lista
print(galera[2][1])#Amostrará o elemento 1 da celula 2 neste caso o 70
print(galera[-1][1])#Amostrará também o 70 pois o '-1' equivale á ultima celula
for p in galera:
    print(p[0])#Amostra o nome das pessoas da lista 'galera'
for pi in galera:
    print(f'{pi[0]} tem {p[1]} anos de idade!')'''
galera = list()
dado = list()
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])#Faz toda a diferença!
    dado.clear()
