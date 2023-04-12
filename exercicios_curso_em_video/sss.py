
from random import choice
print(' {:=^50} '.format(' Adivinhe a palavra ! '))
lista = ['abelha', 'macaco', 'matemática', 'livro', 'praia', 'leão', 'celular', 'triângulo', 'história', 'capitalismo']
palavra_secreta1 = choice(lista)
dica1 = input(' Você vai querer uma dica ? ').lower()
if palavra_secreta1 == 'abelha':
    dica2 = ' A sua dica é : Amarelo e preto '
    nps = ' A palavra secreta tem 6 letras '
elif palavra_secreta1 == 'macaco':
    dica2 = ' A sua dica é : Evolução humana '
    nps = ' A palavra secreta tem 6 letras '
elif palavra_secreta1 == 'matemática' or palavra_secreta1 == 'matematica':
    dica2 = ' A sua dica é : Pesadelo de muitos na escola '
    nps = ' A palavra secreta tem 10 letras '
elif palavra_secreta1 == 'livro':
    dica2 = ' A sua dica é : Conhecimento '
    nps = ' A palavra secreta tem 5 letras '
elif palavra_secreta1 == 'praia':
    dica2 = ' A sua dica é : Férias '
    nps = ' A palavra secreta tem 5 letras '
elif palavra_secreta1 == 'leão' or palavra_secreta1 == 'leao':
    dica2 = ' A sua dica é : Rei '
    nps = ' A palavra secreta tem 4 letras '
elif palavra_secreta1 == 'celular':
    dica2 = ' A sua dica é : Sem isso, sem vida '
    nps = ' A palavra secreta tem 7 letras '
elif palavra_secreta1 == 'triângulo' or palavra_secreta1 == 'triangulo':
    dica2 = ' A sua dica é : Forma ge...'
    nps = ' A palavra secreta tem 9 letras '
elif palavra_secreta1 == 'história' or palavra_secreta1 == 'historia':
    dica2 = ' A sua dica é : Passado '
    nps = ' A palavra secreta tem 10 letras '
elif palavra_secreta1 == 'capitalismo':
    dica2 = ' A sua dica é : Right '
    nps = ' A palavra secreta tem 11 letras '
if dica1 == 'Sim' or dica1 == 'sim' or dica1 == 'SIM':
    print(dica2)
else:
    print(' Então vamos direto ao jogo ! ')
print('\n Tente adivinhar a palavra (Regras) : \n Se você pediu dica : \n Você terá 3 chances para adivinhar a palavra \n Se você não pediu dica : \n Você terá 5 chances para adivinhar a palavra ')
print('\n A sua palavra tem {} '.format(nps))
if dica1 == 'sim':
    n1a = str(input(' Tente adivinhar a palavra: ')).strip()
    if n1a == palavra_secreta1:
        print(' Parabéns ! Você ganhou ! ')
    elif n1a != palavra_secreta1:
        print(' Você errou! ')
        n2a = str(input(' Tente novamente: ')).strip()
        if n2a == palavra_secreta1:
            print(' Parabéns ! Você ganhou ! ')
        elif n2a != palavra_secreta1:
            print(' Você errou .')
            n3a = str(input(' Sua última tentativa: ')).strip()
            if n3a == palavra_secreta1:
                print(' Parabéns ! Você ganhou ! ')
            elif n3a != palavra_secreta1:
                print(' Você perdeu \n A palavra era {} '.format(palavra_secreta1))
else:
    n1b = str(input(' Tente adivinhar a palavra: '))
    if n1b == palavra_secreta1:
        print(' Parabéns ! Você ganhou ! ')
    elif n1b != palavra_secreta1:
        print(' Você errou ')
        n2b = str(input(' Tente novamente: '))
        if n2b == palavra_secreta1:
            print(' Parabéns ! Você ganhou !')
        elif n2b != palavra_secreta1:
            print(' Você errou  ')
            n3b = str(input(' Tente novamente: '))
            if n3b == palavra_secreta1:
                print(' Parabéns ! Você ganhou !')
            elif n3b != palavra_secreta1:
                print(' Você errou ')
                n4b = str(input(' Tente novamente: '))
                if n4b == palavra_secreta1:
                    print(' Parabéns ! Você ganhou ! ')
                elif n4b != palavra_secreta1:
                    print(' Você errou  ')
                    n5b = str(input(' Sua última tentativa: '))
                    if n5b == palavra_secreta1:
                        print(' Parabéns ! Você ganhou ! ')
                    elif n5b != palavra_secreta1:
                        print(' Você perdeu  \n A palavra era {} '.format(palavra_secreta1))