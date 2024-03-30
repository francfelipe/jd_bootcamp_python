'''
O objetivo desta aula é falar sobre Controle de Fluxo.

Sempre em atividades atividades de fluxo de dados precisamos definir uma rota para funcionar.
O airflow, por exemplo, é uma ferramenta de orquestração. 
'''

print("esse é o primeiro comando")

print("esse é o segundo comando")

print("esse é o terceiro comando")

'''
Ao executar este arquivo ele executará os scripts acima em uma forma sequencia de cima para baixo.
Na maioria das vezes, precisamos controlar esta sequência através do IF, FOR, WHILE.
Quando olhamos as estruturas (Databricks, Airflow) controlamos as estruturas de fluxos.
'''

'''
DEBUG (rodando o arquivo através do DEBUG)

Ao executar um arquivo, ele roda todo o fluxo. Com o DEBUG conseguimos controlar e rodar linha a linha.

Você marca as linhas que você quer rodar (com duplo clique -ponto de interrupção-) e roda através do DEBUG.

Vai aparecer um controle com play, pular, voltar, parar.

Para isso, marque o inicio e o fim da parte do código que você quer debugar.

No console do lado esquerdo vai aparecer as variáveis sendo criadas.

Vai aparecer um controle com play, pular, voltar, parar.

DEBUGAR é ver linha a linha seu projeto executando.

'''


# CONTROLE DE FLUXO COM IF

# x = 2

# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')
    
    
# CONTROLE DE FLUXO COM FOR
'''
O For itera sobre os itens de qualquer seqência.
'''

for i in range(1,5):
    print(i)
    
for i in 'felipe':
    print(i)
    
    
'''
TIPOS PRIMITIVOS X TIPOS COMPLEXOS

Tipos Primitivos: string, int, float, bool
Tipos Complexos: list, dict (Eu tenho tipos primitivos dentro) 
Faço um dicionário que tem strings.. dicionarios que tem dicionários
'''

# Contagem de palavras em texto

texto = 'hoje é nossa segunda aula do bootcamp, bootcamp de python.'

palavras = texto.split(' ')

print(palavras)

contagem_de_palavras = {}

# eu quero percorter todas as palavras dentro de palavras e checar se ela ja está no meu contagem de palavras

for palavra in palavras:
    if palavra in contagem_de_palavras:
        contagem_de_palavras[palavra] = +1
    else:
        contagem_de_palavras[palavra] = 1
        
print(contagem_de_palavras)


# WHILE LOOP (CONDIÇÃO DESCONHECIDA) 
# Diferentemente do for (onde temos condição conhecida e while para condição desconhecida)
# Cuidado com loopings infinitos

