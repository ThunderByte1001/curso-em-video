numero = int(input('Digite um número: ')) #int para ser numero inteiro, este programa só roda com números inteiros!
s = numero - 1 #Equivale ao numero antecessor
d = numero + 1 #Equivale ao numero sucessor
#Aqui o código também podia ser do estilo deste: print("Analisando o seu numero {} o seu antecessor é o {} e o seu sucessor é o número {}!".format(numero, (numero - 1, numero + 1))
print("Analisando o seu numero {} o seu antecessor é o {} e o seu sucessor é o número {}!".format(numero, s, d))