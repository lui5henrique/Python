''' 27. Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.
'''

nome_completo = str(input('Digite o seu nome completo: ')).strip().lower()

nome_dividido = nome_completo.split()
primeiro_nome = nome_dividido[0]
ultimo_nome = nome_dividido[-1]

print(f'Primeiro nome: {primeiro_nome.capitalize()}')
print(f'Último nome: {ultimo_nome.capitalize()}')