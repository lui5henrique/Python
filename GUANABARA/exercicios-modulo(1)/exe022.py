''' 22. Crie um programa que leia o nome completo de uma pessoa e mostre:

- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.
'''

nome_completo = str(input('Digite o seu Nome Completo: '))
print(f'O nome com todas as letras maiúsculas: {nome_completo.upper()}')
print(f'O nome com todas as letras minúsculas: {nome_completo.lower()}')

print(f'Quantas letras ao todo: {len(nome_completo.replace(" ", ""))}')

primeiro_nome = nome_completo.split()[0]
print(f'Quantas letras tem o primeiro nome: {len(primeiro_nome)}')
print(f'O primeiro nome é: {primeiro_nome}')