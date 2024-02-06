'''
genero = str(input('Digite o seu gênero: [M/F] ')).strip().upper()

while genero not in 'MF':
        print('O genêro digitado não é valido.')
        genero = str(input('Digite o gênero novamente. [M/F] ')).strip().upper()

print('O seu gênero é {0}'.format(genero))
'''

# Guanabará fez assim

sexo = str(input('Digite seu sexo, sendo [M/F]: ')).strip().upper()[0]

while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]

print('Sexo registrado com sucesso. {0}'.format(sexo))