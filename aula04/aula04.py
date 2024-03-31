'''
Type Hint (Dicas de Tipo)

Ajuda a tornar o código mais legível e seguro, especificando o tipo de dados esperados por funções e variáveis.

Na engenharia de dados, isso é útil para farantir que as funções de manipulação e análise de dados recebam
os dados no formato correto, reduzindo erros e tempo de execução.

Disponível após Python 3.5

'''

# Sem Type Hint (Tipagem por inferência: Ao receber um atributo ele tipa dinamicamente)

# idade = 30
# altura = 1.75
# nome = "Alice"
# is_estudante = True

#Com Type Hint (Tipagem Estática)

# idade: int = 38
# altura: float = 1.75
# nome: str = "Alice"
# estudante: bool = True

# altura 

'''
A vantagem da Tipagem Estática é deixar evidente em seu código que tipo de dado ela é. 
Perceba que ao declarar uma variável utilizando o type hint, ao passar o mouse por cima dessa variável,
vai aparecer como dica altura: int = 38 -> `(variable) altura: float`
'''


# TIPAGEM FORTE VS TIPAGEM FRACA

'''
Tipagem forte: Não é automaticamente tratada como outro tipo sem uma conversão explícita. Exemplo: 2 + '2' resultará
TypeError, pois 2 é float e '2' é str.
'''

# idade: int = input("Digite sua idade: ")
# print(idade)
# print(type(idade))

'''
Várias pessoas não curtem o Type Hint justamente pois ele não executa nada.
Ele não executa nada, pois ele é um Hint (dica), uma ajuda.

Ele ajuda a se comunicar melhor!

Não ajuda nada em execução e sim na comunicação.
'''

# idade = int(input("Digite sua idade: "))
# if isinstance(idade, int):
#     print(idade)
# else:
#     print('Digite uma idade válida!')
    
'''
Tipos Complexos

Um conjunto de tipos primitivos (str, int, bool, float) ou de outros tipos complexos
'''

# produto: str = "sapato"
# produto_2: str = "camiseta"
# produto_3: str = "videogame"

# produtos: list = []

# produtos.append(produto)
# produtos.append(produto_2)
# produtos.append(produto_2)

# print(produtos)

'''
Dicionário: Estrutura de chaves e valores

'''

# produto_01: dict = {
#     'nome': 'Sapato',
#     'quantidade': 39,
#     'preco': 10.38,
#     'disponibilidade': True,
# }

# produto_02: dict = {
#     'nome': 'Televisao',
#     'quantidade': 10,
#     'preco': 70.38,
#     'disponibilidade': False,
# }

# carrinho: list = []

# carrinho.append(produto_01)
# carrinho.append(produto_02)

# print(carrinho)

# json e dicionário são praticamente a mesma coisa, possui a mesma estrutura de chave valor

# para converter o carrinho para um json

# import json 
# carrinho_json = json.dumps(carrinho)
# print(carrinho_json)

# compare a estrutura entre o carrinho e o carrinho json (São parecidos)

# Crie um dicionário para armazenar informações de um livro,
# incluindo título, autor e ano de publicação. Imprima cada informação.

from typing import Dict, Any

livro: Dict[str, Any] = {
    'Titulo': 'Game of Thrones',
    'Autor': 'Estagiário',
    'Ano': 2005
}

lista_de_elementos: list = livro.items()
for elemento in lista_de_elementos:
    print(elemento)