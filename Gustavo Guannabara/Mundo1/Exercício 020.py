import random
grupo1 = str(input('Digite o nome do primeiro aluno: '))
grupo2 = str(input('Digite o nome do segundo aluno: '))
grupo3 = str(input('Digite o nome do terceiro aluno: '))
grupo4 = str(input('Digite o nome do quarto aluno: '))
nomes = [grupo1,grupo2,grupo3,grupo4]
ordem = random.sample(nomes,4)
print('A ordem de apresentação de trabalho é {}'.format(ordem))