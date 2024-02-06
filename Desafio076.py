'''produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 20.00, 'Estojo', 28.00, 'Transferidor', 34.00, 'Compasso', 40.00,
            'Mochila', 120.00, 'Canetas', 22.30, 'Livro', 34.90)

print('-'*47)
print('Listagem de preço dos produtos Mercado Polletti')
print('-'*47)

for i in range(len(produtos)):
    if i % 2 == 0:
        print(f'{produtos[i]}', end='')
    elif i % 2 != 0:
        print('.', end='')
        print(f'R$ {produtos[i]:.2f}')
    
print('-'*47)'''

# Guanabará

listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 20.00, 'Estojo', 28.00, 'Transferidor', 34.00, 'Compasso', 40.00,
            'Mochila', 120.00, 'Canetas', 22.30, 'Livro', 34.90)

print('-'*47)
print(f'{"Listagem de preço dos produtos Mercado Polletti":^20}')
print('-'*47)

for pos in range(len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    if pos % 2 == 1:
        print(f'R${listagem[pos]:>5}')