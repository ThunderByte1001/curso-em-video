v = float(input('Qual a velocidade atual do carro? '))
coima = (v-90) * 5
if v <= 90:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('Multado! Você excedeu o limete que é 90km/h! A sua coima é de {:.2f}€!'.format(coima))