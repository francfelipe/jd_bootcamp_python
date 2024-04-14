import pandas as pd
import random

# Configurações iniciais
num_records = 200

# Gerando dados aleatórios
data = {
    "id_pedido": [random.randint(1000, 9999) for _ in range(num_records)],
    "id_produto": [random.randint(1, 50) for _ in range(num_records)],
    "descricao_produto": [f"Produto {i}" for i in [random.randint(1, 50) for _ in range(num_records)]],
    "categoria_produto": [random.choice(["Eletrônicos", "Vestuário", "Brinquedos", "Livros", "Esportes"]) for _ in range(num_records)],
    "quantidade": [random.randint(1, 20) for _ in range(num_records)],
    "preco_total": [round(random.uniform(10.0, 300.0) * q, 2) for q in [random.randint(1, 20) for _ in range(num_records)]],
    "status_entrega": [random.choice(["Em transporte", "Entregue", "Pendente"]) for _ in range(num_records)]
}

# Criando o DataFrame
df_vendas = pd.DataFrame(data)

# Salvando o DataFrame em um arquivo CSV
csv_file_path = "aula07/vendas_produtos.csv"
df_vendas.to_csv(csv_file_path, index=False)

csv_file_path
