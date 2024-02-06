# Meu

'''matrix = list()
dados = list()

for c in range(3):
    for y in range(3):
        dados.append(int(input('Digite seu valor: ')))
    matrix.append(dados[:])
    dados.clear()

#print(f'[  {matrix[0][0]}  ][  {matrix[0][1]}  ][  {matrix[0][2]}  ]\n[  {matrix[1][0]}  ][  {matrix[1][1]}  ][  {matrix[1][2]}  ]\n[  {matrix[2][0]}  ][  {matrix[2][1]}  ][  {matrix[2][2]}  ]')

for m in range(3):
    for i in range(3):
        print(f'[  {matrix[m][i]:^5}  ]', end='')
    print()'''

# Guanabará

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] 
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

for l in range (3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()