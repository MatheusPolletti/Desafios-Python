salarioAtual = float(input('Digite o seu salário: R$'))

print('O seu antigo salário era de \033[0;31mR${0:.2f}\033[m'.format(salarioAtual))

if salarioAtual > 1250:
    novoSalario = salarioAtual + (salarioAtual * 0.10)
    print('O seu novo salário é de \033[0;32mR${0:.2f}\033[m'.format(novoSalario))
else:
    novoSalario = salarioAtual + (salarioAtual * 0.15)
    print('O seu novo salário é de \033[0;32mR${0:.2f}\033[m'.format(novoSalario))