# 25. Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Digite o seu nome: ')).strip()
nome = nome.lower()
if 'silva' in nome:
    print('O nome contém "Silva"')
else:
    print('O nome não contém "Silva"')