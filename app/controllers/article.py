from newspaper import Article
from controllers.rank import Rank
from controllers.entities import Entities

"""
PROCESSAR URL E ARTIGO PARA INDEXAÇÃO
"""

class ParseArticle:
    def __init__(self, nlp, url: str, html: str):
        self.nlp = nlp
        self.url = url
        self.html = html

    def run(self):
        article = Article(self.url, language='pt')
        article.download(input_html=self.html)
        article.parse()
        return {
            "url": article.url,
            "date": article.publish_date,
            "title": article.title,
            "desc": article.meta_description,
            "text": article.text,
            "image": article.top_image,
            "images": article.images,
            "nlp": Rank(self.nlp, article.text).run(),
            "entities": Entities(self.nlp, article.text).run()
        }
