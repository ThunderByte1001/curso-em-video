print('\033[0;31;46mOlá, mundo!\033[m')#Comando para mudar as cores do texto e estilo
a = 1
b = 2
nome = 'Daniel'
print('Os valores são \033[31m{}\033[m e \033[34m{}\033[m!'.format(a,b))#Aqui pode-se ver uma maneira de utilizar!
print('Olá outra vez {}{}{}!'.format('\033[4;30;44m',nome,'\033[m'))#Aqui pode-se ver outra maneira de utilizar!
#Outra maneira de utilizar pode ser assim:
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Olá outra vez {}{}{}!'.format(cores['pretoebranco'], nome,cores['limpa']))#Aqui pode-se ver outra maneira de utilizar!