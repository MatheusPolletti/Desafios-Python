n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))

if n1 == n2:
    print('Os dois valores são iguais, sendo eles {0}'.format(n1))
elif n1 > n2:
    print('O primeiro valor {0} é maior que o segundo valor {1}'.format(n1, n2))
else:
    print('O segundo valor {0} é maior que o primeiro valor {1}'.format(n2, n1))