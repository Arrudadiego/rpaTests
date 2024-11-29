# RPA Python Challenge

Este projeto é uma solução para o desafio de Automação de Processos com Python (RPA), que tem como objetivo extrair e analisar dados de citações de um site web, além de enviar os resultados por e-mail.

## 🚀 Funcionalidades

1. **Web Scraping com Selenium**:
   - Automação do processo de extração de citações, autores e tags do site [quotes.toscrape.com](https://quotes.toscrape.com/js-delayed/).

2. **Processamento de Dados com Pandas**:
   - Análise dos dados extraídos, incluindo:
     - Total de citações.
     - Autor mais recorrente.
     - Tag mais utilizada.

3. **Envio de Relatório por E-mail**:
   - Envio do arquivo CSV com os dados extraídos e o relatório gerado para os e-mails especificados.

---

## 📂 Estrutura do Projeto

```plaintext
rpaTests/
├── .env                # Arquivo com as credenciais de e-mail (não compartilhado)
├── .env.example        # Exemplo de estrutura para o arquivo .env
├── .gitignore          # Arquivo que define arquivos ignorados pelo Git
├── README.md           # Documentação do projeto (este arquivo)
├── requirements.txt    # Dependências do projeto
├── rpa1.py             # Script para o web scraping
├── rpa2.py             # Script para análise dos dados
└── rpa3.py             # Script para envio do relatório por e-mail
```

## Pré-requisitos

- Python 3.x
- Pacotes Python:
  - `selenium`
  - `pandas`
  - `python-dotenv`
  - `webdriver-manager`

## Instalação

**1. Crie um ambiente virtual Python:**
   - **Windows**:
     ```
     python -m venv .venv
     .venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```
     python3 -m venv .venv
     source .venv/bin/activate
     ```

**2. Instale as dependências do projeto:**
   - ``` pip install -r requirements.txt ```


**3. Configure as credenciais de e-mail:**
- Crie o arquivo `.env` a partir do `.env.example`:
  ```
  cp .env.example .env
  ```
- Preencha o `.env` com suas credenciais de e-mail.

## Uso

**1. Execute o script `rpa1.py` para realizar o web scraping:**
  - ```python rpa1.py ```
  - Gera o arquivo `quotes.csv` com as citações extraídas.

**2. Execute o script `rpa2.py` para processar os dados:**
  - ```python rpa2.py```
  - Exibe a análise no console.
  - Gera o relatório `analiseQuotesCsv.txt`.

**3. Execute o script `rpa3.py` para enviar o relatório por e-mail:**
  -```python rpa3.py```
  - Envia o relatório gerado e o arquivo `quotes.csv` para os destinatários especificados.

## Considerações Finais

- Organizei este projeto seguindo as melhores práticas de desenvolvimento:
- **Estrutura modular**: cada funcionalidade está em um script separado.
- **Segurança**: o arquivo `.env` protege credenciais sensíveis.
- **Organização**: o código está limpo e fácil de manter.

- O envio de e-mails é automático, simplificando o compartilhamento de resultados.

**Caso tenha dúvidas ou sugestões de melhoria, entre em contato.**
