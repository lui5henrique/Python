''' 26. Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
'''

frase = str(input('Digite uma frase: ')).strip().lower()
quantidade_a = frase.count('a')

primeira_posicao = frase.find('a')
ultima_posicao = frase.rfind('a')

print(f'A letra "A" aparece {quantidade_a} vezes.')
print(f' A letra "A" aparece pela primeira vez na posição {primeira_posicao + 1}.')
print(f' A letra "A" aparece pela última vez na posição {ultima_posicao + 1}.')