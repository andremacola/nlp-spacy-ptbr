# import uvicorn
import spacy
import pytextrank
from fastapi import Form, FastAPI
from controllers.rank import Rank
from controllers.entities import Entities

# instanciar o Flask
app = FastAPI()

# carregar spaCy, idiomas e configurações na memória
nlp = spacy.load("pt_core_news_md")
nlp.add_pipe("textrank")

# Rota de ranking dos termos
@app.post("/rank")
def rank(text: str = Form(...)):
    rank = Rank(nlp, text)
    return rank.run()

# Rota de entidade dos textos
@app.post("/entities")
def entities(text: str = Form(...)):
    entities = Entities(nlp, text)
    return entities.run()

# # Iniciar Uvicorn
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=5757)
