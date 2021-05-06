import spacy
import pathlib
import time
from icecream import ic

start_time = time.time()

for i in range(1):
  # Texto para análise
  text = pathlib.Path("./textos/bbb.txt").read_text()

  # Carregar spaCy, idiomas e configurações
  nlp = spacy.load("pt_core_news_sm")

  # Rodar documento no sPacy
  doc = nlp(text)

# Acessar dados
ic('==================== Análise Gramatical: ====================')
for token in doc:
  if token.pos_ == 'VERB':
    ic('---')
  ic(token.orth_, token.pos_)
  if token.pos_ == 'VERB':
    ic(token.lemma_)
    ic('---')

# ic('==================== Análise de Raízes: ====================')
# for token in doc:
#   if token.pos_ == 'VERB':
#     ic(token, token.lemma_)

ic('==================== Tempo de Execução: ====================')
def elapsed():
  return "%s seconds" % (time.time() - start_time)
ic(elapsed())
