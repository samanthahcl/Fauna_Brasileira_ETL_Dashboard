import pandas as pd

# 1. Inspecionando o arquivo de Taxonomia
print("--- Lendo taxon.txt ---")
df_taxon = pd.read_csv("taxon.txt", sep="\t", low_memory=False)
print(df_taxon.info())
print(df_taxon.head(3))

# 2. Inspecionando o arquivo de Distribuição
print("\n--- Lendo distribution.txt ---")
df_dist = pd.read_csv("distribution.txt", sep="\t", low_memory=False)
print(df_dist.info())
print(df_dist.head(3))