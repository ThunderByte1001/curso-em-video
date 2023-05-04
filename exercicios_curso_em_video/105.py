def notas(*n,sit=False):#NÃO ESQUECER!!! O ASTERISTICO '*' SERVE PARA MOSTRAR VÁRIAS INFORMAÇÕES,NESTE CASO NOTAS!
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não indicar a situação do aluno.
    :return: dicionário com várias informações sobre a situação da turma.
    '''
    r = dict()#Dicionário
    r['total'] = len(n)
    r['maior'] = max(n)#Saber o valor máximo
    r['menor'] = min(n)#Saber o valor minímo
    r['media'] = sum(n) / len(n)#A soma de todos os valores em 'n' a dividir pelos número de valores em 'n'
    if sit:# Significa = Se o sit está verdadeiro(True) então...
        if r['media'] >= 10:
            r['situação'] = 'razoável'
        elif r['media'] > 14:
            r['situação'] = 'BOA'
        elif r['media'] < 10:
            r['situação'] = 'MÁ'
        elif r['media'] <= 5:
            r['situação'] = 'TERRÍVEL!±'
    return r#Retorna o r


#Programa Principal
resp = notas(10.6, 10.0, 14.6, 9.5,sit=True)# Aqui a 'sit' tem de ser assim = 'sit=True', e não SÓ True, porque se colocar só True, este não demonstra a situação na totalidade.
print(resp)
#help(notas)
#Este exercício demonstra uma solução diferente da solução apresentada pelo professor Gustavo Guanabara.
#Aqui a situação da turma está com valores diferentes escolhidos por mim.