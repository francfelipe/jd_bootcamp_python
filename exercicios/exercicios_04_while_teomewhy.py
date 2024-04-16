# Faça um programa que recebe uma quantidade indefinida de valores
# correspondentes a "saldo em conta mas quando o usuário apertar "enter" 
# sem digitar valor algum, o programa para de receber valores, e exibe a soma
# de todos os valores digitados anteriormente.

# %% 
total: float = 0
entrada: float = None

while True:
    entrada = input("Entre com o valor do saldo: ")
    if entrada == "":
        break 
    total += float(entrada)
    
print(total)
# %%
