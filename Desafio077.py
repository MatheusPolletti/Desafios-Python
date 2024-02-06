'''
palavras = ('Matheus', 'Estudar', 'Fatec', 'Amor', 'Computador', 'Livro', 'Lutar', 'Perder', 'Vencer', 'Querer', 'Viver',
          'Curso', 'Python')

for i in range(len(palavras)):
    print(f'Na palavra {palavras[i]} temos ', end='')
    for letra in palavras[i]: # Pode usar apenas com i
        if letra in 'aA':
            print('a ', end='')
        elif letra in 'eE':
            print('e ', end='')
        elif letra in 'iI':
            print('i ', end='')
        elif letra in 'oO':
            print('o ', end='')
        elif letra in 'uU':
            print('u ', end='')
    print('\n')
'''

# Guanabará

palavras = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis', 'Estudar', 'Praticar', 'Trabalhar', 
            'Mercado', 'Programador', 'Futuro')

for p in palavras:
    print(f'\nNa palavra {p} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')