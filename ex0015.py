print('==== DESAFIO 0015 ====')
import random

aluno01 = str(input('Digite o nome do aluno: '))
aluno02 = str(input('Digite o nome de outro aluno: '))
aluno03 = str(input('Digite o nome de outro aluno: '))
aluno04 = str(input('Digite o nome de mais um aluno: '))

lista = [aluno01, aluno02, aluno03, aluno04]

escolhido = random.choice(lista)

print('O escolhido para apagar o quadro foi: {}'.format(escolhido))

