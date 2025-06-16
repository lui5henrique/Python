''' 19. Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
'''

import random

alunos = ['Gustavo','Helena','Sávio','Henrique']
aluno_escolhido = random.choice(alunos)

print(f'O aluno escolhido para apagar o quadro foi: {aluno_escolhido}.')



''' Se o professor quiser sortear alunos de acordo com o digitado no teclado, pode utulizar o input string,
colocando os nomes separados por vírgula e depois usar o método split para criar a lista.

aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))
sorteio = [aluno1, aluno2, aluno3, aluno 4]
'''