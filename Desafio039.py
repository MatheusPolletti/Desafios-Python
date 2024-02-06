from datetime import date
anoAtual = date.today().year

idade = int(input('Me diga o seu ano de nascimento: '))
genero = str(input('Você é homem ou mulher? ')).strip().lower()

print('\n\n')

if genero == 'homem':
    if anoAtual - idade == 18:
        tempo = anoAtual - idade
        serviu = tempo - 18
        tavala = anoAtual - serviu
        print('A sua idade é de {0} anos'.format(tempo))
        print('Seu alistamento foi em {0}'.format(tavala))
        print('Você vai servir esse ano')
    elif anoAtual - idade > 18 and anoAtual - idade < 200:
        tempo = anoAtual - idade
        serviu = tempo - 18
        tavala = anoAtual - serviu
        print('A sua idade é de {0} anos'.format(tempo))
        print('Seu alistamento é em {0}'.format(tavala))
        print('Já passou o tempo de servir')
        print('Já faz {0} anos que você serviu!'.format(serviu))
    elif anoAtual - idade < 18 and anoAtual - idade > -1:
        tempo = anoAtual - idade
        print('A sua idade é de {0} anos'.format(tempo))
        print('Você ainda vai servir')  
    else:
        print('O ano de nascimento informado está errado, é impossível você ter nascido em {0}'.format(idade))
else:
    print('Mulheres não precisam servir')