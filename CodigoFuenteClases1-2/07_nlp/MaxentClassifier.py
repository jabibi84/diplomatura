#############################################################################
# Ejemplos extraidos del libro Python 3 Text Processing with NLTK 3 Cookbook.
# Referidos al capitulo 7.
#############################################################################

from nltk.corpus import movie_reviews
from nltk.classify.util import accuracy
from nltk.classify import MaxentClassifier
from featx import label_feats_from_corpus, split_label_feats  # featx.py debe estar en el mismo dir.
import time

start_time = time.clock()
lfeats = label_feats_from_corpus(movie_reviews)
print("Tiempo Total de Lectura: " + ("{:.2f}".format(time.clock() - start_time)).replace('.', ',') + " seconds")


train_feats, test_feats = split_label_feats(lfeats, split=0.55)

start_time = time.clock()
me_classifier = MaxentClassifier.train(train_feats, trace=0, max_iter=1, min_lldelta=0.5)
print("Tiempo Total de Entrenamiento: " + ("{:.2f}".format(time.clock() - start_time)).replace('.', ',') + " seconds")

print("Accuracy: " + str(accuracy(me_classifier, test_feats)))

me_classifier = MaxentClassifier.train(train_feats, algorithm='gis', trace=0, max_iter=10, min_lldelta=0.5)
print("Accuracy: " + str(accuracy(me_classifier, test_feats)))
