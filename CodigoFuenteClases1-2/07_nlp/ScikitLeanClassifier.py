#############################################################################
# Ejemplos extraidos del libro Python 3 Text Processing with NLTK 3 Cookbook.
# Referidos al capitulo 7.
#############################################################################

from nltk.corpus import movie_reviews
from featx import label_feats_from_corpus, split_label_feats  # featx.py debe estar en el mismo dir.
from nltk.classify.scikitlearn import SklearnClassifier
from nltk.classify.util import accuracy
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn.svm import NuSVC

lfeats = label_feats_from_corpus(movie_reviews)
train_feats, test_feats = split_label_feats(lfeats, split=0.75)

print("Training Set: " + str(len(train_feats)))
# Training Set: 1500
print("Test Set: " + str(len(test_feats)))
# Test Set: 500

sk_classifier = SklearnClassifier(MultinomialNB())
sk_classifier.train(train_feats)
print("Accuracy MultinomialNB: " + str(accuracy(sk_classifier, test_feats)))
# Accuracy MultinomialNB: 0.83

sk_classifier = SklearnClassifier(BernoulliNB())
sk_classifier.train(train_feats)
print("Accuracy BernoulliNB: " + str(accuracy(sk_classifier, test_feats)))
# Accuracy BernoulliNB: 0.812

sk_classifier = SklearnClassifier(LogisticRegression()).train(train_feats)
print("Accuracy LogisticRegression: " + str(accuracy(sk_classifier, test_feats)))
# Accuracy LogisticRegression: 0.892

sk_classifier = SklearnClassifier(SVC()).train(train_feats)
print("Accuracy SVC: " + str(accuracy(sk_classifier, test_feats)))
# Accuracy SVC: 0.69

sk_classifier = SklearnClassifier(LinearSVC()).train(train_feats)
print("Accuracy LinearSVC: " + str(accuracy(sk_classifier, test_feats)))
# Accuracy LinearSVC: 0.864

sk_classifier = SklearnClassifier(NuSVC()).train(train_feats)
print("Accuracy NuSVC: " + str(accuracy(sk_classifier, test_feats)))
# Accuracy NuSVC: 0.882

#Training Set: 1500
#Test Set: 500
#Accuracy MultinomialNB: 0.83
#Accuracy BernoulliNB: 0.812
#Accuracy LogisticRegression: 0.892
#Accuracy SVC: 0.69
#Accuracy LinearSVC: 0.864
#Accuracy NuSVC: 0.882




