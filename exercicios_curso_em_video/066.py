n = soma = cont = 0
while True:#Enquanto estiver verdadeiro
    n = int(input('Digite um valor: '))
    if n == 999:
        break#aCABA O PROGRAMA
    cont += 1
    soma = soma + n
print(f'A soma dos {cont} valores é de \033[32m{soma}\033[m!')
print('\033[31mAcabou\033[m')