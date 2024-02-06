# Meu

'''def escreva(texto):
    print('-'*len(texto))
    print(texto)
    print('-'*len(texto))


escreva(str(input('Digite seu texto: ')).strip().title())'''

def escreva(msg):
    tam = len(msg) + 4
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)


escreva('Gustavo Guanabará')

escreva('Matheus Polletti')

escreva('Curso em Vídeo')