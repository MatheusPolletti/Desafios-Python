somaI = somaP = 0
contI = contP = 0

for n in range (1, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        print('Esse número é par')
        contP += 1
        somaP += num
    else:
        print('Esse número é ímpar')
        somaI += num
        contI += 1

print('\n\033[32m')
print('A soma de {0} números pares é de: {1}'.format(contP, somaP))
print('A soma de {0} números impares é de: {1}'.format(contI, somaI))
print('\033[m\n')