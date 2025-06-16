# 32. Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date
# Solução 1: Usando a biblioteca datetime
ano = int(input('Digite o ano que desejar ou digite 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')

'''Explicação:
Um ano é bissexto se for divisível por 4, mas não por 100, exceto se for divisível por 400.
'''
