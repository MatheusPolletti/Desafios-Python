from math import hypot

oposto = float(input('Digite o valor do cateto oposto em cm: '))
adjacente = float(input('Digite o valor do cateto adjacente em cm: '))
tradicional = (oposto ** 2 + adjacente ** 2) ** (1/2)

print('{:.2f} cm'.format(hypot(oposto, adjacente)))
print('{:.2f} cm'.format(tradicional))