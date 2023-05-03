def leiInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))# Começa-se dizendo que a mensagem 'msg' é str para que quando o individuo coloca tipo um número não aparecer logo a mensagem de erro, do python!
        if n.isnumeric():#Se o numero 'n' for numérico,
            valor = int(n)# então o valor que era str passa int desta forma!
            ok = True
        else:
            print('\033[31mDigite um número válido!\033[m')
        if ok:#Se está tudo ok...
            break# Pára!
    return valor


#Programa Principal
n = leiInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')