peso = float(input('Digite o seu peso em kg: '))
al = str(input('Digite a sua altura em cm: '))
altura = al.replace(',', '.')
altura = float(altura)

imc = ( peso / ( pow(altura, 2) ) ) # * 10000 para que não precise de vírgula

if imc < 18.5:
    print('Seu imc é de {0:.1f}'.format(imc))
    print('Você está abaixo do peso')
elif imc < 25:
    print('Seu imc é de {0:.1f}'.format(imc))
    print('Você está no seu peso ideal')
elif imc < 30:
    print('Seu imc é de {0:.1f}'.format(imc))
    print('Você está com sobrepeso')
elif imc < 40:
    print('Seu imc é de {0:.1f}'.format(imc))
    print('Você está obeso')
else:
    print('Seu imc é de {0:.1f}'.format(imc))
    print('Você está com obesidade mórbida')