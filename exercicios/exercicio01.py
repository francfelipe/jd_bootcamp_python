'''
Criar programa onde o usuário digita o nome, idade, função, salário e percentual do bônus.
O programa calcula o valor total (1000 + (salario * bônus)) e imprime na tela.
Os resultados são salvos num csv.
'''

# Variáveis
nome: str = None
idade: int = None
funcao: str = None
salario: float = None
bonus: float = None
total: float = None
nome_valido: bool = False
CONSTANT_BONUS: float = 1000
CONSTANT_IDADE_MINIMA: int = 18
CONSTANT_TENTATIVAS: int = 3


# INSERCAO NOME
tentativas:int = 0
while tentativas < CONSTANT_TENTATIVAS:
    try:
        nome: str = input('Digite seu nome: ')
        if any(char.isdigit() for char in nome):
            print('Não utilize números: ', nome)
        elif len(nome) == 0:
            print('Você não digitou nada.')
        elif nome.isspace():
            print('Você digitou apenas espaço.')
        else:
            nome: str = nome.strip()
            print('Nome: ', nome)
            nome_valido = True # Nome é válido, sai do loop
        tentativas += 1
        if not nome_valido and tentativas == CONSTANT_TENTATIVAS:
            print('Número de tentativas atingida.')
            exit()
    except ValueError as e:
        print(e)
        exit()

# Idade
tentativas:int = 0
idade_valida: bool = False

while tentativas <= CONSTANT_TENTATIVAS:
    try:
        idade: int = input('Digite sua idade: ')
        idade: int = int(idade)
        if idade < CONSTANT_IDADE_MINIMA:
            tentativas += 1
            print('Verifique a idade digitada: ', idade)
        else:
            print('Idade: ', idade)
            idade_valida:bool = True
        tentativas += 1
        if not idade_valida and tentativas == CONSTANT_TENTATIVAS:
            print('Número de tentativas atingida.')
            exit()
    except ValueError as e:
        tentativas += 1
        print(e)

#     # Função
#     try:
#         funcao: str = input('Digite sua função: ')
#         if any(char.isdigit() for char in funcao):
#             tentativas += 1
#             print('Não utilize números: ', funcao)
#         elif len(funcao) == 0:
#             tentativas += 1
#             print('Você não digitou nada.')
#         elif funcao.isspace():
#             tentativas += 1
#             print('Você digitou apenas espaço.')
#         else:
#             funcao: str = funcao.strip()
#             print('Função: ', funcao)
#     except ValueError as e:
#         tentativas += 1
#         print(e)

#     # Salário
#     try:
#         salario: float = input('Digite seu salário: ')
#         salario: float = float(salario)
#         if salario < 0:
#             tentativas += 1
#             print('O salário não pode ser negativo: ', salario)
#         else:
#             print(f'Salário: {salario:.2f}')
#     except ValueError as e:
#         tentativas += 1
#         print(e)

#     # Bônus
#     try:
#         bonus: float = input('Digite seu bônus: ')
#         bonus: float = float(bonus)
#         if bonus < 0:
#             tentativas += 1
#             print('O bônus não pode ser negativo: ', bonus)
#         else:
#             print(f'Bônus: {bonus:.2f}')
#     except ValueError as e:
#         tentativas += 1
#         print(e)
# print('Você esgotou o número de tentativas, começe novamente!')
