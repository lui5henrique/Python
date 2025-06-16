''' 4. Criar um programa que leia pelo teclado e mostre na tela o seu tipo primitivo
e todas as informações possíveis sobre ele. 
'''
# Exemplo de código para verificar o tipo primitivo e informações sobre o valor digitado
valor_teste = input('Digite algo: ')
print(f'O tipo orimitivo desse valor é: {type(valor_teste)}')
print(f'Só tem espaços? {valor_teste.isspace()}')
print(f'É um número? {valor_teste.isnumeric()}')
print(f'É alfabético? {valor_teste.isalpha()}')
print(f'É alfanumérico? {valor_teste.isalnum()}')
print(f'Está em maiúsculas? {valor_teste.isupper()}')
print(f'Está em minúsculas? {valor_teste.islower()}')
print(f'Está capitalizada? {valor_teste.istitle()}')
print(f'É um dígito? {valor_teste.isdigit()}')
print(f'É um identificador? {valor_teste.isidentifier()}')
print(f'É um espaço? {valor_teste.isspace()}')
print(f'É um printável? {valor_teste.isprintable()}')
print(f'É um símbolo? {valor_teste.isascii()}')
print(f'Contém caracteres especiais? {not valor_teste.isalnum()}')