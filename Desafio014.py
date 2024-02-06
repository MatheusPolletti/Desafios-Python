c = float(input('Digite a temperatura em graus celsius °C ')) 

f1 = (c * 1.8) + 32
#f2 = (c * 9/5) + 32
k = c + 273.15

print('A temperatura em farhnheit é de {0:.2f} °F'.format(f1))
#print('A temperatura em farhnheit é de {0:.2f}'.format(f2))
print('A temperatura em farhnheit é de {0:.2f} K'.format(k))