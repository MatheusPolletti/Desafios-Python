'''
Como eu fiz
ano = int(input('Digite o ano para saber se ele é bissexto: '))

anoStr = str(ano)
anoCortado = " ".join(anoStr).split()
anoFim = int(anoCortado[len(anoCortado) - 2] + anoCortado[len(anoCortado) - 1])

#if ano % 4 == 0 and anoFim != 00:
#    print('Esse ano é bissexto')
#else:
#    print('Esse ano não é bissexto')

if anoFim == 00 and ano % 400 == 0:
    print('Esse ano é bissexto')
elif anoFim != 00 and ano % 4 == 0:
    print('Esse ano é bissexto')
else:
    print('Esse ano não é bissexto')
'''

from datetime import date

ano = int(input('Que ano quer analisar? Se colocar 0 análisa o ano atual '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {0} é bissexto'.format(ano))
else:
    print('\033[0;36;41mNão é bissexto\033[m')