import random

n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input('Digite o nome do primeiro aluno: '))
n3 = str(input('Digite o nome do primeiro aluno: '))
n4 = str(input('Digite o nome do primeiro aluno: '))
alunos = [n1, n2, n3, n4] # Lista fica entre [] no python

print('O aluno escolhido foi: {}'.format(random.choice(alunos))) # random.choice escolhe um aleatório