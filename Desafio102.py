# Meu

"""def fatorial(numero = 1, show = False):
    '''
    A funcao Fatorial calcula o Fatorial de um número
    Parâmetro número: Recebe o número que será calculado o fatorial
    Parâmetro show: Opcional, determina se vai mostrar(True) ou não(False-Padrão) o cálculo do fatorial
    return: Retorna o valor do fatorial numero
    '''
    fatorial = 1
    for c in range(numero, 0, -1):
        if show:
            print(f' {c}', end=' ')
            if c > 1:
                print('*', end='')
            else:
                print('=', end=' ')
        fatorial *= c
    return fatorial


fat = int(input('Você quer saber o fatorial de qual número? '))
while True:
    mostrar = str(input('Você quer mostrar o cálculo?[S/N] ')).strip().upper()[0]
    if mostrar not in 'SN':
        print('Por favor, digite apenas S ou N.')
    elif mostrar in 'SN':
        break

if mostrar in 'S':
    mostrar = True
else:
    mostrar = False

resultado = fatorial(fat, mostrar)

print(resultado)

#help(fatorial)"""

# Guanabará

def fatorial(n = 1, show = False):
    """
    -> Calcula o Fatorial de um número
    :param n: Número fatorial a ser calculado
    :param show: Opcional, mostra se vai mostrar o cálculo
    :return: O valor de fatorial de n
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c} ', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

print(fatorial(5, True))