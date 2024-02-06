'''
Como eu fiz

print('Analisador de triângulos')
print('-'*20)
a = float(input('Digite o tamanho da reta 1: '))
b = float(input('Digite o tamanho da reta 2: '))
c = float(input('Digite o tamanho da reta 3: '))
print('-'*20)

if ( (b - c ) < a < b + c and (a - c) < b < a + c and (a - b) < c < a + b) and (a == b == c):
    print('Podem formar um triângulo')
    print('Ele é um triângulo Equilátero')
elif ( (b - c ) < a < b + c and (a - c) < b < a + c and (a - b) < c < a + b) and ( (a == b and a != c and b != c) or (c == b and b != a and c != a) or (a == c and a != b and c != b)):
    print('Podem formar um triângulo')
    print('Ele é um triângulo Isósceles')
elif ( (b - c ) < a < b + c and (a - c) < b < a + c and (a - b) < c < a + b) and (a != b != c):
    print('Podem formar um triângulo')
    print('Ele é um triângulo Escaleno')
else:
    print('\033[0;31mNão podem formar um triângulo\033[m')
print('-'*20)
'''

# Como o guanabará fez

print('Analisador de triângulos')
print('-'*20)
a = float(input('Digite o tamanho da reta 1: '))
b = float(input('Digite o tamanho da reta 2: '))
c = float(input('Digite o tamanho da reta 3: '))
print('-'*20)

if (b - c ) < a < b + c and (a - c) < b < a + c and (a - b) < c < a + b:
    print('Podem formar um triângulo')
    if a == b == c:
        print('Equilátero')
    elif a != b != c != a:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('\033[0;31mNão podem formar um triângulo\033[m')
print('-'*20)