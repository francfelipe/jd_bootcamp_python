
tentativa = 0

while tentativa < 3:
    # Nome
    try:
        nome: str = "F3LIP"
        if any(char.isdigit() for char in nome):
            tentativa += 1
            print('Não utilize números: ', nome)
        elif len(nome) == 0:
            tentativa += 1
            print('Você não digitou nada.')
        elif nome.isspace():
            tentativa += 1
            print('Você digitou apenas espaço.')
        else:
            nome: str = nome.strip()
            print('Nome: ', nome)
    except ValueError as e:
        tentativa += 1
        print(e)
        
print('Você esgotou o número de tentativas!')