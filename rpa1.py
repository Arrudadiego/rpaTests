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

def setup_driver():
    options = webdriver.ChromeOptions()  
    options.add_argument('--headless')  
    options.add_argument('--lang=en-US') 
    return webdriver.Chrome(options=options)

def scrape_quotes(driver):
    #lista que ira armazenar os dados
    quotes_data = [] 
    
    #wait para carregar as citações
    quote_elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'quote'))
    )
    
    for quote_element in quote_elements:
        #encontra e extrai o texto
        quote_text = quote_element.find_element(By.CLASS_NAME, 'text').text
        
        #encontra e extrai o autor
        author = quote_element.find_element(By.CLASS_NAME, 'author').text
        
        #encontra e extrai as tags
        tags_elements = quote_element.find_elements(By.CLASS_NAME, 'tag')
        tags = [tag.text for tag in tags_elements]  # Converte tags para lista
        
        #adiçao na lista
        quotes_data.append({
            'Quote': quote_text,
            'Author': author,
            'Tags': ', '.join(tags)
        })
    
    return quotes_data

def save_to_csv(quotes_data, filename='quotes.csv'):
    
    #define a ordem das colunas
    keys = quotes_data[0].keys()
    
    #abre o arquivo csv
    with open(filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
        #escritor csv
        writer = csv.DictWriter(csvfile, fieldnames=keys)       
        writer.writeheader()
        writer.writerows(quotes_data)

def main():
    #driver do navegador
    driver = setup_driver()
    
    try:
        #ida ao site
        driver.get('https://quotes.toscrape.com/js-delayed/')
        time.sleep(5)
        quotes_data = scrape_quotes(driver)        
        save_to_csv(quotes_data)
        
        #print em caso de sucesso
        print(f"Foram extraidas com sucesso {len(quotes_data)} citações")
    
    finally:
        #encerra o driver
        driver.quit()

#chamada da função main
if __name__ == '__main__':
    main()