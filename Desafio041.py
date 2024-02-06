from datetime import date
anoAtual = date.today().year

anoNasc = int(input('Digite o seu ano de nascimento: '))
idade = anoAtual - anoNasc

if idade < 9 and idade > -1:
    print('A sua idade é de: {0} anos'.format(idade))
    print('Categoria Mirim')
elif idade < 14 and idade > -1:
    print('A sua idade é de: {0} anos'.format(idade))
    print('Categoria Infantil')
elif idade < 19 and idade > -1:
    print('A sua idade é de: {0} anos'.format(idade))
    print('Categoria Junior')
elif idade < 20 and idade > -1:
    print('A sua idade é de: {0} anos'.format(idade))
    print('Categoria Sênior')
elif idade < 200 and idade > -1:
    print('A sua idade é de: {0} anos'.format(idade))
    print('Categoria Master')
else:
    print('Data de nascimento incorreta')