import polars as pl
import matplotlib.pyplot as plt

# Caminho para o arquivo CSV gerado anteriormente
arquivo_csv = "dados_carros.csv"

# Leitura do arquivo CSV para um DataFrame com o polars
df = pl.read_csv(arquivo_csv)

# Agrupar por modelo e ano e contar a quantidade de carros aprovados em cada grupo
contagem_total = df.groupby(['modelo', 'fabricacao']).agg(pl.count('modelo').alias('quantidade'))

# Filtrar os carros reprovados
df_reprovados = df.filter(df['case'] == 'Reprovado')
# Agrupar por modelo e ano e contar a quantidade de carros aprovados em cada grupo
resultado_reprovados = df_reprovados.groupby(['modelo', 'fabricacao']).agg(pl.count('modelo').alias('quantidade'))

# Exibir o resultado
print(resultado_reprovados)

# Exibir o resultado dos carros reprovados com contagem igual a 0
print("Carros Reprovados com Contagem 0:")
print(resultado_reprovados.filter(resultado_reprovados['quantidade'] == 1))

# Filtrar apenas os carros reprovados com contagem igual a 0
df_resultado_reprovados = resultado_reprovados.filter(resultado_reprovados['quantidade'] == 1)

# Realiza o inner join dos DataFrames df_resultado_reprovados e contagem_total
df_resultado_reprovados_com_total = df_resultado_reprovados.join(
    contagem_total,
    on=['modelo', 'fabricacao'],  # Colunas de agrupamento para a junção
    suffix='_total'  # Sufixo para adicionar às colunas do contagem_total para evitar conflitos de nome
)

# Ordena o DataFrame de forma crescente pela coluna "quantidade_total"
df_resultado_reprovados_com_total = df_resultado_reprovados_com_total.sort(
    by=['quantidade_total']
)

# Inverte a ordem do DataFrame para que a ordenação seja decrescente
df_resultado_reprovados_com_total = df_resultado_reprovados_com_total.reverse()

# Exibe o resultado com a nova coluna "quantidade_total" ordenada de forma decrescente
print(df_resultado_reprovados_com_total)

# Salvar o DataFrame ordenado com a nova coluna em um arquivo CSV
arquivo_csv_resultado_reprovados_com_total = "carros_reprovados_com_total.csv"
df_resultado_reprovados_com_total.write_csv(arquivo_csv_resultado_reprovados_com_total)

# Seleciona os 5 principais itens (modelos e anos) com base na coluna "quantidade_total"
top_5_itens = df_resultado_reprovados_com_total.head(5)

# Plotar o gráfico de barras
plt.bar(top_5_itens['modelo'], top_5_itens['quantidade_total'])

# Adicionar título e rótulos aos eixos
plt.title('Top 5 Carros Reprovados')
plt.xlabel('Modelo e Ano')
plt.ylabel('Quantidade Total Reprovada')

# Mostrar o gráfico
plt.show()