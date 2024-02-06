# Meu

'''from time import sleep

def anunciado():
    print('='*31)
    print('Analisando os valores passados')
    print('='*31, '\n')
    sleep(1)

def maior(*numero):
    maior = 0
    anunciado()
    print(f'Os valores informados são: ', end='')
    for valor in numero:
        print(valor, end=' ')
    print(f'\nNo total temos {len(numero)} items.')
    for indice, valor in enumerate(numero):
        if indice == 0:
            maior = valor
        elif valor > maior:
            maior = valor
    print(f'O maior valor informado foi {maior}\n')

sleep(1)
maior(2, 9, 4, 5, 7, 1)
sleep(1)
maior(4, 7, 0)
sleep(1)
maior(1, 2)
sleep(1)
maior(6)
sleep(1)
maior()'''

# Guanabará

from time import sleep

def maior(*num):
    contador = maior = 0
    print('\nAnalisando os valores passados: ', end='')
    for valor in num:
        print(f'{valor}', end = ' ', flush=True)
        #sleep(0.4)
        if contador == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        contador += 1
    print(f'\nForam informados {contador} valores ao todo.')
    print(f'O maior valor inforamdo foi {maior}.')


maior(2, 9, 4, 5, 7, 1)

maior(4, 7, 0)

maior(1, 2)

maior(6)

maior()