# Meu

'''def ficha(jogador, gol):
    if jogador == '':
        jogador = '?Desconhecido?'
    if gol == '' or golUsuario.isdecimal == False:
        gol = '0'
    return f'O jogador {jogador} fez {gol} gol(s) no campeonato'


print('='*24)
jogadorUsuario = str(input('Digite o nome do jogador: ')).strip().title()
golUsuario = str(input('Quantos gols ele marcou? ')).strip()

print(ficha(jogadorUsuario, golUsuario))'''

# Guanabara

def ficha(jogador = '<desconhecido>', gol = 0):
    print(f'O jogador {jogador} fez {gol} gols no campeonato')


nome = str(input('Nome do jogador: '))
g = str(input('Número de gol: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0

if nome.strip() == '':
    ficha(gol = g)
else:
    ficha(nome, g)
