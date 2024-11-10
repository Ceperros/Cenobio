# archivo: Scraper.py
from MethodC import MethodC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from transformers import pipeline
import time

class Scraper:
  

    def __init__(self, url):
        self.url = url
        self.driver = self._initialize_driver()
    
    def _initialize_driver(self):
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        return webdriver.Chrome(service=service, options=options)
    
    def scrape_links(self):
        self.driver.get(self.url)
        headlines = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'h2, h1'))
        )
        links = []
        for headline in headlines:
            try:
                link_element = headline.find_element(By.TAG_NAME, 'a')
                link = link_element.get_attribute('href') if link_element else 'No link'
                links.append(link)
            except:
                continue
        return links

    def scrape_article(self, link):
        self.driver.get(link)
        metodos = MethodC()
       # time.sleep(2)  # espera breve para asegurar que el contenido se haya cargado
        try:
            #Extraccion de datos
            body_element = self.driver.find_element(By.CSS_SELECTOR, '.d-the-single-wrapper__text')
            body_text = body_element.text
            title = self.driver.title
            
            
           
        
            # Capturar el autor usando BeautifulSoup para analizar el HTML
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            description = soup.find('meta', attrs={'name': 'description'})
            description = description['content'] if description else 'No description found'
            date_published = soup.find('meta', attrs={'property': 'article:published_time'})
            date_published = date_published['content'] if date_published else 'No publication date found'
            keywords = soup.find('meta', attrs={'name': 'keywords'})
            keywords = keywords['content'] if keywords else 'No keywords found'
            author = soup.select_one('.the-by__permalink')  # Ajustar selector según sea necesario
            sentiment_analysis = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
            sentiment = sentiment_analysis(body_text)[0] 
            return {
                'title': title,
                'link': link,
                'body': body_text,
                'description': description,
                'keywords': keywords,
                'date_published': date_published,
                'author': author.text if author else 'Desconocido',
                'label': metodos.asignar_label(body_text),              
                'sentiment': sentiment
            }
        except Exception as e:
            print(f"Error al obtener el artículo: {e}")
            return None

    def close(self):
        self.driver.quit()
