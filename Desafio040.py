n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))

media = (n1 + n2) / 2

if media < 5:
    print('Você foi reprovado')
elif media < 6.9:
    print('Você está de recuperação')
else:
    print('Você passou de ano! Parabéns!')