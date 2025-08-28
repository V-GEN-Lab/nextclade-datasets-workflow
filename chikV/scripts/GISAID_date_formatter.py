import sys
import pandas as pd

def completar_datas(data):
    if pd.isnull(data):
        return data

    try:
        # Tenta converter a data para o formato desejado
        data_formatada = pd.to_datetime(data, errors='coerce')
        if pd.notnull(data_formatada):
            return data_formatada.strftime('%Y-%m-%d')
        else:
            return data
    except ValueError:
        # Se não for possível converter, retorna a data original
        return data

# Verifica se foram fornecidos os argumentos corretos
if len(sys.argv) != 3:
    print("Uso: python script.py caminho/do/seu/arquivo_entrada.tsv caminho/do/seu/arquivo_saida.tsv")
    sys.exit(1)

# Carregar o arquivo de entrada
caminho_arquivo_entrada = sys.argv[1]
df = pd.read_csv(caminho_arquivo_entrada, delimiter='\t')  # Assumindo um arquivo tsv

# Aplicar a função de completar datas à coluna de datas
df['date'] = df['date'].apply(completar_datas)

# Salvar o resultado em um novo arquivo TSV
caminho_arquivo_saida = sys.argv[2]
df.to_csv(caminho_arquivo_saida, sep='\t', index=False)

print(f'Arquivo de metadados com correção de datas salvo como: "{caminho_arquivo_saida}"')
