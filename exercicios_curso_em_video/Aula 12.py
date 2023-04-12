#Condições aninhadas!!!
nome = str(input('Qual é seu nome?'))
if nome == "Daniel":
    print('Que nome bonito!'.format(nome))
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Joao':# elif pode ser colocado as vezes que se quiser!!!
    print('O seu nome é bem popular em Portugal!')
elif nome in 'Joaquim Manuel António de Sousa':
    print('Belo nome que você tem!')
elif nome in 'Adilia Joana Ana Jucefina':
    print('Belo nome feminino!')
else: # Apenas pode-se utilizar uma vez ou nenhuma!!!
    print('O seu nome é bem normal!')
print('Tenha um bom dia, {}!'.format(nome))