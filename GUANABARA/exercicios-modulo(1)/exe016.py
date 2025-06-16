# 16. Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import math

num_real = float(input('Digite um número Real: '))

# Usando a função math.floor para obter a parte inteira
parte_inteira = math.trunc(num_real)

print(f'O número Real digitado foi {num_real} e sua parte inteira é {parte_inteira}.')