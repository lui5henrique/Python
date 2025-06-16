# 12. Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o preço do produto: R$ '))
desconto = 5 / 100  # 5% de desconto
novo_preco = preco - desconto * preco  # Calcula o novo preço com desconto
print(f'O novo preço do produto com 5% de desconto é: R${novo_preco:.2f}.')