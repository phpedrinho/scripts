import sys
from pathlib import Path
import pandas as pd

# Verifica se pelo menos o arquivo foi informado
if len(sys.argv) < 2:
    print("Uso: python converter.py <arquivo.xlsx> [valor_departamento]")
    sys.exit(1)

# Caminho do arquivo Excel
arquivo_excel = Path(sys.argv[1])

# Verifica se o arquivo existe
if not arquivo_excel.exists():
    print(f"Erro: O arquivo '{arquivo_excel}' não foi encontrado.")
    sys.exit(1)

# Nome do CSV de saída
arquivo_csv = arquivo_excel.with_suffix(".csv")

# Lê a planilha
df = pd.read_excel(arquivo_excel)

# Se foi informado um segundo parâmetro, concatena ao departamento
if len(sys.argv) >= 3:
    df["Departamento"] = (
    sys.argv[2]  + "_" + df["Departamento"].astype(str)
)

# # Seleciona as colunas desejadas e salva em CSV
df[["Email", "Nome", "Departamento"]].to_csv(
    arquivo_csv,
    index=False,
    header=False,
    sep=",",
    encoding="utf-8-sig"
)

print(f"Conversão concluída!")
print(f"Arquivo gerado: {arquivo_csv}")