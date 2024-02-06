# Meu

numeros =  ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
            'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int
    parar = str
    while num  not in range(0, 21):
        num = int(input('Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {numeros[num]}')
    while parar  != 's' and parar != 'n':
        parar = str(input('Você quer parar? [S/N]: ')).strip().lower()[0]
    if parar in 's':
        break

# Guanabará
'''
cont =  ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
            'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente')

print(f'Você digitou o número {cont[num]}')
'''