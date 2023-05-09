from ex109 import moeda

p = float(input('Digite o preço: '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p,True)}')#Se for colocado o 'True' o valor fica formatado com '€'
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p,False)}')#Se colocar 'False' o valor fica do jeito que foi inserido sem formatação
print(f'Aumentado 10%, temos {moeda.aumentar(p,True)}')
