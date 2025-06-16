''' 30. Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
'''

distancia = float(input('Digite a distância da viagem em km: '))

if distancia <= 200:
    preco200 = distancia * 0,50
    print(f'O preço da passagem é R${preco200:}')
elif distancia > 200:
    preco201 = distancia * 0.45
    print(f'O preço da passagem é R${preco201:.2f}.')
else:
    print('Distância inválida. Por favor, insira um valor positivo.')