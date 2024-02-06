# Meu

'''pessoas = list()
dados = list()
maior = menor = contador = 0
pMaior = list()
pMenor = list()

while True:
    resp = ' '
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if contador == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    contador += 1
    pessoas.append(dados[:])
    dados.clear()
    while resp not in 'sn':
        resp = str(input('Você quer continuar? [s/n]: ')).lower().strip()[0]
    if resp in 'n':
        break
    
print(f'Ao total você cadastrou {contador} pessoas')

print(f'O maior peso foi de {maior} kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]} ', end=' ')
        pMaior.append(p[0])

print(f'\nO menor peso foi de {menor} kg. Peso de ')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]} ', end='')
        pMenor.append(p[0])

print(f'\n\nO maior peso foi de {maior}, sendo registrado por {pMaior}\nO menor peso foi de {menor}, sendo registrado por {pMenor}')'''

temp = []
princ = []
mai = men = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        elif temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('S/N: ')).upper().strip()[0]
    if resp in 'N':
        break
print(f'Ao todo você cadastrou {len(princ)} pessoas')
print(f'O maior peso foi {mai} de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'{p[0]} ', end='')
print(f'\nO menor peso foi {men} de ', end='')
for p in princ:
    if p[1] == men:
        print(f'{p[0]} ', end='')