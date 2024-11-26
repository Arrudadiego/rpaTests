import os
import sys
import pandas as pd

def get_script_directory():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    elif __file__:
        return os.path.dirname(os.path.abspath(__file__))
    return os.getcwd()

def analyze_quotes(csv_file='quotes.csv'):

    #diretório do script
    diretorio = get_script_directory()
    
    #path para o arquivo csv
    path = os.path.join(diretorio, csv_file)
    
    try:
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
        
        #relatorio da análise
        report_path = os.path.join(diretorio, 'analiseQuotesCsv.txt')
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write("Relatório de Análise de Citações \n\n")
            f.write(f"Total de citações: {total_quotes}\n")
            f.write(f"Autor mais recorrente: {recurring_autor} (com {autor_count} citações)\n")
            f.write(f"Tag mais utilizada: '{most_tag}' (com {tag_count} ocorrências)\n")
        
        print(f"\nRelatório salvo em: {report_path}")
    
    except FileNotFoundError:
        print(f"Erro: Arquivo {path} não encontrado.")
        print("Certifique-se de que o arquivo 'quotes.csv' existe no mesmo diretório do script.")
    except Exception as e:
        print(f"Ocorreu um erro durante a análise: {e}")

def main():
    analyze_quotes()

if __name__ == '__main__':
    main()