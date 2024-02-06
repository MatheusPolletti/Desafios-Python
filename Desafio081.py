# Meu

'''listan = list()
contador = 0

while True:
    resp = ' '
    listan.append(int(input('Digite um número: ')))
    contador += 1
    while resp not in 'SN':
        resp = str(input('Você quer continuar? [S/N]? ')).strip().upper()[0]
    if resp in 'N':
        break

listan.sort(reverse = True)

print(f'Foram digitados {contador} números.')
print(f'A ordem descrescente dos elementos digitados é {listan}')

if 5 in listan:
    print('O valor 5 está presente na lista')
else:
    print('O valor 5 não foi digitado')'''

# Guanabará

valores = []

while True:
    resp = ' '
    valores.append(int(input('Digite um número: ')))
    while resp not in 'SN':
        resp = str(input('Você quer continuar? [S/N]? ')).strip().upper()[0]
    if resp in 'N':
        break

print(f'Você digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'A ordem decrescente dos valores é {valores}')
if 5 in valores:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')