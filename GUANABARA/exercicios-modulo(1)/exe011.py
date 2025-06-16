''' 11. Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados. (2m²))
'''

# Exemplo de código para calcular a área da parede e a quantidade de tinta necessária
largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = largura * altura
tinta_necessaria = area / 2

print(f'A área da parede é {area:.2f} m². A quantidade de tinta necessária é {tinta_necessaria:.2f} litros.')