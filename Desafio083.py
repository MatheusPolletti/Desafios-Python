# Meu

'''
validarE = list()
validarD = list()

expressao = str(input('Digite a expressão que você quer validar: ')).strip().lower()

for letra in expressao:
    if '(' in letra:
        validarE.append(letra)
    elif ')' in letra:
        validarD.append(letra)

if (len(validarE) == len(validarD)):
    print('\033[32mA sua expressão é válida.\033[m')
else:
    print('\033[31mA sua expressão não é válida.\033[m')
'''
  
expr = str(input('Digite a sua expressão: '))
pilha = []

for simb in expr:
    if simb == '(':
        pilha.append('(') 
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')') # Serva caso o primeiro seja um )
            break

if len(pilha) == 0:
    print('Sua expressão está válida')
else:
    print('Sua expressão está errada')