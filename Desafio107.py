# Meu

'''from exercicio107 import moeda

p = float(input('Digite um valor: '))

print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} e {moeda.dobro(p)}')
print(f'Aumentado 10% de {p}, temos {moeda.aumentando(p, 10)}')
print(f'Diminuindo 13$ de {p}, temos {moeda.diminuindo(p, 13)}')'''

from exercicio107 import moeda

p = float(input('Digite o preço: '))

print(f'Metade de {p} é {moeda.metade(p)}')
print(f'Dobro de {p} é {moeda.dobro(p)}')
print(f'Aumento 10% de {p} é {moeda.aumentar(p, 10)}')
print(f'Diminuindo 13% de {p} é {moeda.diminuir(p, 13)}')
