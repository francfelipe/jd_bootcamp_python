CONTANTE_BONUS = 1000

# solicitando nome usuário
nome_usuario = input('Digite seu nome: ')

# nome_usuario = 33 isso é um erro?
# nome_usuario = se apenas deu enter e não digitou nada
# nome_usario = digitou apenas espaços

if nome_usuario.isdigit():
    print("Você digitou seu nome errado")
    exit()
elif len(nome_usuario) == 0:
    print("Você não digitou nada")
    exit()
elif nome_usuario.isspace():
    print("Você digitou apenas espaço")
    exit()

# Solicitando o valor do salário

# e se o usuario digitar um valor negativo
# e se o usuario digitar um valor abaixo do salário mínimo
# e se o usuario digitar um valor muito alto
# e se o usuario digitar um valor de outro tipo
# e se o usuario nao digitar nada
# e se o usuario não digitar apenas espaços ok

salario = input('Digite o valor do salário: ')

SALARIO_MINIMO = 1400
SALARIO_MAXIMO = 50000

if salario.isspace():
    print("Você digitou apenas espaço")
    exit()
elif len(salario) == 0:
    print("Você não digitou nada")
    exit()
else:
    try:
        salario = float(salario)
        if salario < SALARIO_MINIMO:
            print(f"Você digitou um salário abaixo do mínimo {SALARIO_MINIMO}.")
        elif salario > SALARIO_MAXIMO:
            print(f"Você digitou um salário acima do máximo {SALARIO_MAXIMO}.")
        else:
            salario
    except ValueError:
        print("Você não digitou um valor numérico")


# # Solicitando o percentual do bônus recebido

'''
e se o bonus for negativo
e se o bonus for digitado em percentual (50) ao invés de 0.5
e se nao digitar nada
e se digitar espaço
e se digitar texto
'''

bonus = input('Digite o valor do bônus: ')
BONUS_MINIMO = 0
BONUS_MAXIMO = 3

if bonus.isspace():
    print("Você digitou apenas espaço")
    exit()
elif len(bonus) == 0:
    print("Você não digitou nada")
    exit()
else:
    try:
        bonus = float(bonus)
        if bonus < BONUS_MINIMO:
            print(f"Você digitou um salário abaixo do mínimo {BONUS_MINIMO}.")
        elif bonus > BONUS_MAXIMO:
            print(f"Você digitou um salário acima do máximo {BONUS_MAXIMO}.")
        else:
            bonus
    except ValueError:
        print("Você não digitou um valor numérico")

valor_total = CONTANTE_BONUS + (salario * bonus)

print(f'Olá {nome_usuario}, o seu bônus foi de {valor_total}')