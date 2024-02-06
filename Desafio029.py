velocidade = float(input('Digite a velocidade que o carro estava indo: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você ultrapassou o limite de velocidade\nSua multa está no valor de R${0}.00'.format(multa))
else:
    print('Dirija com segurança!')