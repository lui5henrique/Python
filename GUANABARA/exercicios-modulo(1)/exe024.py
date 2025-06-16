# 24. Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Digite o nome de uma cidade: ')).strip()
cidade = cidade.lower()
if cidade.startswith('santo'):
    print('A cidade começa com "Santo"')
else:
    print('A cidade não começa com "Santo"')