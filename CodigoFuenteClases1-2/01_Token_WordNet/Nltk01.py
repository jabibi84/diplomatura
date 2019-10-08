#############################################################################
#Ejemplos extraidos del libro Python Text Processing with NLTK 2.0 Cookbook.
#Autor Jacob Perkins. Editorial Packt Publishing.
#Referidos al capitulo 1.
#############################################################################

#Importar libreria NLTK para acceder a su funcionalidad.
import nltk

print("01 Tokenization: Separación en oraciones:")
print("Definicion: Es la acción de dividir un texto en unidades llamadas tokens")
para = """Hello World. It's good to see you. Thanks for buying this book."""
sent = nltk.sent_tokenize(para)
print("Oración original: " + para)
print("Método Utilizado: nltk.sent_tokenize()")
print("Oración 1: " +  sent[0])
print("Oración 2: " +  sent[1])
print("Oración 3: " +  sent[2])
print("--------------------------------------\n")

print("02 Tokenization: Separación en oraciones, según el lenguaje:")
sentence = 'Hola amigo. Estoy bien.'
print("Oración original: " + sentence)
spanish_tokenizer = nltk.data.load('tokenizers/punkt/spanish.pickle')
spanish_tokens = spanish_tokenizer.tokenize(sentence)
print("Método de carga: nltk.data.load('tokenizers/punkt/spanish.pickle')")
print("Método Utilizado: spanish_tokenizer.tokenize()")
print("Oración 1: " +  spanish_tokens[0])
print("Oración 2: " +  spanish_tokens[1])
print("--------------------------------------\n")

print("03 Tokenization: Separación en palabras:")
sentence = """At eight o'clock on Thursday morning Arthur didn't feel very good."""
print("Oración original: " + sentence)
print("Método Utilizado: nltk.word_tokenize()")
tokens = nltk.word_tokenize(sentence)
print("Vector de tokens:")
print(tokens)
print("--------------------------------------\n")

print("04 Tokenization: Separación en palabras mediante expresiones regulares:")
print("Oración original: " + sentence)
print("Método Utilizado: nltk.regexp_tokenize()")
reg_exp_tokens = nltk.tokenize.regexp_tokenize(sentence, "[\w']+")
print("Vector de tokens de regex:")
print(reg_exp_tokens)
print("--------------------------------------\n")

print("05 Tokenization: Separación en palabras mediante expresiones regulares definiendo el espacio como separador:")
print("Oración original: " + sentence)
print("Método Utilizado: nltk.regexp_tokenize()")
reg_exp_tokens = nltk.tokenize.regexp_tokenize(sentence, '\s+', gaps=True)
print("Vector de tokens de regex definiendo el espacio como separador:")
print(reg_exp_tokens)
print("--------------------------------------\n")

print("06 Stopwords:")
print("Definicion: Son palabras que no contribuyen al sentido de la oración")
print("Oración original: " + "Can't is a contraction")
print("Método Utilizado: nltk.corpus.stopwords.words")
english_stops = set( nltk.corpus.stopwords.words('english'))
english_stops.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}'])
words = ["Can't", 'is', 'a', 'contraction']
print("Stopwordse + update:")
print(english_stops)
for i in words:
    if i.lower() not in english_stops:
        print("No Stopwords: " + i)
print("--------------------------------------\n")

print("07 Stopwords en español:")
print("Oración original: " + "Cantar es un verbo")
print("Método Utilizado: nltk.corpus.stopwords.words")
spanish_stops = set( nltk.corpus.stopwords.words('spanish'))
spanish_stops.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}'])
words = ["Cantar", 'es', 'un', 'verbo']
print("Stopwordse + update:")
print(spanish_stops)
for i in words:
    if i.lower() not in spanish_stops:
        print("No Stopwords: " + i)
print("--------------------------------------\n")

print("08 Wordnet: Generico:")
print("Definicion: Es un diccionario en ingles orientado semánticamente")
print("Ubicación: C:\nltk_data\corpora\omw\spa")
print("Wordnet Utilizado: " + "motorcar")
print("Método Utilizado: nltk.corpus.wordnet.synsets()")
syns = nltk.corpus.wordnet.synsets('motorcar')
print(syns[0].name() + " (Es la primera definicion del sustantivo car)")
print(syns)
print("--------------------------------------\n")

print("09 Wordnet: Detalle:")
print("Wordnet Utilizado: " + "car.n.01")
print("Método Utilizado: nltk.corpus.wordnet.synset('car.n.01')hyponyms()")
syns = nltk.corpus.wordnet.synset('car.n.01')
print("Lista de entradas para car")
print(syns.hyponyms())
print("--------------------------------------\n")

print("10 Wordnet Español:")
print("Wordnet Utilizado: " + "car")
print("Método Utilizado: nltk.corpus.wordnet.synset()")
syns = nltk.corpus.wordnet.synsets('car')
print("Lista de entradas en español")
print(syns[0].lemma_names('spa'))
print("--------------------------------------\n")

print("11 Wordnet Entradas:")
print("Wordnet Utilizado: " + "great")
print("Método Utilizado: nltk.corpus.wordnet.synset()")
print("Lista de entradas great:" )
print(nltk.corpus.wordnet.synsets('great'))
print("Total:       " + str(len(nltk.corpus.wordnet.synsets('great'))))
print("Sustantivos: " + str(len(nltk.corpus.wordnet.synsets('great', pos='n'))))
print("Adjetivos:   " + str(len(nltk.corpus.wordnet.synsets('great', pos='a'))))
print("--------------------------------------\n")

print("12 Wordnet Similitud:")
print("Wordnet Utilizado: " + "cookbook & instruction_book")
print("Método Utilizado: nltk.corpus.wordnet.wup_similarityt()")
cb = nltk.corpus.wordnet.synset('cookbook.n.01')
ib = nltk.corpus.wordnet.synset('instruction_book.n.01')
print("Similaridad: " + str(cb.wup_similarity(ib)))
print("--------------------------------------\n")

print("13 Wordnet Comparacion de Verbos:")
print("Wordnet Utilizado: " + "cook & bake")
print("Método Utilizado: nltk.corpus.wordnet.wup_similarityt()")
cb = nltk.corpus.wordnet.synset('cook.v.01')
ib = nltk.corpus.wordnet.synset('bake.v.01')
print("Similaridad: " + str(cb.wup_similarity(ib)))
print("--------------------------------------\n")

print("14 Collocations:")
print("Definicion: Son dos o más palabras que tienden a aparecer con frecuencia juntos")
print("Método Utilizado: nltk.collocations.BigramCollocationFinder.from_words()")
print("Busqueda de Frecuencia de Bigrams")
print("Archivo a evaluar: C:\\nltk_data\\corpora\\webtext\\grail.txt")
words = [w.lower() for w in nltk.corpus.webtext.words('grail.txt')]
bcf = nltk.collocations.BigramCollocationFinder.from_words(words)
print(bcf.nbest(nltk.collocations.BigramAssocMeasures.likelihood_ratio, 4))
print("--------------------------------------\n")

print("15 Collocations:")
print("Método Utilizado: nltk.collocations.BigramCollocationFinder.from_words()")
print("Busqueda de Frecuencia de Trigrams")
print("Archivo a evaluar: C:\\nltk_data\\corpora\\webtext\\singles.txt")
stopset = set(nltk.corpus.stopwords.words('english'))
filter_stops = lambda w: len(w) < 3 or w in stopset
words = [w.lower() for w in nltk.corpus.webtext.words('singles.txt')]
tcf = nltk.collocations.TrigramCollocationFinder.from_words(words)
tcf.apply_word_filter(filter_stops)
tcf.apply_freq_filter(3)
print(tcf.nbest(nltk.collocations.TrigramAssocMeasures.likelihood_ratio, 4))
print("--------------------------------------\n")