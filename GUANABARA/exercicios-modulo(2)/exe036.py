''' 36. Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''
# Solicita os dados do usuário
valor_casa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite o valor do seu salário: R$ '))
anos_pagamento = int(input('Em quantos anos você quer pagar? '))

# Calcula a prestação mensal e o limite de 30% do salário
prestacao = valor_casa / (anos_pagamento * 12)
limite = salario * 0.30

if prestacao <= limite:
    print(f'Empréstimo aprovado! A prestação mensal será de R$ {prestacao:.2f}.')
else:
    print(f'Empréstimo negado! A prestação mensal de R$ {prestacao:.2f} excede o limite de 30% do seu salário de R$ {salario:.2f}.')