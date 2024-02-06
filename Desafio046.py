from time import sleep

for e in range (10, -1, -1):
    print('Vai estourar em: {0}'.format(e))
    sleep(1)

print('\n\033[33mEstourou\033[m\n')