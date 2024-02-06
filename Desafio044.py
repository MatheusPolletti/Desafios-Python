print('-'*5, 'Loja Polletti', '-'*5)
preco = float(input('Digite o preço do produto: R$'))
print('''-----Formas de Pagamento-----\n
1 - À vista dinheiro / cheque
2 - À vista cartão
3 - 2x no cartão
4 - 3x ou mais no cartão\n''')
pagamento = int(input('Qual a forma de pagamento? '))

if pagamento == 3 or pagamento == 4:
    parcela = int(input('Quantas parcelas? '))
    if pagamento == 3 and parcela < 3:
        print('\n\nVocê vai pagar o preço normal')
        pagar = preco / parcela
        print('O valor total a ser pago é de R${0} e você vai pagar R${1} em {2} meses'.format(preco, pagar, parcela))
    elif pagamento == 4 and parcela < 20:
        print('\n\nVocê vai pagar um juros de 20% por mês')
        pagarcompleto = preco + preco * 0.2
        pagar = pagarcompleto / parcela
        print('O valor total a ser pago é de R${0} e você vai pagar \033[31mR${1}\033[m em {2} meses'.format(preco, pagar, parcela))
        print('O valor completo a ser pago é de \033[31mR${0}\033[m'.format(pagarcompleto))
    else:
        print('Não é permitido pagar em mais que 20 parcelas')
elif pagamento == 1 or pagamento == 2:
    if pagamento == 1:
        print('\n\nVocê recebeu um desconto de \033[32m10%\033[m')
        print('O valor a ser pago é de \033[32mR${0:.2f}\033[m'.format(preco - (preco * 10 / 100)))
    elif pagamento == 2:
        print('\n\nVocê recebeu um desconto de \033[32m5%\033[m')
        print('O valor a ser pago é de \033[32mR${0:.2f}\033[m'.format(preco - (preco * 5 / 100)))
else:
    print('\033[31mA forma de pagamento colocada está errada\033[m')