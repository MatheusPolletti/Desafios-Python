# Código que eu fiz
'''
print('-'*41)
print('Os 10 termos de uma Progressão Aritmética')
print('-'*41)

pa = pt = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão da P.A: '))

cont = 1

while cont < 11:
    print('{} --> '.format(pa), end='')
    pa += r
    cont += 1

print('--> Acabou')
'''

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

termo = primeiro
cont = 1

while cont <= 10:
    print('{} --> '.format(termo), end='')
    termo += razao
    cont += 1

print('Fim')