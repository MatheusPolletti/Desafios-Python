# Meu

'''matrix = list()
dados = list()
MaiorLinhaDois = terceiraColuna = pares = 0

for c in range(3):
    for y in range(3):
        dados.append(int(input(f'Digite seu valor para a posição [{c}], [{y}]: ')))
    matrix.append(dados[:])
    dados.clear()

for m in range(3):
    for i in range(3):
        print(f'[  {matrix[m][i]:^5}  ]', end='')
    print()

for t in matrix:
    for p in t:
        if p % 2 == 0:
            pares += p

for Coluna in range(3):
    terceiraColuna += matrix[Coluna][-1]

for c, linhaDois in enumerate(matrix[1]):
    if c == 0:
        MaiorLinhaDois = linhaDois
    elif linhaDois > MaiorLinhaDois:
        MaiorLinhaDois = linhaDois

print(f'\nA soma dos valores pares é: {pares}')
print(f'A soma dos valores da terceira coluna é: {terceiraColuna}')
print(f'O maior valor da segunda linha é {MaiorLinhaDois}')'''

# Guanabará

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] 
somaPar = maiorValor = somaColuna = 0

for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

for l in range (3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somaPar += matriz[l][c]
    print()

for l in range(3):
    somaColuna += matriz[l][2]

for c in range(3):
    if c == 0:
        maiorValor = matriz[1][c]
    elif matriz[1][c] > maiorValor:
        maiorValor = matriz[1][c]

print(f'A soma dos valores pares é: {somaPar}')
print(f'A soma dos valores da terceira coluna é: {somaColuna}')
print(f'O maior valor é o {maiorValor}')
