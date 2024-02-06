soma = 0
contador = 0
contadorImpar = 0

for n in range(1, 501, 2):
    if n % 3 == 0: # and n % 2 != 0: Não é preciso verificar
        print('Esse número é impar e múltiplo de 3: {}'.format(n))
        soma += n
        contador += 1
    contadorImpar += 1

print('A soma de todos esses valores é de: {0}'.format(soma))
print('A quantia de número passado foi de {0}'.format(contador))
print('A quantia de ímpares entre 1 e 500 é de {0}'.format(contadorImpar))