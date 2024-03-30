# solicitando nome usuário
nome_usuario = input('Digite seu nome: ')

# Solicitando o valor do salário
salario = input('Digite o valor do salário: ')
salario = float(salario)

# Solicitando o percentual do bônus recebido
bonus = input('Digite o valor percentual do bônus: ')
bonus = float(bonus)

valor_total = 1000 + (salario * bonus)

print(f'Olá {nome_usuario}, o seu bônus foi de {valor_total}')