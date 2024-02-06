def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') # a tenta abrir, rt é read text
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') # Criar o arquivo, o mais serve para criar o arquivo caso ele não exista
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')

    
def lerArquivo(nome):
    try:
        a = open(nome, 'rt') 
    except:
        print('Erro ao abrir o arquivo')
    else:   
        #print(a.read()) # read lê isso, radlines lê as linhas do arquivo, junto da formatação (\n)
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Erro na abertura')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro na hora de inscrever dados')
        else:
            print('Registro com sucesso')
