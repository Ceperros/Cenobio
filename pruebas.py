from transformers import pipeline

# Configurar el pipeline de análisis de sentimientos
sentiment_analysis = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

# Probar el pipeline
result = sentiment_analysis("¡Este es un excelente producto!")
print(result)