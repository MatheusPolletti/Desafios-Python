'''n = 5
valores = list()

for x in range(5):
    n = int(input('Digite um número para ser adicionado: '))

    if x == 0:
        valores.append(n)
    else:
        if n > valores[x - 1]:
            valores.insert(x - 1, n)

print(valores)'''

lista = []

for c in range(5):
    n = int(input('Digite um valor: '))
    if  c == 0 or n > lista[-1]:
        lista.append(n)
    else: 
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionando na posição {pos}')
                break
            pos += 1
print(lista)