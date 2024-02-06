'''
print('\033[34m')
print('-'*17)
print('\033[35m', end='')
print('Tabuada Pollletti', end='')
print('\033[m')
print('\033[34m', end='')
print('-'*17, '\033[m\n')

while True:
    cont = 0
    valor = int(input('\nVocê quer saber a tabuada de qual valor? '))
    print('\n')
    if valor < 0:
        break
    while cont <= 10:
        print(f'{valor} * {cont} = {valor * cont}')
        cont += 1
    
print('\n\033[34mPrograma de Tabuada finalizado. Volte Sempre!\033[m\n')
'''

# Guanabará

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} * {c} = {n * c}')
print('Programa Tabuada Encerrado!')