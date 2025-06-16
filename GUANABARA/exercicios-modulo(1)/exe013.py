# 13. Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o salário do funcionário: '))
aumento = 15 / 100  # 15% de aumento
novo_salario = (salario * aumento) + salario  # Calcula o novo salário com aumento
print(f'O novo salário do funcionário com 15$ de aumento é: R${novo_salario:.2f}.')