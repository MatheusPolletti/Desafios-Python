# Meu

'''def voto(anoNasc):
    from datetime import datetime
    anoAtual = datetime.now().year
    idade = anoAtual - anoNasc
    if idade >= 18 and idade <= 65:
        return f'Com {idade} anos o voto é OBRIGATÓRIO'
    elif idade < 16:
        return f'Com {idade} anos você NÃO VOTA'
    elif idade > 65 or idade <= 18:
        return f'Com {idade} anos o voto NÃO É OBRIGATÓRIO'



nasceu = int(input('Digite qual seu ano de nascimento: '))

resultado = voto(nasceu)

print(resultado)'''

# Guanabará

def voto(ano):
    from datetime import datetime
    atual = datetime.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: Não VOTA!'
    elif 16 <= idade < 18 or idade >65:
        return f'Com {idade} anos: Voto OPCIONAL!'
    else:
        return f'Com {idade} anos: Voto Obrigatório!'


nasc = int(input('Você nasceu em que ano? '))

print(voto(nasc))
