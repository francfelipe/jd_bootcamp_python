nome_usuario = input('Digite seu nome: ')

# Solicitando o valor do salário
tentativa = 0
salario = None  # Inicializando a variável salario

while tentativa < 3:
    try:
        salario_input = input('Digite o valor do salário: ')
        salario = float(salario_input)  # Tentativa de converter a entrada para float
        bonus_input = input('Digite o valor do bônus: ')
        bonus = float(bonus_input)
        valor_bonus = 1000 + (salario * bonus)
        print(f'Olá {nome_usuario}, o seu bônus foi de {valor_bonus}')
        break  # Sai do loop se a conversão for bem-sucedida
    except ValueError:
        print('O valor inserido não é um número válido. Tente novamente')
        tentativa += 1

if salario is None or bonus is None:  # Checa se o salário não foi definido após as tentativas
    print('O número máximo de tentativas foi alcançado. Por favor, tente novamente.')