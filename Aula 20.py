# FUNCÕE
'''def titulo(txt):
    print('-'*30)
    print(txt)
    print('-'*30)


#Programa Principal
titulo('   CURSO EM VÍDEO   ')
titulo('   Agora é que é    ')'''


'''def soma(a,b):#Defenição ou Função
    print(f'A = {a} e B = {b}')
    s = a +b
    print(f'A soma de A + B = {s}')


#Programa principal
print('<< Soma de somente dois valores >>')
soma(4,5)
soma(b=5,a=4)#outra maneira de fazer e dar o mesmo
soma(7,8)'''

'''def soma(* valores): #Maneira de somar mais de dois valores ao mesmo tempo
    s = 0
    for num in valores:
        s +=num
    print(f'Somando os valores {valores} temos {s}')


soma(5,2)
soma(2,9,4)'''









'''def contador(* num):
    for valor in num:
        print(f'{valor} ', end='')
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')



contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)'''

'''def dobra (lista):
    pos = 0
    while pos< len(lista):
        lista[pos]*=2
        pos += 1

valores = [7,2,5,0,4]
print(valores)
print('Valores dobrados abaixo')
dobra(valores)
print(valores)
print('-'*30)
outros = [4,5,2,8,9]
dobra(outros)
print(outros)'''
def multiplicacao(num1,num2):
    print(f'A = {num1} e B = {num2} ')
    m = num1 * num2
    print(f'O produto de {num1} e {num2} é {m}')

def titulo(txt):
    print('-'*30)
    print(txt)
    print('-'*30)
num1 = int(input('Qual o primeiro valor: '))
num2 = int(input('Qual o segundo valor: '))

titulo('<< O programa da multiplicação >>')
multiplicacao(num1,num2)

