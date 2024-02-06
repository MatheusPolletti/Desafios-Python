'''
palavra = str(input('Digite uma frase para ver se ela é um palíndromo: ')).strip().lower()

palavra = palavra.split()
junto = ''.join(palavra)
inverso = junto[::-1]

if junto == inverso:
    print('Essa palavra é um palíndromo')
else:
    print('Essa palavra não é um palíndromo')
'''

frase = str(input('Digite uma frase para ver se ela é um palíndromo: ')).strip().lower()

palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

print(junto, inverso)

if junto == inverso:
    print('É palíndromo')
else:
    print('Não é palíndromo')