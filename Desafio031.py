distancia = float(input('Digite a distância da viagem em km: '))

valor = distancia * 0.50 if distancia <= 200 else distancia * 0.45

print('Você vai fazer uma viagem de {0}km'.format(distancia))
print('Você precisa pagar R${0:.2f}'.format(valor))

'''
if distancia <= 200:
    valor = distancia * 0.50
    print('Você vai fazer uma viagem de {0}km'.format(distancia))
    print('Você precisa pagar R${0:.2f}'.format(valor))
else:
    valor = distancia * 0.45
    print('Você vai fazer uma viagem de {0}km'.format(distancia))
    print('Você precisa pagar R${0:.2f}'.format(valor))
'''