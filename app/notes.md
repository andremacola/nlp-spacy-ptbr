## WORKFLOW

- primeiro extrai
- verifica termos longos em relação aos termos mais curtos e elimina os curtos quando viável
- Tenta extrair uma sigla. Ex: se ele encontrar o termo "Instituto Brasileiro de Geografia e Estatística", pega-se a primeira letra de cada palavra (eliminando preposições e verbos de ligação) e monta "IBGE", logo após se verifica se IBGE é uma palavra-chave encontrada
- Verifica se cada palavra com ranking superior a X (termos grandes levam prioridade) existem relacionadas no publisher. Se tiver, marca como uma palavra-chave válida para "relacionadas"
- Verifica se cada palavra com ranking superior a X (termos grandes levam prioridade) existem na wikipedia. Se tiver, marca como uma palavra-chave válida favorita para "relacionadas"
- No publisher, encontrar uma forma de rankear as palavras/termos-chaves mais encontrados nas matérias. Essas palavras serão "vips" e marcadas sempre que forem encontradas
- Cruzar palavras com o título
- OBS: Eliminar/Agrupar plural. Ex: hérnia, hérnias


## NOTAS

- Palavras como 'investigados' podem ser consideradas verbos de acordo com o contexto.
	- Ex: que eles sejam investigados (verbo)
	- Ex: Os investigados são (substantivo)

- As relacionadas podem ser mais assertivas cruzando o termo da palavra-chave com as entidades (que podem ser consideradas tags)

## SPACY

Substituir pasta `lang`

`cp spacy/lang/pt/syntax_iterators.py ~/.virtualenvs/nlp/lib/python3.9/site-packages/spacy/lang/pt`
`cp spacy/lang/pt/__init__.py ~/.virtualenvs/nlp/lib/python3.9/site-packages/spacy/lang/pt`
