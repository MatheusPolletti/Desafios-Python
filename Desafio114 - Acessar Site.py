# Meu

'''import urllib
import urllib.request

try:
    urllib.request.urlopen('https://www.youtube.com/')
except:
    print('Não consegui acessar! ')
else:
    print('Consegui acessar')'''

# Guanabará

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com/')
except urllib.error.URLError: # Código de defeito dele
    print('O site não está acessível!')
else:
    print('O site está acessível!')
    print(site.read()) # Assim você consegue ler o conteúdo do site
