num = int(input('Qual o primeiro valor: '))
num2 = int(input('Qual o segundo valor: '))
açao = 0

while açao != 5:
    açao = int(input('Somar[1]\n'
                     'Multiplicar [2]\n'
                     'Subtrair[3]\n'
                     'Novos números[4]\n'
                     'Sair do programa[5]\n'
                     'Oque deseja: '))
    if açao == 1:
        print(f'A soma de {num} + {num2} é {num + num2}')

    elif açao ==2:
        print(f'A multiplicação de {num} e {num2} é de {num*num2}')

    elif açao ==3:
        print(f'A subtração de {num} e {num2} é de {num - num2}')

    elif açao == 4:
        num = int(input('Qual o primeiro valor: '))
        num2 = int(input('Qual o segundo valor: '))
    elif açao == 5:
        print('Acabou')
        break
    else:
        print('\033[40mPorfavor tente outravez, opção\033[m \033[31mERRADA\033[m!')
print('\033[40mFim do programa! Volte sempre!\033[m ')
print('-=-'*10)




