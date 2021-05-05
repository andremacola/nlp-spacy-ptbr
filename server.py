import spacy
import pytextrank
from flask import Flask, jsonify, abort, request, send_from_directory, render_template
from controllers.rank import Rank

# instanciar o Flask
app = Flask(__name__)

# carregar spaCy, idiomas e configurações na memória
nlp = spacy.load("pt_core_news_md")
nlp.add_pipe("textrank")

# Rota de ranking dos termos
@app.route("/rank", methods=['GET', 'POST'])
def rank():
    params = request.form # postdata
    data = dict()

    if not 'text' in params:
        data['error'] = '[text] parameter not found'
        return jsonify(data)

    rank = Rank(nlp, params['text'])
    return rank.run()
