''' 29. Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
'''

velocidade = int(input('Digite a velicidade do carro em km/h: '))

if velocidade > 80:
    excesso = velocidade - 80
    multa = 200 + (excesso * 7)
    print(f'Você foi multado! A multa é de R${multa:.2f} por exceder {excesso} km/h do limite de 80 km/h.')
else:
    print('Você está dentro do limite de velocidade. Continue dirigindo com segurança!')