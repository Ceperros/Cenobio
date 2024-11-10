# archivo: main.py

from DataPipeline import DataPipeline
from LoadingAnimation import LoadingAnimation

def main():
    mongo_uri = "mongodb://localhost:27017/"
    db_name = "test"
    url = "https://elmostrador.cl"
    collection_name = "news_articles"
    json_file_path = "C:/Scrping/news_data.json"

    # Iniciar animación de carga
    loading_animation = LoadingAnimation("Scraping en proceso")
    loading_animation.start()

    try:
        pipeline = DataPipeline(mongo_uri, db_name, url)
        
        # Ejecutar scraping y guardar en JSON
        pipeline.process_data(collection_name)
        pipeline.save_to_json(json_file_path)
        
        # Guardar en MongoDB
        pipeline.save_to_mongodb(collection_name)
        
        pipeline.close_connections()
        print("Proceso completado: Datos guardados en JSON y MongoDB.")
    finally:
        # Detener animación de carga
        loading_animation.stop()

if __name__ == "__main__":
    main()
