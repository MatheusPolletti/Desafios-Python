largura = float(input('Digite a largura da sua parede: '))
altura = float(input('Digite a altura da sua parede: '))

área = largura * altura
tinta = área / 2

print('Sua parede tem largura de: {0:.2f}m e altura de: {1:0.2f}m'.format(largura, altura))
print('A área da parede é de {0:.3f}m2\nÉ necessário {1:.4f} litros de tinta para pintar a parede'. format(área, tinta))