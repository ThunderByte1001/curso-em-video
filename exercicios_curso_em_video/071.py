from time import sleep
print('--'*13)
print('BANCO \033[33mCURSO EM VIDEO\033[m')
print('--'*13)
print('-=--=-PorFavor insira o seu cartão bancário-=--=-')
sleep(5)
print('Processando...')
sleep(2)
código = int(input('Informe a sua senha:(de 4 dígitos) '))
adilia = 2222
daniel = 1111
if código == daniel or código == adilia:
    sleep(2)
    print('\033[31mATENÇÃO!!!\033[m\nNo presente momento,só dá para sacar os seguites valores:\n\033[4:36m5€\033[m,\033[4:34m10€\033[m,\33[4:35m20€\033[m,\033[4:33m30€\033[m,\033[4:32m40€\033[m e \033[4:31m50€\033[m. ')
    sleep(1.5)
    contador50_50 = contador20_20 = contador10_10 = contador1_1 = 0
    while True:
        valor =int(input('Qual o valor que deseja sacar? '))
        if valor == 50:
            contador10_10 = contador10_10 + 1
            contador20_20 = contador20_20 + 2
            print('Processando...')
            sleep(2)
            print(f'Total de {contador10_10} cédulas de 10€')
            sleep(1)
            print(f'Total de {contador20_20} cédulas de 20€')
            sleep(1.5)
            break
        if valor == 10:
            contador10_10 = contador10_10 + 1
            print('Processando...')
            sleep(2)
            print(f'Total de {contador10_10} cédulas de 10€')
            sleep(1.5)
            break
        if valor == 5:
            contador1_1 = contador1_1 +5
            print('Processando...')
            sleep(2)
            print(f'Total de {contador1_1} cédulas de 1€')
            sleep(1.5)
            break
        if valor == 20:
            contador10_10 = contador10_10 + 2
            print('Processando...')
            sleep(2)
            print(f'Total de {contador10_10} cédulas de 10€')
            sleep(1.5)
            break
        if valor == 30:
            contador10_10 = contador10_10 + 1
            contador20_20 = contador20_20 + 2
            print('Processando...')
            sleep(2)
            print(f'Total de {contador10_10} cédula de 10€')
            sleep(1)
            print(f'Total de {contador20_20} cédulas de 20€')
            sleep(1.5)
            break
        if valor == 40:
            contador10_10 = contador10_10 + 2
            contador20_20 = contador20_20 + 1
            print('Processando...')
            sleep(2)
            print(f'Total de {contador10_10} cédulas de 10€')
            sleep(1)
            print(f'Total de {contador20_20} cédula de 20€')
            sleep(1.5)
            break
        if valor != 5 or 10 or 20 or 30 or 40 or 50:

            print('Processando...')
            sleep(1.5)
            print('Opção \033[31mERRADA!!!\033[m')
            sleep(1.5)
            print('Por favor retire o cartão e volte a inseri-lo.')
            sleep(3)
            break
else:
    print('Processando...')
    sleep(1.5)
    print('Senha \033[31mERRADA!!!\033[m')
    sleep(1.5)
    print('Por favor retire o cartão e volte a inseri-lo.')
    sleep(1.5)
sleep(1.5)
print('Volte sempre ao BANCO CURSO EM VIDEO! Tenha um bom dia!')