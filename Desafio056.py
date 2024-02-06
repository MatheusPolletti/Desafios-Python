# Código que eu fiz

mulheres = maisVelho = media = 0

for i in range (1, 5):
    nome = str(input('Digite o seu nome: ')).strip().lower()
    idade = int(input('Digite a sua idade em anos: '))
    sexo = str(input('Digite F para femino e M para masculino: ')).strip().lower()
    media += idade
    if i == 1 and sexo == 'm':
        maisVelho = idade
        nomeMaisVelho = nome
    if sexo == 'm' and idade > maisVelho:
        maisVelho = idade
        nomeMaisVelho = nome
    if sexo == 'f' and idade < 20:
        mulheres += 1

print('A idade média do grupo é de {0} anos'.format(media / 4))
print('O nome do homem mais velho é {0} com idade de {1} anos'.format(nomeMaisVelho.capitalize(), maisVelho))
print('O grupo tem {0} mulheres com menos de 20 anos'.format(mulheres))

'''
Código do guanabará
somaIdade = 0
mediaIdade = 0
maiorIdade = 0
nomeVelho = ''
totalMulher = 0

for p in range(1, 5):
    print('Você é a pessoa {}°'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('M ou F: ')).strip().upper()
    somaIdade += idade
    if p == 1 and sexo in 'Mm':
        maiorIdade = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdade:
        maiorIdade = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totalMulher += 1


mediaIdade = somaIdade / 4
print('A média de idade do grupo é de {0}'.format(mediaIdade))
print('O homem mais velho tem {0} anos e se chama {1}'.format(maiorIdade, nomeVelho))
print('A quantia de mulher com menos de 20 anos são de {0}'.format(totalMulher))
'''