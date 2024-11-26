#import de libs
import os 
import sys
import io
from selenium import webdriver
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC 
import csv 
import time 

#fiz essa funcao para o arquivo csv ficar na mesma pasta em que o terminal estiver
def get_script_directory():
    #pegar a pasta em que esta o script atual
    if getattr(sys, 'frozen', False):
        #olha se é um executavel compilado
        return os.path.dirname(sys.executable)
    elif __file__:
        #verifica se é um script python
        return os.path.dirname(os.path.abspath(__file__))
    
    #volta para o diretório atual
    return os.getcwd()

def setup_driver():
    options = webdriver.ChromeOptions()  
    options.add_argument('--headless')  
    options.add_argument('--lang=en-US') 
    return webdriver.Chrome(options=options)

def scrape_quotes(driver):
    #lista que ira armazenar os dados
    list = [] 
    
    #wait para carregar as citacoes
    citacoes = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'quote'))
    )
    
    for quote_element in citacoes:
        #encontra e extrai o texto
        texto = quote_element.find_element(By.CLASS_NAME, 'text').text
        
        #encontra e extrai o autor
        autor = quote_element.find_element(By.CLASS_NAME, 'author').text
        
        #encontra e extrai as tags
        tags_elements = quote_element.find_elements(By.CLASS_NAME, 'tag')
        tags = [tag.text for tag in tags_elements]  # Converte tags para lista
        
        #adiçao na lista
        list.append({
            'Quote': texto,
            'Author': autor,
            'Tags': ', '.join(tags)
        })
    
    return list

def save_to_csv(list, filename='quotes.csv'):

    #pega o diretorio do script
    diretorio = get_script_directory()
    
    #path para salvar o arquivo
    path = os.path.join(diretorio, filename)
    
    #define a ordem das colunas
    keys = list[0].keys()
    
    #abre o arquivo csv
    with open(filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
        #escritor csv
        writer = csv.DictWriter(csvfile, fieldnames=keys)       
        writer.writeheader()
        writer.writerows(list)

def main():
    #driver do navegador
    driver = setup_driver()
    
    try:
        #ida ao site
        driver.get('https://quotes.toscrape.com/js-delayed/')
        time.sleep(5)
        list = scrape_quotes(driver)        
        save_to_csv(list)
        
        #print em caso de sucesso
        print(f"Foram extraidas com sucesso {len(list)} citações")
    
    finally:
        #encerra o driver
        driver.quit()

#chamada da funcao main
if __name__ == '__main__':
    main()