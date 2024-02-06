print('Analisador de triângulos')
print('-'*20)
a = float(input('Digite o tamanho da reta 1: '))
b = float(input('Digite o tamanho da reta 2: '))
c = float(input('Digite o tamanho da reta 3: '))
print('-'*20)

if (b - c ) < a < b + c and (a - c) < b < a + c and (a - b) < c < a + b:
    print('Podem formar um triângulo')
else:
    print('\033[0;31mNão podem formar um triângulo\033[m')
print('-'*20)