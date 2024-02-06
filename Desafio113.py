# Meu - Eu fiz uma divisão, brah

'''while True:
    try:
        inteiro = int(input('Digite um valor Inteiro: '))
        while True:
            try:
                real = float(input('Digite um real: '))
            except ValueError:
                print('\033[0;31mPor favor, digite um real válido!\033[m')
            except KeyboardInterrupt:
                print('\033[0;31mO usuário parou de digitar!\033[m')
                real = 0
                print(f'O valor inteiro foi {inteiro} e o valor real foi {real}')
                break
            else:
                break
        divisao = inteiro / real
    except (ValueError, TypeError):
        print('\033[0;31mPor favor, digite um inteiro válido!\033[m')
    except KeyboardInterrupt:
        print('\033[0;31mO usuário parou de digitar!\033[m')
    except ZeroDivisionError:
        break
    else:
        print(f'A divisão do {inteiro} pelo {real} é igual a {divisao:.2f}')
        break'''

# Guanabará

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
        
def leiaFloat(msg):
    while True:
        try:
            n = int(input(msg))
        except Exception as erro:
            print(erro.__class__)
            print('\033[0;31mPor favor! Digite um valor inteiro!\033[m')
            continue # Jogo pro começo de novo
        except KeyboardInterrupt:
            print('\n\033[0;31mEntrada de dados interrompida pelo usuário!\033[m')
            break
        else:
            return n


num = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'Valor inteiro digitado {num} e valor real digitado {real}')