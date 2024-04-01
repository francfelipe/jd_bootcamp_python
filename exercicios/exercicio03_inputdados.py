import csv
from os import path


PATH: str = 'exercicios/'
nome_arquivo = 'dados.csv'

dados = {
    'nome': ['Felipe', 'Jose', 'Carlos', 'Aberto'],
    'Idade': [18, 25, 30, 55],
    'salario': [2200, 3400, 2200, 8000],
    'funcao': ['Analista Sistema Jr.', 'Analista de BI', 'Analista Sistema Jr.', 'Coordenador de Vendas']
}

# Obtendo os cabeçalhos a partir das chaves do dicionário
cabecalhos = dados.keys()

# Preparando os dados para escrever no CSV
linhas = []
for i in range(len(dados['nome'])):
    linhas.append({cabecalho: dados[cabecalho][i] for cabecalho in cabecalhos})
    
# Corrigindo a forma como o caminho do arquivo é construído
caminho_completo = path.join(PATH, nome_arquivo)

# Abrindo o arquivo CSV para escrita
with open(caminho_completo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
    escreve_csv = csv.DictWriter(arquivo_csv, fieldnames=cabecalhos)
    
    # Escrevendo o cabeçalho
    escreve_csv.writeheader()
    
    # Escrevendo as linhas de dados
    for linha in linhas:
        escreve_csv.writerow(linha)

print(f"Dados salvos com sucesso no arquivo '{nome_arquivo}'.")
