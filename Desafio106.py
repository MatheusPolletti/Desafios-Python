# Meu

'''def ajuda(recebido):
    from time import sleep
    # Menu
    print('\033[0;30;45m')
    print('='*25)
    print(' Sistema de Ajuda Python ')
    print('='*25)
    print('\033[m')
    #Ciclo
    while True:
        decisao = str(input(recebido)).strip()
        mensagem = f'  Acessando o manual do comando {decisao}  '
        if decisao == 'fim':
            print('\033[0;30;41m')
            print('='*24)
            print('  Finalizando Processo  ')
            print('='*24)
            print('\033[m')
            sleep(1)
            break
        print('\033[0;30;44m')
        print('='*len(mensagem))
        print(mensagem)
        print('='*len(mensagem), end='')
        print()
        print('\033[m')
        sleep(1)
        print('\033[0;30;43m')
        help(decisao)
        print('\033[m')
        

ajuda('Digite a Função ou Biblioteca: ')'''

# Guanabara

from time import sleep

c = ('\033[m', # 0 Sem cores
     '\033[0;30;41m', # 1 Vermelho
     '\033[0;30;42m', # 2 Verde
     '\033[0;30;43m', # 3 Amarelo
     '\033[0;30;44m', # 4 Azul
     '\033[0;30;45m', # 5 Roxo
     '\033[7;30m' # 6 Branco
     )

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor = 0):
    tamanho = len(msg) + 4
    print(c[cor], end='')
    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)
    print(c[0], end='')
    sleep(1)

comando = ''

while True:
    titulo('Sistema de Ajuda Python', 2)
    comando = str(input('Função ou Biblioteca >> '))
    if comando.upper() == 'FIM':
        break
    else: 
        ajuda(comando)


titulo('Até logo!', 1)
