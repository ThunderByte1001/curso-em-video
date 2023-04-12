from time import sleep
print('-=-'*5)
n1 = int(input('Primeiro valor: '))
print('-=-'*5)
n2 = int(input('Segundo valor: '))
print('-=-'*5)
opcao = 0
while opcao != 5:
       print('''[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')
       print('-=-' * 10)
       opcao = int(input('Qual a sua opção? '))
       print('-=-'*10)
       if opcao == 2:
              multiplicaçao = n1 * n2
              sleep(1.5)
              print('\033[40mA multiplicação de {} com {} é {}\033[m'.format(n1, n2, multiplicaçao))
       elif opcao == 1:
              soma = n1 + n2
              sleep(1.5)
              print('\033[40mA soma de {} com {} é de {}\033[m'.format(n1, n2, soma))
       elif opcao == 3:
              if n1 < n2:
                     sleep(1.5)
                     print('\033[40mEntre {} e {} o maior é {}\033[m'.format(n1, n2, n2))
              elif n1 > n2:
                     sleep(1.5)
                     print('\033[40mEntre {} e {} o maior é {}\033[m'.format(n1, n2, n1))
       elif opcao ==4:
              sleep(1.5)
              print('Informe os números novamente:')
              sleep(1.5)
              n1 = int(input('Primeiro valor: '))
              n2 = int(input('Segundo valor: '))
       elif opcao == 5:
              print('-=-'*10)
              print('\033[40mFinalizando...\033[m')
              sleep(2)
              print('-=-'*10)
       else:
              print('\033[40mPorfavor tente outravez, opção\033[m \033[31mERRADA\033[m!')

print('\033[40mFim do programa! Volte sempre!\033[m ')
print('-=-'*10)




