brasileirão = ('Palmeiras', 'Grêmio', 'Atlético', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense', 'Athletico-PR', 
               'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthias', 'Cruzeiro', 'Vasco', 'Bahia', 'Santos', 'Goiás', 'Coritiba',
               'América-MG')

print(f'Lista de times do Brasileirão: {brasileirão}\033[m')

print(f'\nOs cinco primeiros colocados são: {brasileirão[0:5]}')

print(f'\nOs últimos times são: {brasileirão[-4:]}')

print(f'Os times em ordem alfábetica são: {sorted(brasileirão)}')

print(f'\nO palmeiras está na posição {brasileirão.index('Palmeiras') + 1}')