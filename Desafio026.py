frase = str(input('Digite uma frase desejada: ')).lower().strip().replace('á', 'a')

# Quantas vezes aparece o A
print('A letra A aparece {0} vezes na frase'.format(frase.count('a')))

# Primeira vez que aparece
print('A primeira vez que a letra A apareceu foi na posição {0}'.format(frase.find('a') + 1))

# Última vez que aparece
print('A última letra A apareceu na posição {0}'.format(frase.rfind('a') + 1))