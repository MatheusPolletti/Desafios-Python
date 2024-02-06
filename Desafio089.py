# Meu

'''pessoas = list()
dados = list()
nome = list()
notas = list()
somado = list()

while True:
    resp = ' '
    nome.append(str(input('Nome: ')))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    media = (notas[0] + notas[1]) / 2
    somado.append(media)
    dados.append(nome[:])
    dados.append(notas[:])
    dados.append(somado[:])
    pessoas.append(dados[:])
    notas.clear()
    somado.clear()
    nome.clear()
    dados.clear()
    while resp not in 'sn':
        resp = str(input('Você quer continuar? [s/n]: ')).lower().strip()[0]
    if resp in 'n':
        break

print('='*30)
print('Nu.      Nome            Média')
print('='*30)

for c, i in enumerate(pessoas):
    print(f'{c:<7}  {i[0][0]:<8}        {i[2][0]:>.1f}')

while True:
    mostrar = int(input('Digite o número de qual aluno você quer saber a nota: '))
    if mostrar == 999:
        break
    if mostrar > len(pessoas) - 1:
        print('Valor digitado inválido')
    elif mostrar < len(pessoas):
        print(f'As notas da pessoa {pessoas[mostrar][0]} são {pessoas[mostrar][1]}:')'''

ficha = list()
while True:
    resp = ' '
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    while resp not in 'sn':
        resp = str(input('Você quer continuar? [s/n]: ')).lower().strip()[0]
    if resp in 'n':
        break

print(f'{"No.":<4}{"Nome":<10}{"Média":>8.1f}')

for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')
while True:
    opc = int(input('Mostrar nota de qual aluno? 999 para: '))
    if opc == 999:
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')