import pandas as pd

# Lendo os dados
df = pd.read_csv('Netflix Dataset.csv')

print("--- ANÁLISE DE DADOS NETFLIX ---")

# Convertendo a coluna Release_Date para o formato de data do Pandas
df['Release_Date'] = pd.to_datetime(df['Release_Date'].str.strip(), errors='coerce')

# Distribuição por Categoria (Filmes vs Séries)
print("\nQuantidade de títulos por Categoria:")
contagem_categoria = df['Category'].value_counts()
print(contagem_categoria.to_string())

# Países com mais produções no catálogo
print("\nTop 5 Países com mais títulos:")
top_paises = df['Country'].value_counts().head(5)
print(top_paises.to_string())

# Filtrando Filmes (Movies) lançados após o ano 2018
filmes_recentes = df[(df['Category'] == 'Movie') & (df['Release_Date'].dt.year > 2018)]

print(f"\nExemplos de Filmes lançados após 2018 (Total: {len(filmes_recentes)}):")
# Mostrando apenas 10 filmes de exemplo
print(filmes_recentes[['Title', 'Release_Date']].head(10).to_string(index=False))

# Verificando a classificação indicativa mais comum
print("\nDistribuição de Classificação Indicativa (Rating):")
rating_dist = df['Rating'].value_counts()
print(rating_dist.to_string())
