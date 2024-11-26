# RPA Python Challenge

Este projeto é uma solução para o desafio de Automação de Processos com Python (RPA), que tem como objetivo extrair e analisar dados de citações de um site web.

## Descrição

O projeto consiste em três partes principais:

1. **Web Scraping com Selenium**: Automação do processo de extração de citações, autores e tags desse [site](https://quotes.toscrape.com/js-delayed/).
2. **Processamento de Dados com Pandas**: Análise dos dados extraídos, incluindo a identificação do autor mais recorrente e da tag mais utilizada.
3. **Envio de Relatório por E-mail**: Envio do arquivo CSV contendo os dados extraídos, juntamente com o relatório de análise, para os e-mails especificados.

## Estrutura do Projeto

O projeto possui a seguinte estrutura de arquivos:
rpaTests/
.env
.env.example
.gitignore
README.md
requirements.txt
rpa1.py
rpa2.py
rpa3.py
- `.env`: Arquivo com as credenciais de e-mail (não compartilhado).
- `.env.example`: Arquivo de exemplo com a estrutura das variáveis de ambiente.
- `.gitignore`: Arquivo que define quais arquivos devem ser ignorados pelo Git.
- `README.md`: Este arquivo, com informações sobre o projeto.
- `requirements.txt`: Arquivo com as dependências do projeto.
- `rpa1.py`: Script responsável pelo web scraping.
- `rpa2.py`: Script responsável pela análise dos dados.
- `rpa3.py`: Script responsável pelo envio do relatório por e-mail.

## Pré-requisitos

- Python 3.x
- Pacotes Python:
  - `selenium`
  - `pandas`
  - `python-dotenv`

## Instalação

1. Crie um ambiente virtual Python:
   - Windows: `python -m venv .venv`
   - macOS/Linux: `python3 -m venv .venv`
2. Ative o ambiente virtual:
   - Windows: `.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`
3. Instale as dependências do projeto:
   - `pip install -r requirements.txt`
4. Crie o arquivo `.env` com suas credenciais de e-mail:
   - Copie o conteúdo do `.env.example` e preencha com seus valores reais.

## Uso

1. Execute o script `rpa1.py` para realizar o web scraping:
   - `python rpa1.py`
2. Execute o script `rpa2.py` para processar os dados e enviar o relatório por e-mail:
   - `python rpa2.py`

## Considerações Finais

- Organizei esse projeto tentando as melhores práticas de desenvolvimento, com uma estrutura de arquivos clara e boas práticas de segurança (como o uso de um arquivo `.env` para armazenar credenciais).
- O código está dividido em funções, facilitando a manutenção e a adição de novas funcionalidades.
- O envio de e-mail é realizado de forma automática, simplificando o processo de compartilhamento dos resultados.

Sinta-se à vontade para entrar em contato caso tenha alguma dúvida ou sugestão de melhoria para o projeto.
