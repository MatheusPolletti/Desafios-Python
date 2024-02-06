# Meu

'''jogadores = list()

jogador = dict()

gols = list()

num = 0

while True:
    resp = ' '
    total = 0
    jogador['Nome'] = str(input('Digite seu nome: ')).strip().title()
    jogos = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for cont in range(jogos):
        gol = int(input(f'Quantos gols ele fez na partida {cont + 1}? '))
        gols.append(gol)
        total += gol
    jogador['Gols'] = gols[:] # Para fazer uma cópia e não uma  referência
    jogador['Total'] = total
    jogadores.append(jogador.copy())
    gols.clear()
    while resp not in 'SN':
        resp = str(input('Você quer continuar? [S/N]: ')).strip().upper()[0]
    if resp in 'N':
        break

print('Número    =    Nome    =    Gols    =    Total')
print('-'*70)
for c, i in enumerate(jogadores):
    print(f'{c:<10}  {i['Nome']:<14}  {i['Gols']}  {i['Total']:>15}')

while num != 999:
    num = int(input('Digite o jogador que você quer ver: [Use 999 para parar]: '))
    if num > len(jogadores) - 1 or num < 0:
        print('Número incorreto!')
    else:
        print(f'Levantamento do jogador {jogadores[num]['Nome']}')
        for contador, g in enumerate(jogadores[num]['Gols']):
            print(f'No {contador + 1}° jogo, ele fez {g} gols.')

print('Volte Sempre!')'''

# Guanabará

jogador = dict()

partidas = list()

time = list()

while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: ')).strip()
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    partidas.clear()
    for c in range(tot):
        partidas.append(int(input(f'Quantos gols ele fez na {c + 1}° partida: ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar:  [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('Responda apenas S ou N!')
    if resp == 'N':
        break

#print(f'\033[32m{time}\n{partidas}\n{jogador}\033[m')
print('Cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

print('-'*40)
for chave, valor in enumerate(time):
    print(f'{chave:>3}', end='')
    #print(f'\033[32m{chave}{valor}\033[m')
    for dado in valor.values():
        print(f'{str(dado):<15}', end='') # transformou dado em string pra poder usar o :<15
        #print(f'\033[32m{dado}\033[m')
    print()
print('-'*40)

while True:
    busca = int(input('Mostrar dado de qual jogador? (999 para)'))
    if busca == 999:
        break
    if 0 < busca >= len(time):
        print('Esse código não existe')
    else:
        print(f'Levantamento de jogador: {time[busca]["Nome"]}')
        for indice, g in enumerate(time[busca]['Gols']):
            print(f'No jogo {indice + 1} ele fez {g} gols')
    print('-'*40)
print('Volte Sempre!')