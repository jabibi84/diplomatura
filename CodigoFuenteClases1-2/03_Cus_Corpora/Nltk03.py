#############################################################################
#Ejemplos extraidos del libro Python Text Processing with NLTK 2.0 Cookbook.
#Autor Jacob Perkins. Editorial Packt Publishing.
#Referidos al capitulo 3.
#############################################################################

#Importar libreria NLTK para acceder a su funcionalidad.
import nltk

print("01 Corpus: Cargar diccionario propio")
import os, os.path
path = os.path.expanduser('c:/nltk_data')
print(os.path.exists(path))
mywords = nltk.data.load('corpora/cookbook/mywords.txt', format='raw')
print("Listado de palabras:")
print(mywords)
print("--------------------------------------\n")


print("02 Corpus: Cargar diccionario propio Modo 2")
from nltk.corpus.reader import WordListCorpusReader
reader = WordListCorpusReader('.', ['wordlist'])
print("Almacenado en un array")
print(reader.words())
print("Almacenado en texto")
print(reader.raw())
print("--------------------------------------\n")

print("03 Part-of-speech:")
print("El etiquetado de parte del habla es el proceso por el cual se identifica la etiqueta para una palabra.")
print("Ejemplo: The/at-tl expense/nn and/cc time/nn involved/vbn are/ber astronomical/jj ./..")
from nltk.corpus.reader import TaggedCorpusReader
reader = TaggedCorpusReader('.', r'.*\.pos')
print("Palabras:")
print(reader.words())
print("Tags:")
print(reader.tagged_sents())
print("--------------------------------------\n")

print("04 Tags definidos por el usuario:")
from nltk.tokenize import SpaceTokenizer
reader = TaggedCorpusReader('.', r'.*\.pos', word_tokenizer=SpaceTokenizer())
print("Palabras:")
print(reader.words())

from nltk.tokenize import LineTokenizer
reader = TaggedCorpusReader('.', r'.*\.pos', sent_tokenizer=LineTokenizer())
print("Palabras:")
print(reader.sents())
reader = TaggedCorpusReader('.', r'.*\.pos', tagset='en-brown')
print("Palabras Tags Brown:")
print(reader.tagged_words(tagset='universal'))
print("--------------------------------------\n")