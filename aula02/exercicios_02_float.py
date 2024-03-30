# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

v1 = float(input('Digite o primeiro valor: '))
v2 = float(input('Digite o segundo valor: '))

v3 = v1 + v2

print(f'O valor de {v1} + {v2} é {v3}')

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

v1 = float(input('Digite o primeiro valor: '))
v2 = float(input('Digite o segundo valor: '))

v3 = (v1 + v2) / 2

print(f'A média é {v3}')

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

v1 = float(input('Digite o primeiro valor: '))
v2 = float(input('Digite o segundo valor: '))

v3 = v1 ** v2

print(f'O resultado de {v1} elevado a {v2} é: {v3}')

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

# formula para converter celsius em fahrenheit
# (0 °C × 9/5) + 32 = 32 °F

c1 = float(input('Digite o valor da temperatura em celsius: '))

f1 = (c1 * 9/5) + 32

print(f'A temperatura de {c1} °C convertida em fahrenheit é de {f1} °F.')

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

# fórmula: A = π r²

import math

raio = float(input('Digite o valor do raio para cálculo da área de um círculo: '))

area = math.pi * raio ** 2

print("A área do círculo é:", area)

