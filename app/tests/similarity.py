import spacy
import pathlib
import time
from icecream import ic

start_time = time.time()

for i in range(1):
  # Texto para análise
  text1 = pathlib.Path("./textos/noticia-1.txt").read_text()
  text2 = pathlib.Path("./textos/noticia-2.txt").read_text()

  # Carregar spaCy, idiomas e configurações
  nlp = spacy.load("pt_core_news_lg")

  # Rodar documento no sPacy
  doc1 = nlp(text1)
  doc2 = nlp(text2)

# Acessar dados
ic('==================== Análise de Similaridade: ====================')
ic(doc1.similarity(doc2))

ic('==================== Tempo de Execução: ====================')
def elapsed():
  return "%s seconds" % (time.time() - start_time)
ic(elapsed())
