distancia = int(input('Qual é a distância da sua viagem? '))
print('Você esta prestes a começar uma viagem de {:.1f}km.'.format(distancia))
n = 0.50 * distancia
if n <= 200:
    print('O preço é de: {:.2f}€'.format(n))
else:
    print('O preço é de: {:.2f}€'.format(0.45*distancia))
