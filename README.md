# nlp

Serviço de extração de artigos, ranking de keywords e entidades para o Easy Content

## Utilização:

- De preferência, instale e ative uma virtualenv com python3
- Instale as dependencias dentro da virtualenv com o `pip install -r requirements.txt`
- Rode dentro da pasta ***app*** `uvicorn main:app --host 0.0.0.0 --reload --port 5757`
- Entre em `http://localhost:5757/docs` e veja as rotas da API

## OBS:

- Será necessário copiar/importar o `syntax_iterators` do *espanhol*.

### Método 1

- Para isso copie o arquivo `syntax_iterators` localizado em `site-packages -> spacy -> lang -> es` para a pasta `pt`
- Depois importe no `__init__` do idioma PT declarando `tokenizer_exceptions = TOKENIZER_EXCEPTIONS` na classe `PortugueseDefaults`

### Método 2

Você poderá copiar os arquivos do spaCy contidos neste repositório para o pacote do spaCy da virtualenv.

- `cp spacy/lang/pt/syntax_iterators.py ~/.virtualenvs/nlp/lib/python3.9/site-packages/spacy/lang/pt`
- `cp spacy/lang/pt/__init__.py ~/.virtualenvs/nlp/lib/python3.9/site-packages/spacy/lang/pt`
