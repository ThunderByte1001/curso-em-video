#nome = str(input('Qual é o seu nome? ')) #Exemplo de uso dos if e do else!
#if nome =='Daniel':
 #   print('Que nome lindo que você tem!')
#else:
 #   print('Prazer em te conhecer {}!'.format(nome))

#print('Bom dia {}!'.format(nome))
n1 = float(input('Digite a primeira nota: ')) #Outro exemplo de uso do if e do else!
n2 = float(input('Digite a sugunda nota: '))
m = (n1 + n2) / 2
print('A média das duas notas foi de {:.2f}'.format(m))
if m >= 10.0:#NÃO ESQUECER OS DOIS PONTOS!!!!-----ATENÇÃO-----
    print('Parabéns, conseguiu tirar positiva!')
else:
    print('Talvez numa proxima consiga tirar positiva, ESTUDE MAIS!')
