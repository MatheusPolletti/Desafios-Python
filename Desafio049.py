tabuada = int(input('Digite o número que você quer saber a tabuada: '))

for n in range(0, 11):
    # multiplica = tabuada * n
    print('{0} x {1} = {2}'.format(tabuada, n, tabuada * n))