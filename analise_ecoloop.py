import pandas as pd

# carrega a planilha excel
df = pd.read_excel("Analise_de_Dados.xlsx")

# mostra as 5 primeiras linhas da planilha 
print("Pré-visualização dos dados:")
print(df.head())


# 'value_counts' para contar quantas vezes cada ID de máquina aparece
depositos_por_maquina = df['ID MÁQUINA'].value_counts()
print("\nDepósitos por máquina:")
print(depositos_por_maquina)


# 'sum' para somar todos os valores da coluna 'PONTOS'
total_pontos = df['PONTOS'].sum()
print(f"\nTotal de pontos distribuídos: {total_pontos}")
