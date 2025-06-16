# 33. Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

#maior = n1 > n2 and n1 > n3 or n2 > n1 and n2 > n3 or n3 > n1 and n3 > n2
#menor = n1 < n2 and n1 < n3 or n2 < n1 and n2 < n3 or n3 < n1 and n3 < n2

maior = (n1, n2, n3)
menor = (n1, n2, n3)


if maior:
    if n1 > n2 and n1 > n3:
        print(f'O maior número é {n1}')
    elif n2 > n1 and n2 > n3:
        print(f'O maior número é {n2}')
    else:
        print(f'O maior número é {n3}')
if menor:
    if n1 < n2 and n1 < n3:
        print(f'O menor número é {n1}')
    elif n2 < n1 and n2 < n3:
        print(f'O menor número é {n2}')
    else:
        print(f'O menor número é {n3}')