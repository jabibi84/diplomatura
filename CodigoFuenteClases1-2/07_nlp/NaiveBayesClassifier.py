#############################################################################
# Ejemplos extraidos del libro Python 3 Text Processing with NLTK 3 Cookbook.
# Referidos al capitulo 7.
#############################################################################

from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy
from nltk.probability import DictionaryProbDist
from nltk.probability import LaplaceProbDist
from featx import label_feats_from_corpus, split_label_feats, bag_of_words  # featx.py debe estar en el mismo dir.
import time

print(movie_reviews.categories())
# ['neg', 'pos']

lfeats = label_feats_from_corpus(movie_reviews)

print(lfeats.keys())
# dict_keys(['neg', 'pos'])

train_feats, test_feats = split_label_feats(lfeats, split=0.75)
print(len(train_feats))

print(len(test_feats))

nb_classifier = NaiveBayesClassifier.train(train_feats)
print(nb_classifier.labels())

negfeat = bag_of_words(['the', 'plot', 'was', 'ludicrous'])
print(nb_classifier.classify(negfeat))

posfeat = bag_of_words(['kate', 'winslet', 'is', 'accessible'])
print(nb_classifier.classify(posfeat))

print(accuracy(nb_classifier, test_feats))

probs = nb_classifier.prob_classify(test_feats[0][0])
print(probs.samples())

print(probs.max())

print(probs.prob('pos'))

print(probs.prob('neg'))

print(nb_classifier.most_informative_features(n=5))
print("############################################################################")
print(nb_classifier.show_most_informative_features(n=5))
print("############################################################################")

nb_classifier = NaiveBayesClassifier.train(train_feats, estimator=LaplaceProbDist)

print("Accuracy: " + str(accuracy(nb_classifier, test_feats)))
# Accuracy: 0.76

label_probdist = DictionaryProbDist({'pos': 0.5, 'neg': 0.5})
true_probdist = DictionaryProbDist({True: 1})
feature_probdist = {('pos', 'yes'): true_probdist, ('neg', 'no'): true_probdist}
classifier = NaiveBayesClassifier(label_probdist, feature_probdist)

print(classifier.classify({'yes': True}))
print(classifier.classify({'no': True}))
