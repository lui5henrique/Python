''' 37. Escreva um programa em Python que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
'''

# Solicita um número inteiro e a base de conversão ao usuário
n = int(input('Digite um número inteiro: '))
print('Agora escolha uma das bases de conversão:')
print('[1] Converter para BINÁRIO')
print('[2] Converter para OCTAL')    
print('[3] Converter para HEXADECIMAL')
opcao = int(input('Qual base você escolhe?'))

if opcao == 1:
    print(f'{n} convertido para BINÁRIO é igual a {bin(n)[2:]}.')

elif opcao == 2:
    print(f'{n} convertido para OCTAL é igual a {oct(n)[2:]}.')

elif opcao == 3:
    print(f'{n} convertido para HEXADECIMAL é igual a {hex(n)[2:]}.')

else:
    print('Opção inválida. Tente novamente.')