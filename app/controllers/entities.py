from os.path import split

class Entities:
    def __init__(self, nlp, text):
        self.nlp = nlp
        self.text = text

    """
    REMOVER DUPLICADOS
    """
    def remove_dup(self, a):
        i = 0
        while i < len(a):
            j = i + 1
            while j < len(a):
                if a[i] == a[j]:
                    del a[j]
                else:
                    j += 1
            i += 1

    """
    PREPARAR RETORNO
    DOS DADOS
    """
    def data(self, doc):
        data = []
        dups = []

        for entity in doc.ents:
            if str(entity) not in dups: # entity não é uma string, por isso usar o str()
                data.append({ "entity": str(entity), "label": entity.label_})
                dups.append(str(entity))

        return data

    """
    EXECUTAR O SPACY
    E RETORNAR OS DADOS
    """
    def run(self):
        doc = self.nlp(self.text)
        return self.data(doc)
