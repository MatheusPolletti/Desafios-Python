dias = int(input('Quantos dias o carro ficou alugado?: '))
km = int(input('Quantos km o carro andou?: '))
valorDia = dias * 60
valorKm = km * 0.15
pagar = (dias * 60) + (km * 0.15)

print('O valor por dia a ser pago é de: R${0:.2f}'.format(valorDia))
print('O valor por Km a ser pago é de: R${0:.2f}'.format(valorKm))
print('O valor total a ser pago é de: R${0:.2f}'.format(pagar))