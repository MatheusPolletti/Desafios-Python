# Meu

'''def metade(valor = 0):
    resultado =  valor / 2
    return resultado


def dobro(valor = 0):
    resultado = valor * 2
    return resultado


def aumentando(valor = 0, porcentagem = 0):
    resultado = valor + (valor * porcentagem / 100)
    return resultado


def diminuindo(valor = 0, porcentagem = 0):
    resultado = valor - (valor * porcentagem / 100)
    return resultado

def moeda(valor, moeda = 'R$'):
    resposta = f'{moeda}{valor:^8.2f}'.replace('.', ',')
    return resposta'''

# Guanabará

def aumentar(preco = 0, taxa = 0):
    resposta = preco + (preco * taxa / 100)
    return resposta


def diminuir(preco = 0, taxa = 0):
    resposta =  preco - (preco * taxa / 100)
    return resposta


def dobro(preco = 0):
    resposta = preco * 2
    return resposta


def metade(preco = 0):
    resposta = preco / 2
    return resposta


def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:^8.2f}'.replace('.', ',')
