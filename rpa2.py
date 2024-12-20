import os
import sys
import pandas as pd
from rpa1 import get_script_directory


def analyze_quotes(csv_file='quotes.csv'):

    #diretorio do script
    diretorio = get_script_directory()
    
    #path para o arquivo csv
    path = os.path.join(diretorio, csv_file)
    
    try:
        if not os.path.exists(path):
            print(f"Erro: Arquivo {path} não encontrado.")
            return None, None
        
        df = pd.read_csv(path, encoding='utf-8')
        
        #analise de citações
        total_quotes = len(df)
        print("Análise de Citações")
        print(f"Número total de citações: {total_quotes}")

        #contagem do autor mais recorrente
        autor_counts = df['Author'].value_counts()
        recurring_autor =autor_counts.index[0]
        autor_count =autor_counts.iloc[0]
        print(f"\nAutor mais recorrente: {recurring_autor}")
        print(f"Número de citações do autor: {autor_count}")
        
        #tirando as tags de uma string e separando em listas
        df['Tags'] = df['Tags'].str.split(', ')       
        #separa as tags em linhas
        tags_series = df.explode('Tags')['Tags']
        tag_counts = tags_series.value_counts()
        
        #contagem da tag mais utilizada
        most_tag = tag_counts.index[0]
        tag_count = tag_counts.iloc[0]
        print(f"\nTag mais utilizada: '{most_tag}'")
        print(f"Número de ocorrências: {tag_count}")

        summary = f"""
Relatório de Análise de Citações:

- Total de citações: {total_quotes}
- Autor mais recorrente: {recurring_autor} (com {autor_count} citações)
- Tag mais utilizada: '{most_tag}' (com {tag_count} ocorrências)
"""
        return summary, path
                
    except FileNotFoundError:
        print(f"Erro: Arquivo {path} não encontrado.")
        print("Certifique-se de que o arquivo 'quotes.csv' existe no mesmo diretório do script.")
    except Exception as e:
        print(f"Ocorreu um erro durante a análise: {e}")
    except pd.errors.EmptyDataError:
        print(f"Erro: Arquivo {path} está vazio ou corrompido.")
        return None, None

def main():
    analyze_quotes()

if __name__ == '__main__':
    main()