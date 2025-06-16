''' 39. Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

from datetime import date


ano_nascimento = int(input('Informe o ano do seu nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if idade < 18:
    anos_alistamento = 18 - idade
    print(f'Você tem {idade} anos de idade, ainda vai se alistar ao serviço militar. Faltam {anos_alistamento} anos para o alistamento.')

elif idade == 18:
    print('Você tem {idade} anos de idade e está na idade exata para se alistar ao serviço militar. É hora de se alistar!')

else:
    print(f'Você tem {idade} anos de idades e já passou do tempo de alistamento. Já se passaram {idade - 18} anos desde o seu alistamento.')