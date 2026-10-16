import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração estética dos gráficos
sns.set_theme(style="whitegrid")
plt.rcParams['font.sans-serif'] = 'Segoe UI'

print("==================================================")
print(" 1. CARREGAMENTO E INSPEÇÃO INICIAL DOS DADOS")
print("==================================================")

# Carregamento dos ficheiros Darwin Core Archive (DwC-A) do ICMBio
df_taxon = pd.read_csv("taxon.txt", sep="\t", low_memory=False)
df_dist = pd.read_csv("distribution.txt", sep="\t", low_memory=False)

print(f"Total de registos em Taxonomia: {df_taxon.shape[0]}")
print(f"Total de registos em Distribuição: {df_dist.shape[0]}")

print("\n==================================================")
print(" 2. TRATAMENTO E CRUZAMENTO DE DADOS")
print("==================================================")

# Cruzamento das bases através da chave 'id' (taxon_id)
df_merged = pd.merge(
    df_dist[['id', 'countryCode', 'threatStatus']],
    df_taxon[['id', 'scientificName', 'kingdom', 'phylum', 'class', 'order', 'family', 'taxonRank']],
    on='id',
    how='inner'
)

# Remoção de duplicados para garantir unicidade analítica
df_merged = df_merged.drop_duplicates(subset=['id'])
print(f"Total de espécies únicas após consolidação: {df_merged.shape[0]}")

print("\n==================================================")
print(" 3. MÉTRICAS DE NEGÓCIO (DO DASHBOARD)")
print("==================================================")

total_especies = df_merged['id'].nunique()
print(f"• Total de Espécies Catalogadas: {total_especies}")

status_counts = df_merged['threatStatus'].value_counts()
print("\n• Espécies por Status de Ameaça:")
print(status_counts)

phylum_counts = df_merged['phylum'].value_counts()
print("\n• Top Filos mais representados:")
print(phylum_counts.head(5))

print("\n==================================================")
print(" Análise Exploratória concluída com sucesso!")
print("==================================================")