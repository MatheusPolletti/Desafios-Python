# Meu

'''import Desafio115Util

Desafio115Util.sistema()'''

# Guanabará

import Desafio115Util
import Desafio115Arquivo
from time import sleep

arq = 'pessoas.txt' # Por algum motivo o arquivo tá fora da pasta?

if not Desafio115Arquivo.arquivoExiste(arq):
    print('Arquivo não encontrado')
    Desafio115Arquivo.criarArquivo(arq)

while True:
    resposta = Desafio115Util.menu(['Ver pessoas cadastradas', 'Cadastrar Pessoas', 'Sair do sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo
        Desafio115Arquivo.lerArquivo(arq)
    elif resposta == 2:
        Desafio115Util.cabeçalho('Novo cadastro')
        nome = str(input('Nome: '))
        idade = Desafio115Util.leiaInt('Idade: ')
        Desafio115Arquivo.cadastrar(arq, nome, idade)
    elif resposta == 3:
        Desafio115Util.cabeçalho('Saindo do Sistema! Até logo!')
        break
    else:
        Desafio115Util.cabeçalho('\033[31mERRO! Digite uma opção válida!\033[m')
        sleep(2)
    