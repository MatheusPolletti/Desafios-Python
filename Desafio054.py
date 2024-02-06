from datetime import date
anoAtual = date.today().year

atingiuMaioridade = 0
naoAtingiuMaioridade = 0


for n in range(1, 8):
    nasc = int(input('Digite o ano de nascimento da {0}° pessoa: '.format(n)))
    idade = anoAtual - nasc
    if idade >= 21 and idade < 200:
        print('Você já atingiu a maioridade')
        atingiuMaioridade += 1
    elif idade < 21 and idade >= 0:
        print('Você ainda não atingiu a maioridade')
        naoAtingiuMaioridade += 1
    else:
        print('A data de nascimento está incorreta')

print('{0} pessoas já são maiores de idade.'.format(atingiuMaioridade))
print('{0} pessoas não são maiores de idade'.format(naoAtingiuMaioridade))