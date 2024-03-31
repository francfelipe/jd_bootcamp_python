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

idade: int = input("Digite sua idade: ")
print(idade)
print(type(idade))

'''
Várias pessoas não curtem o Type Hint justamente pois ele não executa nada.
Ele não executa nada, pois ele é um Hint (dica), uma ajuda.

Ele ajuda a se comunicar melhor!

Não ajuda nada em execução e sim na comunicação.
'''

idade = int(input("Digite sua idade: "))
if isinstance(idade, int):
    print(idade)
else:
    Print('Digite uma idade válida!')
