# Meu

def metade(valor = 0, mostrar = False):
    resultado =  valor / 2
    if mostrar:
        resultado = moeda(resultado)
    return resultado


def dobro(valor = 0, mostrar = False):
    resultado = valor * 2
    if mostrar: 
        resultado = moeda(resultado)
    return resultado


def aumentando(valor = 0, porcentagem = 0, mostrar = False):
    resultado = valor + (valor * porcentagem / 100)
    if mostrar:
        resultado = moeda(resultado)
    return resultado


def diminuindo(valor = 0, porcentagem = 0, mostrar = False):
    resultado = valor - (valor * porcentagem / 100)
    if mostrar:
        resultado = moeda(resultado)
    return resultado


def moeda(valor, moeda = 'R$'):
    resposta = f'{moeda}{valor:^8.2f}'.replace('.', ',')
    return resposta


def resumo(preco = 0, aumento = 0, reducao = 0):
    print('-'*31)
    print('        Resumo do valor        ')
    print('-'*31)
    print(f'O preço analisado é: {moeda(preco):>11}')
    print(f'O dobro do preço é: {dobro(preco, True)}')
    print(f'A metade do preço é: {metade(preco, True)}')
    print(f'O preço com um aumento de {aumento}% é: {aumentando(preco, aumento, True)}')
    print(f'O preço com redução de {reducao}% é: {diminuindo(preco, reducao, True)}')


# Guanabará

'''def aumentar(preco = 0, taxa = 0, formato = False):
    resposta = preco + (preco * taxa / 100)
    return resposta if formato is False else moeda(resposta)


def diminuir(preco = 0, taxa = 0, formato = False):
    resposta =  preco - (preco * taxa / 100)
    return resposta if formato is False else moeda(resposta)


def dobro(preco = 0, formato = False):
    resposta = preco * 2
    return resposta if formato is False else moeda(resposta)


def metade(preco = 0, formato = False):
    resposta = preco / 2
    return resposta if not formato else moeda(resposta)


def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:^8.2f}'.replace('.', ',')


def resumo(preco = 0, taxaAumento = 10, taxaReducao = 5):
    print('-'*30)
    print('Resumo do valor'. center(30)) # Centraliza em 30 caracteres
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preco)}') # \t para tabulação
    print(f'O dobro de {moeda(preco)}: \t{dobro(preco, True)}')
    print(f'Metade de {moeda(preco)}: \t{metade(preco, True)}')
    print(f'Aumento de {taxaAumento}%: \t{aumentar(preco, taxaAumento, True)}')
    print(f'Diminuindo {taxaReducao}%: \t\t{diminuir(preco, taxaReducao, True)}')
    print(f'-'*30)'''