def voto(nascimento):#Aqui na definição coloquei a variavel nascimento dentro da definição voto() porque assim, ja posso chamar a definição para o programa principal!
    ano_atual = 2023
    idade = ano_atual - nascimento

    if idade < 18:# Se a idade for menor que 18 anos... o individuo nao vota
        print(f'Com {idade} anos: ',end='')
        return "Não vota!"
    elif idade >= 65:# senao, a idade for maior ou igual a 65 anos... o voto fica opcional!
        print(f'Com {idade} anos o ', end='')
        return "Voto é Opcional!"
    else:# Aqui o resto é obviamente a questão de o individuo ter mais de 18 anos e menos de 65!
        print(f'Com {idade} anos: ', end='')
        return "Voto obrigatório!"


nascimento = int(input("Em que ano você nasceu? "))
print(voto(nascimento))
