import csv

path_arquivo = 'aula07/vendas_produtos.csv'

def ler_csv(nome_do_arquivo_csv: str) -> list[dict]:
    '''
    Funcao que le um arquivo csv e retorna uma
    lista de dicionarios
    '''
    lista: list = []
    with open(nome_do_arquivo_csv, mode = 'r', encoding = 'utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
           lista.append(linha) 
    return lista

def filtrar_produtos_nao_entregues(lista: list[dict]) -> list[dict]:
    '''
    Funcao que filtra produtos onde status_entrega é entregue.
    '''
    lista_com_produtos_entregues: list = []
    for produto in lista:
        if produto.get('status_entrega') == 'Entregue':
            lista_com_produtos_entregues.append(produto)
    return lista_com_produtos_entregues

def somar_valores_dos_produtos(lista_com_produtos_entregues: list[dict]) -> float:
    '''
    Funcao que soma os valores dos produtos
    '''
    valor_total: float = 0
    for produto in lista_com_produtos_entregues:
        valor_total += float(produto.get('preco_total'))
    return valor_total


lista_de_produtos = ler_csv(path_arquivo)
produtos_entregues = filtrar_produtos_nao_entregues(lista_de_produtos)
valor_dos_produtos_entregues = somar_valores_dos_produtos(produtos_entregues)
print(valor_dos_produtos_entregues)

