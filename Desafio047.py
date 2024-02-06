# Ver se é par
for n in range(2, 51, 2): # Fazer pulando de 2 em 2 já facilita, pois pula o ímpar
    if n % 2 == 0:
        print('{} é par ,'.format(n), end='')

print('\n')
for i in range (2, 51, 2):
    print(i)