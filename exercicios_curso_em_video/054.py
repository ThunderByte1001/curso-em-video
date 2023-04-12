#Saber quantas pessoas são maiores de idade e menores de idade
totmaior = 0 #Aqui fica a zero para cada vez que se encontra neste caso uma pessoa de maioridade,adicionar mais 1
totmenor = 0
for c in range(1,8):
    ano = int(input('Em que ano a {}ª pessoa nasceu?'.format(c)))
    if 2023 - ano >= 18: #se o ano atual é 2023 entao 2023 menos o ano escolhido acima se for maior ou igual a 18 é maioridade!
        totmaior += 1 # aqui também podia ser asssim: totmaior = totmaior + 1

    elif 2023 - ano < 18:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(totmaior))
print('E também tivemos {} pessoas menores de idade.'.format(totmenor))