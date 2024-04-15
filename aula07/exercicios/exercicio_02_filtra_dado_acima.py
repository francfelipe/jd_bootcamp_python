# %%
'''
Filtra dado acima de um limite
Pessoa escolhe um valor e filtra dados de uma lista acima do valor escolhido
'''

# %%

lista = [1,4,10,15]
# %%
resultado = []
valor = 5
for i in lista:
    if i > valor:
        resultado.append(i)
        
resultado
# %%
def filtra_valores_acima(lista: list, valor: float) -> list:
    resultado: list = []
    for i in lista:
        if i > valor:
            resultado.append(i)
    return resultado
# %%
lista = [10, 20, 50, 100]
valor = 10

acima = filtra_valores_acima(lista, valor)
acima 
# %%
