from random import randint
v1 = randint(0,10)
v2 = randint(0,10)
v3 = randint(0,10)
v4 = randint(0,10)
v5 = randint(0,10)
valores = [f'Os valores sorteados foram: {v1} {v2} {v3} {v4} {v5}']
print(valores)
maior_numero = max(v1,v2,v3,v4,v5)
menor_numero = min(v1,v2,v3,v4,v5)
#if v1 > v2 and v1>v3 and v1>v4 and v1>v5:        Esta maneira também funciona mas ocupa muito mais espaço,
 #   print(f'O maior número é o {v1}')            mas, não detecta o maior numero quando temos dois maiores numeros iguais.
#elif v2 > v3 and v2>v1 and v2>v4 and v2>v5:
 #   print(f'O maior número é o {v2}')
#elif v3 > v2 and v3>v1 and v3>v4 and v3>v5:
 #   print(f'O maior número é o {v3}')
#elif v4 > v2 and v4>v1 and v4>v3 and v4>v5:
 #   print(f'O maior número é o {v4}')
#elif v5 > v2 and v5>v1 and v5>v4 and v5>v3:
   # print(f'O maior número é o {v5}')

#-----------------//------------------------
#if v1 < v2 and v1<v3 and v1<v4 and v1<v5:         Esta maneira também funciona mas ocupa muito mais espaço,
 #   print(f'O menor número é o {v1}')             mas, não detecta o menor numero quando temos dois menores numeros iguais.
#elif v2 < v3 and v2<v1 and v2<v4 and v2<v5:
 #   print(f'O menor número é o {v2}')
#elif v3 < v2 and v3<v1 and v3<v4 and v3<v5:
#    print(f'O menor número é o {v3}')
#elif v4 < v2 and v4<v1 and v4<v3 and v4<v5:
#    print(f'O menor número é o {v4}')
#elif v5 < v2 and v5<v1 and v5<v4 and v5<v3:
 #   print(f'O menor número é o {v5}')
print(f'O maior número é {maior_numero}')
print(f'O menor número é {menor_numero}')




