# Meu

'''listaCompleta = list()
listaPar = list()
listaImpar = list()


while True:
    resp = ' '
    listaCompleta.append(int(input('Digite um número: ')))
    while resp not in 'SN':
        resp = str(input('Você quer continuar? [S/N]? ')).strip().upper()[0]
    if resp in 'N':
        break

for i in listaCompleta:
    if i % 2 == 0:
        listaPar.append(i)
    else:
        listaImpar.append(i)

listaCompleta.sort()
listaPar.sort()
listaImpar.sort()

print(f'A lista completa é {listaCompleta}')
print(f'A lista de pares é {listaPar}')
print(f'A lista de ímpares é {listaImpar}')'''

# Guanabará

num = []
pares = []
impares = []

while True:
    num.append(int(input('Digite seu número: ')))
    resp = str(input('Quer continuar? [s/n]')).strip().lower()[0]
    if resp in 'n':
        break

for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)


print(f'A lista é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')