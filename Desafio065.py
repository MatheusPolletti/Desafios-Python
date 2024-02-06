# Meu código
'''
maior = menor = num = soma = contador = 0
continuar = ''

while continuar in 'Ss':
    num = int(input('Digite um número: '))
    if continuar == '':
        menor = maior = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    continuar = str(input('Você quer continuar? [S/N] ')).strip()[0]
    contador += 1
    soma += num

print('Você digitou {0} números. A soma deles é: {1} e a sua média é: {2:.2f}'.format(contador, soma, soma / contador))

if menor == maior:
    print('O maior e menor número são iguais: {0}'.format(maior))
else:
    print('O maior número é {0} e o menor número é {1}'.format(maior, menor))
'''

resp = 'S'
soma = quantia = media = maior = menor = 0

while resp in 'S':
    num = int(input('Digite um número: '))
    soma += num
    quantia += 1
    if quantia == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

media = soma / quantia

print('Você digitou {0} números e a média foi de {1}'.format(quantia, media))
print('O maior número é {0} e o menor número é {1}'.format(maior, menor))
