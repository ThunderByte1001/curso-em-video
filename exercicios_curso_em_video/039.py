#Alistamento Militar
ano = int(input('Ano de nascimento: '))#qual o ano de nascimento
idade = 2023 - ano #Saber a idade da pessoa
print('Quem nasceu no ano de {} tem {} anos em 2023.'.format(ano,idade))
alistamento = ano + 18 #Saber o ano do alistamento
anos = 2023 - alistamento #Á quanto tempo ja devia se ter alistado
if idade > 18: #Se idade for maior que 18
    print('Você já deveria ter se alistado há {} anos.'.format(anos))
    print('Seu alistamento foi em {}.'.format(alistamento))
elif idade == 18: # Se idade for igual a 18
    print('Você deve-se alistar neste ano.')

else: #Se idade for abaixo de 18
    print('Seu alistamento será em {}.'.format(alistamento))