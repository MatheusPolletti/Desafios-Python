# Meu

'''pessoa = dict()
lista = []

def menu():
    print('-' * 36)
    print('           Menu Principal')
    print('-' * 36)
    print('\033[0;33m1 - \033[0;34mVer Pessoas Cadastradas\033[m')
    print('\033[0;33m2 - \033[0;34mCadastrar nova Pessoa\033[m')
    print('\033[0;33m3 - \033[0;34mSair do Sistema\033[m')
    print('-' * 36)


def validacao():
    while True:
        try:
            opc = int(input('\033[0;36mDigite sua opção: \033[m'))
        except:
            print(f'\033[0;31mErro! Digite um valor válido!\033[m')
        else:
            if opc > 3 or opc < 1:
                print('\033[0;31mErro! Digite uma opção válida!\033[m')
                continue
            return opc


def escolha(opcao):
    
    if opcao == 1:
        print('\033[0;35m')
        print('-' * 36)
        print('        Pessoas Cadastradas:')
        print('-' * 36)
        print('\033[m')
        for valor in lista:
            print(f'{valor['Nome']:<20} {valor['Idade']:>10} anos')
    if opcao == 2:
        print('\033[0;35m')
        print('-' * 36)
        print('         Adicionado usuário        ')
        print('-' * 36)
        print('\033[m')
        pessoa['Nome'] = str(input('Digite o nome do novo usuário cadastrado: '))
        while True:
            try:
                pessoa['Idade'] = int(input('Digite o a idade do usuário: '))
            except:
                continue
            else:
                break
        lista.append(pessoa.copy())
    if opcao == 3:
        print('\033[0;31m')
        print('-' * 36)
        print('  Parando o Sistema. Volte Sempre!  ')
        print('-' * 36)
        print('\033[m')
        exit()

    
def sistema():
    while True:
        menu()
        opcaoRecebida = validacao()
        escolha(opcaoRecebida)'''

# Guanabará

def linha(tam = 42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mPor favor! Digite um valor inteiro!\033[m')
            continue # Jogo pro começo de novo
        except KeyboardInterrupt:
            print('\n\033[0;31mEntrada de dados interrompida pelo usuário!\033[m')
            break
        else:
            return n


def menu(lista):
    cabeçalho('Menu Principal')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua opção: \033[m')
    return opc