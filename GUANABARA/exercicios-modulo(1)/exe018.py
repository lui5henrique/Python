# 18. Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = float(input('Digite um ângulo: '))

seno = math.sin(math.radians(angulo))
con = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print(f'O ângulo de {math.trunc(angulo)}° tem o SENO de {seno:.2f} \n O ângulo de {math.trunc(angulo)}° tem o COSSENO de {con:.2f} \n O ângulo de {math.trunc(angulo)}° tem a TANGENTE de {tan:.2f}')