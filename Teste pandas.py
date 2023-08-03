import pandas as pd
import random
import string
import time

inicio = time.time()
modelos_carros = ["Fusca", "Uno", "Gol", "Corolla", "Civic", "Hilux", "Onix", "HB20"]
anos_carros = [str(ano) for ano in range(2000, 2023)]
clientes = ["Cliente1", "Cliente2", "Cliente3", "Cliente4", "Cliente5"]

qtde_registros = 20000

# Gerando dados aleatórios para a coluna "nome"
def gerar_nome_aleatorio():
    return "".join(random.choices(string.ascii_lowercase, k=8))

nomes_aleatorios = [gerar_nome_aleatorio() for _ in range(qtde_registros)]

# Gerando dados aleatórios para a coluna "modelo_carro"
modelos_aleatorios = [random.choice(modelos_carros) for _ in range(qtde_registros)]

# Gerando dados aleatórios para a coluna "ano_carro"
anos_aleatorios = [random.choice(anos_carros) for _ in range(qtde_registros)]

# Gerando dados aleatórios para a coluna "cliente"
clientes_aleatorios = [random.choice(clientes) for _ in range(qtde_registros)]

# Criando um DataFrame com os dados
data = {
    "nome": nomes_aleatorios,
    "modelo_carro": modelos_aleatorios,
    "ano_carro": anos_aleatorios,
    "cliente": clientes_aleatorios
}

df = pd.DataFrame(data)

# Salve o DataFrame em um arquivo CSV
arquivo_csv = "dados_carros_pandas.csv"
df.to_csv(arquivo_csv, index=False)
fim = time.time()
tempo_execucao = fim - inicio
print("Tempo de execução: {:.6f} segundos".format(tempo_execucao))
