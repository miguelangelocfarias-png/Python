from random import choice
aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do primeiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))
nomes = [aluno1,aluno2,aluno3,aluno4]
sorteado = choice(nomes)
print('O aluno sorteado é o aluno {}'.format(sorteado))
