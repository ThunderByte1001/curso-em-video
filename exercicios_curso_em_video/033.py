#Maior e menor valor------Programa abaixo feito por mim apenas com dois valores
#n1 = int(input('Digite o primeiro valor: '))
#n2 = int(input('Digite o segundo valor: '))
#if n1 > n2:
#    print('O maior numero é {}'.format(n1))
#if n2 > n1:
#    print('O maior numero é {}'.format(n2))
#if n1<n2:
#    print('O menor número é {}'.format(n1))
#if n2<n1:
#    print('O menor número é {}'.format(n2))
#else:
 #   print('O menor número é {}'.format())

 #Abaixo o programa feito por professor Gustavo Guanabara com três digitos!
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c= int(input('Digite o terceiro valor: '))
menor = a #Aqui atribui-se logo um menor
if b<a and b<c:
    menor=b # Se 'b' é menor que 'a' e 'b' é menor que 'c', entao o menor é o b
if c<a and c<b:
    menor=c # Se 'c' é menor que 'a' e 'c' é menor que 'b', entao o menor é o c
print('O menor valor digitado foi {}'.format(menor))
maior = b
if c>b and c>a: # Se 'c' é maior que 'b' e 'c' é maior que 'a', entao o maior é o c
    maior=c
if a>b and a>c: # Se 'a' é maior que 'b' e 'a' é maior que 'c', entao o maior é o a
    maior=a
print('O maior valor digitado foi {}'.format(maior))

