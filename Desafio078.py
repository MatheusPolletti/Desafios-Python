# Meu

'''valores = list()

for i in range(5):
    valores.append(int(input(f'Digite um valor para a posição {i}:')))

print(f'Você digitou os valores: {valores}')

#for c, v in enumerate(valores):
#    print(f'{v}', end='')
#    print(', ' if c <= 3  else print(''), end='')

print(f'O maior valor digitado foi {max(valores)} na posição', end='')

for posicaoMa, valorMa in enumerate(valores):
    if valorMa == max(valores):
        print(f' {posicaoMa}', end='')

print(f'\nO menor valor digitado foi {min(valores)} na posição', end='')

for posicaoMe, valorMe in enumerate(valores):
    if valorMe == min(valores):
        print(f' {posicaoMe}', end='')'''

# Guanabará

listanum = []
maior = 0
menor = 0

for c in range(5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = listanum[c]
        menor = listanum[c]
    else:
        if c > maior:
            maior = listanum[c]
        if c < menor:
            menor = listanum[c]

print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(listanum):    
    if v == maior:
        print(f'{i} ', end='')
        
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i} ', end='')