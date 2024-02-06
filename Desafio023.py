# Informar a unidade, dezena, centena e milhar de um número

#numero = input('Digite um número de 0 a 9999: ')
#print('milhar: {0}\ncentena: {1}\ndezena: {2}\nunidade: {3}'.format(numero[0], numero[1], numero[2], numero[3]))

# num = input('Digite um número de 0 a 9999: ')
# numero = num.replace('', ' ').lstrip()
# dividido = numero.split()
# print('{0}, {1}, {2}, {3}'.format(num[1][0], num[1][1], num[1][2], num[1][3]))

num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

# print(u)
# print(d)
# print(c)
# print(m)

print('Analisando o número: {0}'.format(num))

print('Unidade: {0}'.format(u))
print('Dezena: {0}'.format(d))
print('Centena: {0}'.format(c))
print('Milhar: {0}'.format(m))