import spacy
import pytextrank
import pathlib
import time
from icecream import ic

start_time = time.time()

for i in range(1):
  # Texto para análise
  text = pathlib.Path("./textos/hernia.txt").read_text()

  # Carregar spaCy, idiomas e configurações
  nlp = spacy.load("pt_core_news_sm")

  # Adicionar o PyTextRank na pipeline do spaCy
  nlp.add_pipe("textrank")

  # Rodar documento no sPacy
  doc = nlp(text)


# Acessar dados
ic('==================== Termos Grandes: ====================')
for phrase in doc._.phrases:
  if len(phrase.text.split()) >= 3:
    ic(phrase.rank, phrase.text)
    # ic(phrase.chunks)

ic('==================== Termos Médios: ====================')
for phrase in doc._.phrases:
  if len(phrase.text.split()) == 2:
    ic(phrase.rank, phrase.text)

ic('==================== Termos Individuais: ====================')
for phrase in doc._.phrases:
  if len(phrase.text.split()) < 2:
    ic(phrase.rank, phrase.text)


ic('==================== Tempo de Execução: ====================')
def elapsed():
  return "%s seconds" % (time.time() - start_time)
ic(elapsed())
