import spacy
import pathlib
import time
from icecream import ic

start_time = time.time()

def remove_dup(a):
   i = 0
   while i < len(a):
      j = i + 1
      while j < len(a):
         if a[i] == a[j]:
            del a[j]
         else:
            j += 1
      i += 1

for i in range(1):
  # Texto para análise
  text = pathlib.Path("./textos/noticia-2.txt").read_text()

  # Carregar spaCy, idiomas e configurações
  nlp = spacy.load("pt_core_news_md")

  # Rodar documento no sPacy
  doc = nlp(text)


# Acessar dados
ic('==================== Entidades: ====================')
dups = []
for entity in doc.ents:
  if str(entity) not in dups: # entity não é uma string, por isso usar o str()
    ic(entity, entity.label_)
    dups.append(str(entity))


ic('==================== Tempo de Execução: ====================')
def elapsed():
  return "%s seconds" % (time.time() - start_time)
ic(elapsed())
