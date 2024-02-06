valorCasa = float(input('Diga qual o valor da casa que você deseja comprar: R$'))
salario = float(input('Diga qual é o seu salário: R$'))
anos = int(input('Diga em quantos anos você quer pagar a casa: '))

meses = anos * 12
parcela = valorCasa / meses

if parcela > (salario * 0.3):
    print('Você não pode comprar essa casa')
    print('Você vai ter que pagar {0:.2f} por um período de {1} meses'.format(parcela, meses))
else:
    print('Você pode comprar essa casa')
    print('Você vai ter que pagar {0:.2f} por um período de {1} meses'.format(parcela, meses))