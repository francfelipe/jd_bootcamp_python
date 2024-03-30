# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

v1 = input("Digite o primeiro valor (int): ")
v2 = input("Digite o segundo valor (int): ")

v1 = int(v1)
v2 = int(v2)

v3 = v1 + v2 

print(f'O resultado é: {v1} + {v2} = {v3}.')

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

v1 = input("Digite o primeiro valor (int): ")

v1 = int(v1)
v2 = v1%5

print(f'O resto é: {v2}.')

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

v1 = input("Digite o primeiro valor (int): ")
v2 = input("Digite o segundo valor (int): ")

v1 = int(v1)
v2 = int(v2)

v3 = v1 * v2 

print(f'O resultado é: {v1} x {v2} = {v3}.')


# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

v1 = input("Digite o primeiro valor (int): ")
v2 = input("Digite o segundo valor (int): ")

v1 = int(v1)
v2 = int(v2)

v3 = v1 // v2 

print(f'O resultado é: {v1} / {v2} = {v3}.')

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

v1 = input("Digite o primeiro valor (int): ")
v2 = input("Digite o segundo valor (int): ")

v1 = int(v1)
v2 = int(v2)

v3 = v1 ** v2 

print(f'O resultado é: {v1} elevado a {v2} = {v3}.')