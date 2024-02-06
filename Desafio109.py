# Meu

'''from exercicio109 import moeda

p = float(input('Digite um valor: '))

print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, mostrar = False)}')
print(f'O dobro de {moeda.moeda(p)} e {moeda.dobro(p, mostrar = True)}')
print(f'Aumentado 10% de {moeda.moeda(p)}, temos {moeda.aumentando(p, 10, mostrar = True)}')
print(f'Diminuindo 20% de {moeda.moeda(p)}, temos {moeda.diminuindo(p, 20, mostrar = True)}')'''

# Guanabara

from exercicio109 import moeda

p = float(input('Digite um valor: '))

print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p)}')
print(f'O dobro de {moeda.moeda(p)} e {moeda.dobro(p, True)}')
print(f'Aumentado 10% de {moeda.moeda(p)}, temos {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 13$ de {moeda.moeda(p)}, temos {moeda.diminuir(p, 13, True)}')
