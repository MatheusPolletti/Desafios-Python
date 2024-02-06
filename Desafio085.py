# Meu

'''numeros = list()
listaPar = list()
listaImpar = list()

for c in range(1, 8):
    n = int(input(f'Digite o {c}° valor: '))
    if n % 2 == 0:
        listaPar.append(n)
    else:
        listaImpar.append(n)

listaPar.sort()
listaImpar.sort()
numeros.append(listaPar[:])
numeros.append(listaImpar[:])

print(f'Os valores pares são: {numeros[0]} ')
print(f'Os valores ímpares são: {numeros[1]} ')'''

# Guanabará

num = [[] , []]

valor = 0

for c in range(1, 8):
    valor = int(input(f'Digite o {c}° valor: '))
    if valor % 2 == 0 :
        num[0].append(valor)
    else:
        num[1].append(valor)
    
print(f'Todos os valores: {num}')
print(f'Os valores pares são: {num[0]}')
print(f'Os valores ímpares são: {num[1]}')