import spacy
import pytextrank
from fastapi import Form, FastAPI
from controllers.rank import Rank

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
