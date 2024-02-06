#import random
#mylist = ["apple", "banana", "cherry"]
#print(random.choices(mylist, weights = [3, 1, 5], k = 14))
#

#import random
#n1 = input('Digite o primeiro nome do grupo 1: ')
#n2 = input('Digite o primeiro nome do grupo 2: ')
#n3 = input('Digite o primeiro nome do grupo 3: ')
#n4 = input('Digite o primeiro nome do grupo 4: ')
#nomes = n1, n2, n3, n4
#tamanho = len(nomes)
#print('A ordem de apresentação dos grupos é: {}'.format(random.choices(nomes, weights = None, cum_weights=None, k = tamanho)))

import random

n1 = str(input('Digite o primeiro nome do grupo 1: '))
n2 = str(input('Digite o primeiro nome do grupo 2: '))
n3 = str(input('Digite o primeiro nome do grupo 3: '))
n4 = str(input('Digite o primeiro nome do grupo 4: '))
n5 = str(input('Digite o primeiro nome do grupo 5: '))

nomes = [n1, n2, n3, n4, n5]
tamanho = len(nomes) # Defini o .length do código
random.shuffle(nomes)

#print('{}'.format(random.sample(nomes, tamanho))) Pode fazer usando .sample também
print('{}'.format(nomes, k = tamanho))