import csv

# Caminho para o arquivo
caminho_do_arquivo: str = 'aula04/exemplo.csv'

# Inicializa uma lista vazia para armazenar os dados
dados = []

# Usa o gerenciador de contexto 'with' para abrir o arquivo
# with é um gerenciador de contexto (ele abre e fecha o arquivo para não deixar o arquivo aberto )
with open(caminho_do_arquivo, mode='r', encoding='utf-8') as arquivo:
    # Cria um objeto leitor de CSV
    leitor_csv = csv.DictReader(arquivo)
    
    # Itera sobre as linhas do arquivo CSV
    for linha in leitor_csv:
        # Adiciona cada linha (um dicionário) à lista de dados
        dados.append(linha)
        
# Exibe os dados lidos do arquivo CSV
for registro in dados:
    print(registro)