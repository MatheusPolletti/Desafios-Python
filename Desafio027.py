nome = str(input('Digite o seu nome completo: ')).strip()
nomeCortado = nome.split()
tamanho = len(nomeCortado)

print('O seu primeiro nome é: {0}'.format(nomeCortado[0]))
print('O seu último nome é: {0}'.format(nomeCortado[tamanho - 1]))

# Também pode escrever assim
# print('O seu último nome é: {0}'.format(nomeCortado[len(nomeCortado) - 1]))


# print(nomeCortado)
# print(tamanho - 1)