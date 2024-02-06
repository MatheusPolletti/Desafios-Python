# Meu código

from time import sleep

print('\033[34m')
print('*'*14)
print('\033[35m', end='')
print('Banco Polletti', end='')
print('\033[m')
print('\033[34m', end='')
print('*'*14, '\033[m\n')

sacar = int(input('Qual valor você gostaria de sacar? R$'))
notaCinquenta = notaVinte = notaDez = notaUm = 0

while True:
    if  sacar >= 50:
        notaCinquenta += 1
        sacar -= 50
    elif sacar >= 20:
        notaVinte += 1
        sacar -= 20
    elif sacar >= 10:
        notaDez += 1
        sacar -= 10
    elif sacar >= 1:
        notaUm += 1
        sacar -= 1
    else:
        break

print('\nVocê está sacando...\n')

sleep(2)

if notaCinquenta > 0:
    print(f'Você está sacando \033[34m{notaCinquenta}\033[m notas de \033[34mR$50.00\033[m')
if notaVinte > 0:
    print(f'Você está sacando \033[34m{notaVinte}\033[m notas de \033[34mR$20.00\033[m')
if notaDez > 0:
    print(f'Você está sacando \033[34m{notaDez}\033[m notas de \033[34mR$10.00\033[m')
if notaUm > 0:
    print(f'Você está sacando \033[34m{notaUm}\033[m notas de \033[34mR$1.00\033[m')

print('\n\033[36mObrigado por fazer negócios conosco. Volte Sempre!\033[m\n')

sleep(10)

'''
total = valor = int(input('Que valor quer sacar R$'))
ced = 50
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
'''