print('-'*41)
print('Os 10 termos de uma Progressão Aritmética')
print('-'*41)

pa = pt = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão da P.A: '))

fim = pt + (10 * r)
# Guanabara fez o fim assim: fim = pt + (10 - 1) * r e fez fim + 1 no for

for n in range(pt, fim, r):
    print('{0} --> '.format(n), end = '')
    # Não precisa usar isso pa += r, o guanabará fez usando apenas o próprio n

print('Acabou')