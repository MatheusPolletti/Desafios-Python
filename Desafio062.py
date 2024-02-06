# Código que eu fiz

print('-'*41)
print('Os termos de uma Progressão Aritmética')
print('-'*41)

pt = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão da P.A: '))

cont = 0

while cont < 10:
    print('{} --> '.format(pt), end='')
    pt += r
    cont += 1

print('Acabou')

parar = quantia = cont

while parar != 0:
    parar = int(input('Mais quantos termos você quer ver? '))
    if parar != 0:
        cont = 0
        while cont < parar:
            print('{} --> '.format(pt), end='')
            pt += r
            cont += 1
            quantia += 1
        print('Acabou')

print('Progressão finalizada mostrando {0} termos'.format(quantia))

# Testes

'''
if cont != 0:
    cont = int(input('Mais quantos termos você quer ver?'))
    while cont != (cont - cont +  1):
        print('{} --> '.format(pt), end='')
        pt += r
        cont -= 1
'''

# Código guanabará

'''
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} --> '.format(termo), end='')
        termo += razao
        cont += 1
    print('Fim')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos'.format(total))
'''