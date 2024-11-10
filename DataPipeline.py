# archivo: DataPipeline.py

import json
from MongoDBClient import MongoDBClient
from Scraping import Scraper
import os

class DataPipeline:
    def __init__(self, mongo_uri, db_name, url):
        self.db_client = MongoDBClient(mongo_uri, db_name)
        self.scraper = Scraper(url)
        self.news_data = []  # Lista para almacenar todas las noticias
    
    def process_data(self, collection_name):
        links = self.scraper.scrape_links()
        for link in links:
            article_data = self.scraper.scrape_article(link)
            if article_data:
                self.news_data.append(article_data)  # Agregar cada artículo a la lista

    def save_to_json(self, file_path):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(self.news_data, f, ensure_ascii=False, indent=4)
        print(f"Datos guardados en '{file_path}'")

    def save_to_mongodb(self, collection_name):
        for article_data in self.news_data:
            self.db_client.insert_document(collection_name, article_data)
    
    def close_connections(self):
        self.scraper.close()
        self.db_client.close_connection()
