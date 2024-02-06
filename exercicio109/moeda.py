# Meu

'''def metade(valor = 0, mostrar = False):
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
    return resposta'''

# Guanabará

def aumentar(preco = 0, taxa = 0, formato = False):
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
