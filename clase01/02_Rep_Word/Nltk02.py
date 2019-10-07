#############################################################################
#Ejemplos extraidos del libro Python Text Processing with NLTK 2.0 Cookbook.
#Autor Jacob Perkins. Editorial Packt Publishing.
#Referidos al capitulo 2.
#############################################################################

#Importar libreria NLTK para acceder a su funcionalidad.
import nltk

print("01 Stemming: Raiz de las palabras.")
print("Definicion: es un método para reducir una palabra a su raíz o stem en ingles.")

print("PorterStemmer:")
stemmer = nltk.stem.PorterStemmer()
print("Stem  de Cooking: " + stemmer.stem('cooking'))
print("LancasterStemmer:")
stemmer = nltk.stem.LancasterStemmer()
print("Stem  de Cooking: " + stemmer.stem('cooking'))
print("RegexpStemmer:")
stemmer = nltk.stem.RegexpStemmer('ing')
print("Stem  de Cooking: " + stemmer.stem('cooking'))
print("SnowballStemmer:")
stemmer = nltk.stem.SnowballStemmer('spanish')
print("Stem  de Cooking: " + stemmer.stem('cocinando'))
print("--------------------------------------\n")

print("02 Lemmatization: Raiz de las palabras.")
print("Definicion: la lematizacion es similar al remplazo por sinonimos.")

print("Lemmatization:")
lemmatizer = nltk.stem.WordNetLemmatizer()
print("Lemma  de Cooking                         : " + lemmatizer.lemmatize('cooking'))
print("Lemma  de Cooking indicadono que es verbo : " + lemmatizer.lemmatize('cooking', pos='v'))
print("Lemma  de Cookbooks                       : " + lemmatizer.lemmatize('cookbooks'))
print("--------------------------------------\n")

print("03 Remplazo de palabras con expresiones regulares.")
import re
replacement_patterns = [
  (r'won\'t', 'will not'),
  (r'can\'t', 'cannot'),
  (r'i\'m', 'i am'),
  (r'ain\'t', 'is not'),
  (r'(\w+)\'ll', '\g<1> will'),
  (r'(\w+)n\'t', '\g<1> not'),
  (r'(\w+)\'ve', '\g<1> have'),
  (r'(\w+)\'s', '\g<1> is'),
  (r'(\w+)\'re', '\g<1> are'),
  (r'(\w+)\'d', '\g<1> would')
]
class RegexpReplacer(object):
    def __init__(self, patterns=replacement_patterns):
        self.patterns = [(re.compile(regex), repl) for (regex, repl) in
                         patterns]

    def replace(self, text):
        s = text
        for (pattern, repl) in self.patterns:
            (s, count) = re.subn(pattern, repl, s)
        return s

replacer = RegexpReplacer()
print("Resultado de remplazar 'can't is a contraction' : " + replacer.replace("can't is a contraction"))

print("Tokenizacion:")
print(nltk.tokenize.word_tokenize("can't is a contraction"))
print("Remplazar antes Tokenizacion:")
print(nltk.tokenize.word_tokenize(replacer.replace("can't is a contraction")))
print("--------------------------------------\n")

print("04 Remplazo de letras repetidas.")
class RepeatReplacer(object):
  def __init__(self):
    self.repeat_regexp = re.compile(r'(\w*)(\w)\2(\w*)')
    self.repl = r'\1\2\3'
  def replace(self, word):
    repl_word = self.repeat_regexp.sub(self.repl, word)
    if repl_word != word:
      return self.replace(repl_word)
    else:
      return repl_word

replacer = RepeatReplacer()
print("looooove : " + replacer.replace('looooove'))
print("oooooh   : " + replacer.replace('oooooh'))
print("goose    : " + replacer.replace('goose'))
print("--------------------------------------\n")

print("05 Remplazo de palabras.")
class WordReplacer(object):
  def __init__(self, word_map):
    self.word_map = word_map
  def replace(self, word):
    return self.word_map.get(word, word)

replacer = WordReplacer({'bday': 'birthday'})
print("bday: " + replacer.replace('bday'))
print("--------------------------------------\n")

print("06 Correccion de vocabulario.")
import enchant
from nltk.metrics import edit_distance
class SpellingReplacer(object):
  def __init__(self, dict_name='en', max_dist=2):
    self.spell_dict = enchant.Dict(dict_name)
    self.max_dist = max_dist
  def replace(self, word):
    if self.spell_dict.check(word):
      return word
    suggestions = self.spell_dict.suggest(word)
    if suggestions and edit_distance(word, suggestions[0]) <= self.max_dist:
      return suggestions[0]
    else:
      return word

replacer = SpellingReplacer()
print(replacer.replace('cookbok'))
print("--------------------------------------\n")

print("07 Distancia entre palabras:")
from nltk.metrics import edit_distance
print("'hola' y 'bola': " + str(edit_distance('hola', 'bola')))
print("--------------------------------------\n")

print("08 Crear diccionario propio:")
d = enchant.DictWithPWL('en_US', 'C:/NPL/Prg/03_Cus_Corpora/mywords.txt')
print("Existe nltk:" )
print(d.check('nltk'))
print("Existe nlk:")
print(d.check('nlk'))
print("Existe regular:")
print(d.check('regular'))
print("--------------------------------------\n")


print("09 Diccionario de sinonimos:")
import csv
class CsvWordReplacer(WordReplacer):
  def __init__(self, fname):
    word_map = {}
    for line in csv.reader(open(fname)):
      word, syn = line
      word_map[word] = syn
    super(CsvWordReplacer, self).__init__(word_map)

replacer = CsvWordReplacer('C:/NPL/Prg/03_Cus_Corpora/synonyms.csv')
print("Remplazar hola : " + replacer.replace('hola'))
print("Remplazar casa : " + replacer.replace('casa'))
print("--------------------------------------\n")