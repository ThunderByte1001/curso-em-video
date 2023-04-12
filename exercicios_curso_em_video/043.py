print('Olá, aqui é o lugar ídeal para descobrir se o seu peso está dentro do peso ídeal!')
nome = str(input('Por favor, diga-nos o seu nome: '))
print('Muito Obrigado, {}!'.format(nome))
peso = float(input('Qual é o seu peso? (kg) '))
altura = float(input('Qual é a sua altura? (m)'))
imc = peso / (altura * altura)
print('O IMC dessa pessoa é de {:.2f}'.format(imc))
if imc < 18.5:
    print('Está abaixo do peso! ')
elif imc >= 18.5 and imc < 25:
    print('Está com o peso ídeal!')
elif imc >= 25 and imc < 30:
    print('SOBREPESO!')
elif imc >= 30 and imc < 40:
    print('OBESIDADE!')
else:
    print('MUITO CUIDADO!! OBESIDADE MÓRBIDA!!!')