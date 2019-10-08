#############################################################################
# Ejemplos extraidos del libro Python 3 Text Processing with NLTK 3 Cookbook.
# Referidos al capitulo 7.
#############################################################################

from featx import label_feats_from_corpus, split_label_feats  # featx.py debe estar en el mismo dir.
from classification import precision_recall                   # classification.py debe estar en el mismo dir.
from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier
from nltk.classify import MaxentClassifier
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB

lfeats = label_feats_from_corpus(movie_reviews)
train_feats, test_feats = split_label_feats(lfeats, split=0.75)

print("######################################################################")
nb_classifier = NaiveBayesClassifier.train(train_feats)
nb_precisions, nb_recalls = precision_recall(nb_classifier, test_feats)
print("Precisions Naive Bayes Pos: " + str(nb_precisions['pos']))
# Precisions Naive Bayes Pos: 0.651595744680851
print("Precisions Naive Bayes Neg: " + str(nb_precisions['neg']))
# Precisions Naive Bayes Neg: 0.9596774193548387
print("Recalls Naive Bayes Pos: " + str(nb_recalls['pos']))
# Recalls Naive Bayes Neg: 0.476Recalls Naive Bayes Pos: 0.98
print("Recalls Naive Bayes Neg: " + str(nb_recalls['neg']))
# Recalls Naive Bayes Neg: 0.476
print("######################################################################")
train_feats, test_feats = split_label_feats(lfeats, split=0.55)
me_classifier = MaxentClassifier.train(train_feats, trace=0, max_iter=1, min_lldelta=0.5)
me_precisions, me_recalls = precision_recall(me_classifier, test_feats)
print("Precisions Max Entropy Pos: " + str(me_precisions['pos']))
# Precisions Max Entropy Pos: 0.7580174927113703
print("Precisions Max Entropy Neg: " + str(me_precisions['neg']))
# Precisions Max Entropy Neg: 0.6588868940754039
print("Recalls Max Entropy Pos: " + str(me_recalls['pos']))
# Recalls Max Entropy Pos: 0.5777777777777777
print("Recalls Max Entropy Neg: " + str(me_recalls['neg']))
# Recalls Max Entropy Neg: 0.8155555555555556
print("######################################################################")
sk_classifier = SklearnClassifier(MultinomialNB())
sk_classifier.train(train_feats)
sk_precisions, sk_recalls = precision_recall(sk_classifier, test_feats)
print("Precisions MultinomialNB Pos: " + str(sk_precisions['pos']))
# Precisions MultinomialNB Pos: 0.84375
print("Precisions MultinomialNB Neg: " + str(sk_precisions['neg']))
# Precisions MultinomialNB Neg: 0.7954545454545454
print("Recalls MultinomialNB Pos: " + str(sk_recalls['pos']))
# Recalls MultinomialNB Pos: 0.78
print("Recalls MultinomialNB Neg: " + str(sk_recalls['neg']))
# Recalls MultinomialNB Neg: 0.8555555555555555
print("######################################################################")
