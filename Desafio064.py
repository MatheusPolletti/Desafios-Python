# Meu código
'''
soma = contador = num = 0

while num != 999:
    print('\nDigite 999 para parar o sistema!')
    num = int(input('Digite um número inteiro: '))
    if num != 999:
        contador += 1
        soma += num

print('\nVocê digitou {0} números e a soma entre eles é de: {1}'.format(contador, soma))
'''

soma = cont = num = 0
num = int(input('Digite um número, use 999 para parar: '))

while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número, use 999 para parar: '))

print('Digitou {0} números e sua soma é {1}'.format(cont, soma))