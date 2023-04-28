def area(num1,num2):
    a = num1 * num2
    print(f'A área de um terreno {num1}x{num2} é de {a}m²')

def titulo(txt):
    print(txt)
    print('-'*30) 
 
#Programa principal
titulo('Controlo de Terrenos')
num1 = float(input('LARGURA (M): '))
num2 = float(input('COMPRIMENTO (M): '))
area(num1,num2)