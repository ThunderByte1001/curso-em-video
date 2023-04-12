#Conversor de números inteiros para binario, octal, hexadecimal!!!
n = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão: ')
print('[1] converter para BINÁRIO ')
print('[2] converter para OCTAL')
print('[3] converter para HEXADECIMAL')
y = '%o' % n
base = int(input('Sua opção: '))
if base == 1:
    print(bin(n)[2:])
elif base == 2:
    print(y)
elif base == 3:
    print(hex(n)[2:])
else:
    print('Opção inválida. Tente novamente.')



