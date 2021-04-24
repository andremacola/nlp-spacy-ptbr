# nlp-spacy-ptbr

Experimentos em PT-BR com NLP utilizando spaCy

## Utilização:

- De preferência, instale e ative uma virtualenv com python3
- Instale as dependencias dentro da virtualenv com o `pip install -r requirements.txt`
- **OBS:** Será necessário copiar/importar o `syntax_iterations` do *espanhol*. Para isso copie o arquivo `syntax_iterations` localizado em `site-packages -> spacy -> lang -> es` para a pasta `pt` e depois importe no `__init__` do idioma PT declarando `tokenizer_exceptions = TOKENIZER_EXCEPTIONS` na classe `PortugueseDefaults`
- Rode com `python ./src/rank.py` ou qualquer outro arquivo no src/
