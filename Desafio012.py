preçoAtual = float(input('Digite o valor atual do produto: '))
preçoDesconto = preçoAtual * 0.95
preçoDesconto2 = preçoAtual - (preçoAtual * 5 / 100)

print('O preço com desconto do produto é de: {0:.2f}'.format(preçoDesconto))
print('O preço com desconto do produto é de: {0:.2f}'.format(preçoDesconto2))