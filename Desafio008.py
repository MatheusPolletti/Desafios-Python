metros = int(input('Digite um valor em metros: '))

print('\n\nO valor em centimetros é: {0:.0f}cm\nO valor em milimetros é: {1:.0f}mm\nO valor em kilometro é: {2}km\nO valor em hm é de: {3}\nO valor em dam é de {4}\nO valor em dm é de: {5}'.format(metros * 100, metros * 1000, metros / 1000, metros / 100, metros / 10, metros * 10))