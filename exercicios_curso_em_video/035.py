#Analisar se três segmentos de reta conseguekm formar um triângulo!
print('-='*15)
print('Analisador de Triângulos')
print('-='*15)
n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input(('Terceiro segmento: ')))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else: #Se a soma for
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
