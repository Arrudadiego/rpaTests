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
from rpa1 import get_script_directory
from rpa2 import analyze_quotes


#funcao para enviar o relatorio por email
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