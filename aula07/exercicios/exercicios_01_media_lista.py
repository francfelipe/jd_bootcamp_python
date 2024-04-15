# %%
'''
Calcular media de valores um uma lista
'''
# %%
lista = [1,1,1,2,2,2]

soma = 0
for i in lista:
    soma += i
    tamanho = len(lista)
    
print(soma, tamanho, soma/tamanho)
# %%
def media_valores_lista(lista: list) -> int:
    '''
    Calcula a media dos valores de uma lista
    '''
    soma = 0
    for i in lista:
        soma += i
    tamanho = len(lista)
    media = soma / tamanho
    return print(f'Tamanho: {tamanho}, soma: {soma} e média: {media}')
# %%
lista = [1,2]

retorno = media_valores_lista(lista)
retorno
# %%
