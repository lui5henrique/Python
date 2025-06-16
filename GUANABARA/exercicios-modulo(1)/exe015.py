''' 15. Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
'''

# Passo 1: Perguntar a quantidade de Km percorridos:
km_percorridos = float(input('Digite a quantidade de Km percorridos: '))

# Passo 2: Perguntar a quantidade de dias pelos quais o carro foi alugado:
dias_alugados = int(input('Digite a quandtidade de dias pelos quais o carro foi alugado: '))

#Passo 3: Calcular o preço a pagar:
pagamento = (dias_alugados * 60) + (km_percorridos * 0.15)

# Passo 4: Exibir o resultado:
print(f'O valor a pagar é de R$ {pagamento:.2f} reais.')