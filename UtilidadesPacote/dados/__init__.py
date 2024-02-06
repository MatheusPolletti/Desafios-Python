# Meu

'''def leiaDinheiro(msgRecebido):
    mensagem = str(input(msgRecebido)).replace(',', '.')
    while mensagem.replace('.', '').isnumeric() == False:
        print(f'\033[31mErro! \'{mensagem}\' não é um número válido, por favor, digite um número válido\033[m')
        mensagem = str(input(msgRecebido)).replace(',', '.')
    return float(mensagem)'''

# Guanabará

def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '': # Se for alfanúmerico, letras
            print(f'\033[0;31mERRO! {msg} não é válido\033[m')
        else:
            valido = True
            return float(entrada)
