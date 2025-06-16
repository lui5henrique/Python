''' 34. Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
'''

salario = float(input('Digite o salário do funcionário: R$ '))

if salario > 1250:
    aumento10 = salario * 0.10
    print(f'O aumento do salário foi de R$ {aumento10:.2f} e o novo salário é R$ {salario + aumento10:.2f}')
else:
    aumento15 = salario * 0.15
    print(f'O aumento do salário foi de R$ {aumento15:.2f} e o novo salário é R$ {salario + aumento15:.2f}')
