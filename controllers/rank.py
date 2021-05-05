from os.path import split

class Rank:
    def __init__(self, nlp, text):
        self.nlp = nlp
        self.text = text

    """
    PREPARAR RETORNO
    DOS DADOS
    """
    def data(self, doc):
        data = {
            'large': [],
            'medium': [],
            'small': []
        }

        for phrase in doc._.phrases:
            # criar objeto da palavra/sentença
            word = { 'text': phrase.text, 'rank': phrase.rank }

            # ignorar keywords com score vazio
            if phrase.rank == 0 or len(phrase.text) <= 2:
                continue

            # separar sentença/palavra por ordem de grandeza
            if len(phrase.text.split()) >= 3:
                data['large'].append(word)
            if len(phrase.text.split()) == 2:
                data['medium'].append(word)
            if len(phrase.text.split()) < 2:
                data['small'].append(word)

        return data

    """
    EXECUTAR O SPACY
    E RETORNAR OS DADOS
    """
    def run(self):
        doc = self.nlp(self.text)
        return self.data(doc)
