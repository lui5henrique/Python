''' 28. Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

from random import randint
from time import sleep

numero_computador = randint(0, 5) # O computador escolhe um número entre 0 e 5

numero_usuario = int(input('Digite um número entre 0 e 5: '))

print('PROCESSANDO...')
sleep(3)
if numero_usuario == numero_computador:
    print(f'Parabéns! Você acertou, o número era {numero_computador}.')
else:
    print(f'Você errou! O número era {numero_computador}. Tente novamente!')