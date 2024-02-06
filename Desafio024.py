# Ver se o nome da cidade começa com Santo
cidade = str(input('Digite o nome da sua cidade: ')).strip().lower().split()

print('santo' in cidade[0])

# Guanabara Fez Assim

cid = str(input('Digite o nome da sua cidade: ')).strip()
totmenor = totmaior = 0
print(cid[:5].upper() == 'SANTO')