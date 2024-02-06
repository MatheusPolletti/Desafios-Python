# Meu

'''def leiaInt(recebido):
    valido = str(input(recebido))
    while valido.isnumeric() == False:
        print('\033[31mErro! Você não digitou um valor númerico\033[m')
        valido = str(input(recebido))
    if valido.isnumeric():
        return int(valido)
    
    
numero = leiaInt('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {numero}')'''

# Guanabará

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro! Digite um número inteiro válido!\033[m')
        if ok: 
            break
    return valor

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')