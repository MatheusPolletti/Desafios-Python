# Meu

'''from datetime import date

pessoa = dict()

pessoa['Nome'] = str(input('Digite o seu nome: ')).strip().title()

anoNascimento = int(input('Digite o seu ano de nascimento: '))
anoAtual = date.today().year
pessoa['Idade'] = anoAtual - anoNascimento

pessoa['CarteiraTrabalho'] = int(input('Digite a sua carteira de trabalho(Caso não tenha digite 0): '))

if pessoa['CarteiraTrabalho'] > 0:
    pessoa['AnoContratação'] = int(input('Digite o seu ano de contratação: '))
    pessoa['Salário'] = float(input('Digite o seu salário: '))
    aposentadoria = anoAtual - pessoa['AnoContratação']
    aposentadoriaSoma = 35 - aposentadoria 
    aposentadoriaIdade = aposentadoriaSoma + pessoa['Idade']
    pessoa['Aposentadoria'] = aposentadoriaIdade
    

if pessoa ["CarteiraTrabalho"] == 0:
    print(f'O nome da pessoa é: {pessoa['Nome']}')
    print(f'A sua idade é de {pessoa['Idade']} anos')
    print(f'O seu ctps tem valor de {pessoa["CarteiraTrabalho"]}')
else:
    print(f'O nome da pessoa é: {pessoa['Nome']}')
    print(f'A sua idade é de {pessoa['Idade']} anos')
    print(f'O seu ctps tem valor de {pessoa["CarteiraTrabalho"]}')
    print(f'O ano de contratação da pessoa é {pessoa['AnoContratação']}')
    print(f'O salário da pessoa é R${pessoa["Salário"]}')
    print(f'A pessoa vai se aposentar ao {pessoa['Aposentadoria']}')'''

# Guanabará

from datetime import datetime # Novo forma

dados = dict()


dados['Nome'] = str(input('Nome: ')).strip()
nasc = int(input('Ano de nascimento: '))
dados['Idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Digite sua carteira de trabalho(0 não tem): '))

if dados['ctps'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salario'] = float(input('Salário: '))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Contratação'] + 35) - datetime.now().year)

for chave, valor in dados.items():
    print(f'{chave} tem o valor {valor}')