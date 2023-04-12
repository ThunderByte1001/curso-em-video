#Média um pouco mais trabalhosa
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1+n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é de {:.1f} valores'.format(n1, n2, media))
if media < 9.5:
    print('O aluno está reprovado!')
elif media >= 10.0 and media <= 11.9:#Metodo de recuperação não utilizado em portugal, apenas fiz com valores há minha escolha pois, gosto de fazer exercicios iguais ao professor Guanabara!
    print('O aluno está em recuperação!')
else:
    print('O aluno está aprovado!')
