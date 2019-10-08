#############################################################################
#Ejemplos extraidos del libro Natural Language Processing With Python.
#Referidos al capitulo 5.
#############################################################################

#Importar libreria NLTK para acceder a su funcionalidad.
import nltk

print("01 POS Tagger: Secuencia de Palbras.")
print("Definicion: Part Of Speech (POS) es una Secuencia de Palbras.")
text = nltk.word_tokenize("And now for something completely different")
print("Word Tokenize metodo")
print(nltk.pos_tag(text))
print("--------------------------------------\n")


