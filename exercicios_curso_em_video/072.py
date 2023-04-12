n = int(input('Digite um número de 0 a 20: '))
numeros = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treoze','catorze','quinze','desaseis','desasete','desoito','desanove','vinte')

while n <= 20:
    for cont in (numeros):
        print(f'Você digitou o número {numeros[n]}')
        break
    break
while not n<=20:
    print('Opção \033[31mERRADA!\033[m')
    n = int(input('Digite um número de 0 a 20: '))
    if n <=20:
        print(f'Você digitou o número {numeros[n]}')
        break
