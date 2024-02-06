# Meu

'''def notas(*notaFuncao, situacaoFuncao = False):
    """
    Funcao que calcula a maior, menor e nota média de um aluno, assim como determina sua situação se pedido
    Parâmetros:
    *notaFuncao -> quantidade variável de notas
    *SituacaoFuncao ->  opcional, indica se deve ou não ser mostrado a situação do aluno
    *return -> Dicionário listaAluno com total de notas, maior, menor, média e situação se pedido
    """
    listaAluno = dict()
    maior = menor = 0
    for indice, valor in enumerate(notaFuncao):
        if indice == 0:
            maior = menor = valor
        else:
            if valor > maior:
                maior = valor
            elif valor < menor:
                menor = valor
    media = sum(notaFuncao) / len(notaFuncao)
    listaAluno['Total'] = len(notaFuncao)
    listaAluno['Maior Nota'] = maior
    listaAluno['Menor Nota'] = menor
    listaAluno['Média de Notas'] = media
    if situacaoFuncao:
        if media >= 7:
            listaAluno['Situação'] = 'Boa'
        elif 5 <= media < 7:
            listaAluno['Situação'] = 'Razoável'
        else:
            listaAluno['Situação'] = 'Ruim' 
    return listaAluno


resposta = notas(3.5, 2, 6.5, 2, 7, 4, situacaoFuncao = True)
print(resposta)

help(notas)'''

# Guanabará

def notas(*n, sit = False):
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n) / len(n)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'Boa'
        elif r['Média'] >= 5:
            r['Situação'] = 'Razoável'
        else:
            r['Situação'] = 'Ruim'
    return r

resp = notas(2.5, 1.5, sit = True)
print(resp)