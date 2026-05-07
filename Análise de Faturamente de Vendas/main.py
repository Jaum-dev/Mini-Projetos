import pandas as pd

# Lendo os dados do arquivo CSV
df = pd.read_csv('vendas.csv')

# Calculo do faturamento total por produto (Quantidade * Preço)
df['Faturamento'] = df['Quantidade'] * df['Preco_Unitario']

print("--- RELATÓRIO DE VENDAS ---")
print(df)

# Calculo do faturamento total da loja
faturamento_total = df['Faturamento'].sum()
print(f"\nFaturamento Total: R$ {faturamento_total:.2f}")

# Identificando produtos sem estoque (Quantidade == 0)
print("\nProdutos que precisam de reposição de estoque:")
sem_estoque = df[df['Quantidade'] == 0]
print(sem_estoque[['Produto', 'Categoria']])

# Produto que mais gerou receita
produto_destaque = df.loc[df['Faturamento'].idxmax()]
print(f"\nProduto Líder de Faturamento: {produto_destaque['Produto']} (R$ {produto_destaque['Faturamento']:.2f})")