'''cont = 1
while cont <= 10:
    print(cont, '-> ',end='')
    cont += 1
print('ACABOU')'''
"""n = 0
cont = 0
soma = 0"""
'''while cont<5:
    n = int(input('Digite um número:' ))
    cont +=1
    soma = soma + n
print('{}numeros e {}vezes'.format(soma,cont))'''
'''while n != 999: # Enquanto o 'n' for diferente de 999 perguntar um numero vezes infinitas até ser digitado o nº 999
    n = int(input('numero: '))#Aqui pede-se o numero
    soma += n# visto a cima ter dado como valor 0 á soma entao aqui exemplefiquei que a soma é igual á soma + o 'n'
soma = soma - 999#Para no final a soma ser apenas contabilizada pelos numeros digitados, e não ser adicionado o 999,CONTINUACÃO LINHA ABAIXO!! 
print('A soma vale {}'.format(soma))#exemplefiquei que soma é igual a soma menos o 999!'''#Aqui vemos uma maneira de fazermos um programa de soma
numero = soma = 0
while True:
    numero = int(input('Número: '))
    if numero == 999:#Se o numero for igual a 999 o programa acaba com o 'break'
        break #Quando se utiliza o 'break' quebra-se o programa, acabando-o
    soma += numero
print('A soma vale {}'.format(soma))
#----------------f string!!!-----------------------
#print(f'A soma vale {soma}')
#nome = 'José'
#idade = 33
#salario = 1000
#print(f'O {nome} tem {idade} anos.')#Nova maneira de se fazer PYTHON 3.6+
#print('O {} tem {} anos.'.format(nome,idade))#maneira normal de se fazer PYTHON 3
#print('O %s tem %d anos.'% (nome,idade))#maneira antiga de se fazer PYTHON 2
#print(f'O {nome} tem {idade} anos e ganha {salario}€')