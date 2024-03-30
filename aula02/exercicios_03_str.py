# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

palavra = input('Digite uma palavra: ')

palavra = palavra.upper()

print(f'A palavra em maiúsculas é: {palavra}')

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

palavra = input('Insira seu nome completo: ')

palavra = palavra.lower()

print(f'O nome completo em minúsculas é: {palavra}')

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

frase = input('Digite uma frase: ')

frase = frase.replace(' ', '')

print(f'A frase sem espaços é: {frase}')

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

data = input('Digite uma data (formato DD/MM/AAA): ')

data = data.split('/')

print(data)

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

p1 = input('Digite a primeira palavra: ')
p2 = input('Digite a segunda palavra: ')

p1 = str(p1)
p2 = str(p2)

p3 = p1 + p2

print(p3)