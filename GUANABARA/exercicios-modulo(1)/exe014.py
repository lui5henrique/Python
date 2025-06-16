# 14. Escreva um programa que converta uma temperatura digitada em graus Celsius e converta para graus Fahrenheit.

# Passo 1: Solicitar ao usuário a temperatura em graus Celsius.
temp_celsius = float(input('Digite a temperatura em graus Celsius: '))

# Passo 2: Calcular a temperatura em graus Fahrenheit usando a formúla: F = C * 9/5 + 32
temp_fahrenheit = temp_celsius * 9/5 + 32

# Passo 3: Exibir o resultado da conversão.
print(f'A temperatura de {temp_celsius} graus Celsius é igual a {temp_fahrenheit} graus Fahrenheit.')

# Passo 4: Finalizar o programa
