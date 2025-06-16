# 7. Desenvolver um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota1 = float(input('Digite a primeira nota do aluno(a): '))
nota2 = float(input('Digite a segunda nota do aluno(a): '))
media = (nota1 + nota2) / 2
print(f'A média o aluno(a) é {media:.1f}.')