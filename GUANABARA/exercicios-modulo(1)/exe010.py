''' 10. Ler quanto dinheiro uma pessoa tem na carteira e mostrar quantos dólares ela pode comprar.
Considere US$1,00 = R$3,27
'''
# Exemplo de código para converter reais em dólares
carteira = float(input('Digite quanto dinheiro você tem na carteira: R$ '))

dolar = 3.27
quantidade_dolares = carteira / dolar
print(f'Com R$ {carteira:.2f} você pode comprar US$ {quantidade_dolares:.2f}.')