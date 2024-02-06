# Meu 1.0

'''
dados = dict()

dados['Nome'] = str(input('Digite seu nome: '))
dados['Média'] = float(input(f'Digite a média de {dados["Nome"]}: '))
if dados['Média'] >= 7:
    dados['Situação'] = 'Aprovado'
else:
    dados['Situação'] = 'Reprovado'

print(f'O nome do aluno/aluna é: {dados["Nome"]}\nEle/Ela tem média igual a {dados["Média"]} e a situação foi {dados["Situação"]}')
'''

# Meu 1.1

'''
dados = dict()

no = str(input('Digite seu nome: '))

dados.update({'Nome': no})

media = float(input(f'Digite a média de {dados["Nome"]}: '))

dados.update({'Média': media})

if dados['Média'] >= 7:
    dados.update({'Situação': 'Aprovado'})
else:
    dados.update({'Situação': 'Reprovado'})

print(f'O nome do aluno/aluna é: {dados["Nome"]}\nEle/Ela tem média igual a {dados["Média"]} e a situação foi {dados["Situação"]}')
'''

# Guanabará

aluno = dict()

aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input(f'Média do aluno {aluno["Nome"]}: '))

if aluno['Media'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['Media'] <= 7:
    aluno['Situação'] = 'Recuperação'
else: 
    aluno['Situação'] = 'Reprovado'

for chave, valor in aluno.items():
    print(f'{chave} é igual a {valor}')
