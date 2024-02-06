quantia = soma = 0

while True:
    print('Use 999 para parar o sistema')
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    soma += n
    quantia += 1

print(f'A soma de todos os valores foi de {soma} e você digitou {quantia} números')