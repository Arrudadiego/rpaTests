import os
import sys
import smtplib
import ssl
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv

def get_directory():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    elif __file__:
        return os.path.dirname(os.path.abspath(__file__))
    return os.getcwd()

def analyze_quotes(csv_file='quotes.csv'):

    diretorio = get_directory()
    
    path = os.path.join(diretorio, csv_file)
    
    try:
        df = pd.read_csv(path, encoding='utf-8')
        
        total_quotes = len(df)
        
        autor_counts = df['Author'].value_counts()
        recurring_autor = autor_counts.index[0]
        autor_count = autor_counts.iloc[0]
        
        df['Tags'] = df['Tags'].str.split(', ')
        
        tags_series = df.explode('Tags')['Tags']
        tag_counts = tags_series.value_counts()
        
        most_tag = tag_counts.index[0]
        tag_count = tag_counts.iloc[0]
        
        #conteudo do relatorio
        summary = f"""
Relatório de Análise de Citações:

- Total de citações: {total_quotes}
- Autor mais recorrente: {recurring_autor} (com {autor_count} citações)
- Tag mais utilizada: '{most_tag}' (com {tag_count} ocorrências)
"""
        return summary, path
    
    except FileNotFoundError:
        print(f"Erro: Arquivo {path} não encontrado.")
        return None, None
    except Exception as e:
        print(f"Ocorreu um erro durante a análise: {e}")
        return None, None

def email_report(summary, csv_path):
    #load das variaveis de ambiente
    load_dotenv()
    
    #credenciais do remetente
    email_sender = os.getenv('EMAIL_USER')
    email_password = os.getenv('EMAIL_PASS')
    
    #emails dos destinatários
    destinatarios = [
        'paulo.andre@parvi.com.br', 
        'thiago.jose@parvi.com.br'
    ]
    
    #configs do servidor SMTP do gmail
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    
    try:
        #conexao segura com o servidor SMTP 
        context = ssl.create_default_context()
        
        #iniciar conexão com SMTP
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls(context=context)
            server.login(email_sender, email_password)
            
            #envio do email
            for receiver in destinatarios:
                #criacao do email
                message = MIMEMultipart()
                message['From'] = email_sender
                message['To'] = receiver
                message['Subject'] = 'Relatório - Extração Quotes'
                
                #texto do email
                body = f"""
Olá,

Segue relatório de citações extraídas:

{summary}

Anexo: Arquivo completo de citações em CSV.

Atenciosamente,
Diego Arruda
"""
                message.attach(MIMEText(body, 'plain'))
                
                #colocar o arquivo em anexo
                with open(csv_path, 'rb') as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                
                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition', 
                    f'attachment; filename= quotes.csv'
                )
                message.attach(part)
                
                server.sendmail(email_sender, receiver, message.as_string())
                print(f'E-mail enviado com sucesso para {receiver}')
        
        return True
    
    except Exception as e:
        print(f'Erro ao enviar e-mail: {e}')
        return False

def main():
    #fazer a analise das citacoes e gerar o resumo
    summary, csv_path = analyze_quotes()
    
    if summary and csv_path:
        email_enviado = email_report(summary, csv_path)
        
        if email_enviado:
            print("Relatório enviado com sucesso!")
        else:
            print("Falha no envio do relatório.")
    else:
        print("Não foi possível gerar o relatório.")

if __name__ == '__main__':
    main()