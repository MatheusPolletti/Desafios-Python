'''
num = int(input('Digite um número inteiro para ser convertido: '))
escolha = int(input('Digite 1 para converter para binário, 2 para converter para octal e 3 para converter para hexadecimal: '))

if escolha == 1:
    print('Você está fazendo uma conversão para binário')
    b = format(num, 'b')
    print('O seu número em binário é: {0}'.format(b))
elif escolha == 2:
    print('Você está fazendo uma conversão para octal')
    o = oct(num)
    print('O seu número em octal é: {0}'.format(o.replace('0o', '')))
elif escolha == 3:
    print('Você está fazendo uma conversão para hexadecimal')
    h = hex(num)
    print('O seu número em hexadecimal é: {0}'.format(h.replace('0x', '')))
else:
    print('O número que você digitou não é válido para uma conversão númerica')

'''

# Como o guanabará fez

num = int(input('Digite um número inteiro para ser convertido: '))
escolha = int(input('Digite 1 para converter para binário, 2 para converter para octal e 3 para converter para hexadecimal: '))


if escolha == 1:
    print('Você está fazendo uma conversão para binário')
    print('O seu número em binário é: {0}'.format(bin(num) [2:]))
elif escolha == 2:
    print('Você está fazendo uma conversão para octal')
    print('O seu número em octal é: {0}'.format(oct(num) [2:]))
elif escolha == 3:
    print('Você está fazendo uma conversão para hexadecimal')
    print('O seu número em hexadecimal é: {0}'.format(hex(num) [2:]))
else:
    print('O número que você digitou não é válido para uma conversão númerica')