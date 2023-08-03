import polars as pl
import random
import time

inicio = time.time()
modelos_carros = ["Fusca", "Uno", "Gol", "Corolla", "Civic", "Hilux", "Onix", "HB20"]
anos_carros = [str(ano) for ano in range(2000, 2023)]
clientes = ["Cliente1", "Cliente2", "Cliente3", "Cliente4", "Cliente5"]
analise = ["Aprovado", "Reprovado"]

qtde_registros = 400000  # Número de registros que você deseja no arquivo CSV

# Gerando dados aleatórios para a coluna "nome"
nomes_aleatorios = ["".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=8)) for _ in range(qtde_registros)]

# Gerando dados aleatórios para a coluna "modelo_carro"
modelos_aleatorios = [random.choice(modelos_carros) for _ in range(qtde_registros)]

# Gerando dados aleatórios para a coluna "ano_carro"
anos_aleatorios = [random.choice(anos_carros) for _ in range(qtde_registros)]

# Gerando dados aleatórios para a coluna "analise"
analise_aleatorios = [random.choice(analise) for _ in range(qtde_registros)]

# Gerando dados aleatórios para a coluna "cliente"
clientes_aleatorios = [random.choice(clientes) for _ in range(qtde_registros)]

data = {
    "nome": nomes_aleatorios,
    "modelo_carro": modelos_aleatorios,
    "ano_carro": anos_aleatorios,
    "cliente": clientes_aleatorios,
    "analise": analise_aleatorios
}

df = pl.DataFrame(data)

arquivo_csv = "dados_carros.csv"
df.write_csv(arquivo_csv)
fim = time.time()
tempo_execucao = fim - inicio
print("Tempo de execução: {:.6f} segundos".format(tempo_execucao))


