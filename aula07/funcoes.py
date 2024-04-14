# %%
'''
Motivação: Reutilização de código.

Funções permitem que você escreva um bloco de código uma vez e o execute múltiplas vezes, possivelmente com diferentes
argumentos, para produzir diferentes resultados.

Isso ajuda a tornar o código mais legível, modular e fácil de debugar.

'''

#%%
'''
Definindo Funções: Utiliza-se a keyword `def` seguida pelo nome da função.

Exemplo:
def minha_funcao():
    return "Hello, worl

'''

# %%
valor_1 = 2
valor_2 = 3
valor_3 = valor_1 + valor_2
valor_3

# %%
valor_4 = 6
valor_5 = 10
valor_6 = valor_4 + valor_5
valor_6

# %%
'''
O objetivo destas funções é exatamente evitar 
estas repetições.
'''

# %%

def soma(valor_1: float, valor_2: float) -> float:
    valor_3 = valor_1 + valor_2
    return valor_3

# %%
valor_1 = 2.6
valor_2 = 3
f_soma = soma(valor_1, valor_2)
f_soma
# %%
f_soma2 = soma(3.4, -3.0)
f_soma2
# %%
def soma_teste(valor_1: float, valor_2: float) -> float:
    '''
    funcao simples de soma de valores  
    valor_1 + valor_2 = total  
    recebe dois argumentos do tipo float  
    '''
    valor_3 = valor_1 + valor_2
    return valor_3
# %%

# Quando eu faço uma função eu ganho agilidade na 
# sustentação

# %%
