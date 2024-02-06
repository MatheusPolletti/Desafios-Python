nome = str(input('Digite o seu nome completo: ')).strip()

print('O seu nome em maiúsculas é {0}'.format(nome.upper()))
print('O seu nome em minúsculas é {0}'.format(nome.lower()))

# Como eu fiz
# x = len(nome)
# y = nome.count(' ')
# tamanho = x - y
# print('O tamanho da frase é de {0} letras'.format(tamanho))

print('O tamanho da frase é de {0} letras'.format(len(nome) - nome.count(' ')))

# Como eu fiz
# corte = nome.split()
# tamanho2 = len(corte[0])
# print('O seu primeiro nome é {0} e ele tem {1} letras'.format(corte[0], tamanho2))


print('Seu primeiro nome tem {0} letras'.format(nome.find(' ')))
