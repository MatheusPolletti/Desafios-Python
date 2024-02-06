# Meu

'''print('Tamanho de Terreno')
print('=-='*6)

def terreno(largura, comprimento):
    tamanho = largura * comprimento
    print(f'O seu terreno tem uma largura e comprimento de: {largura} * {comprimento}, isso da um tamanho de {tamanho}m²')


terreno(float(input('Digite a largura (m) do seu terreno: ')), float(input('Digite o comprimento (m) do seu terreno: ')))'''

def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}*{comp} é de {a}m²')


print('Controle de terrenos: ')
print('-'*20)
l = float(input('Largura em metros: '))
c = float(input('Comprimento em metros: '))
area(l, c)