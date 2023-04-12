import math
n = int(input('Digite um número: '))
dobro = n * 2
triplo = n * 3
raiz = math.sqrt(n)
print('O dobro de {} vale {}'.format(n, dobro))
print("O triplo de {} vale {}".format(n, triplo))
print("A raiz quadrada de {} vale {:.2f}".format(n, raiz)) #Aqui pode-se observar que {:.2f} serve para deixar o número só com duas casas decimáis!