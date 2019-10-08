#############################################################################
# Ejemplos extraidos del libro Python 3 Text Processing with NLTK 3 Cookbook.
# Referidos al capitulo 7.
#############################################################################

from featx import label_feats_from_corpus, split_label_feats, high_information_words, bag_of_words_in_set
from classification import precision_recall, MaxVoteClassifier    # classification.py debe estar en el mismo dir.
from nltk.corpus import movie_reviews
from nltk.classify.util import accuracy
from nltk.classify import NaiveBayesClassifier
from nltk.classify import MaxentClassifier
from nltk.classify import DecisionTreeClassifier
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.svm import LinearSVC

labels = movie_reviews.categories()
labeled_words = [(l, movie_reviews.words(categories=[l])) for l in labels]
high_info_words = set(high_information_words(labeled_words))
feat_det = lambda words: bag_of_words_in_set(words, high_info_words)
lfeats = label_feats_from_corpus(movie_reviews, feature_detector=feat_det)
train_feats, test_feats = split_label_feats(lfeats)

print("######################################################################")
nb_classifier = NaiveBayesClassifier.train(train_feats)
print("Accuracy Naive Bayes: " + str(accuracy(nb_classifier, test_feats)))
# Accuracy: 0.91
nb_precisions, nb_recalls = precision_recall(nb_classifier, test_feats)
print("Precisions Naive Bayes Pos: " + str(nb_precisions['pos']))
# Precisions Pos: 0.8988326848249028
print("Precisions Naive Bayes Neg: " + str(nb_precisions['neg']))
# Precisions Neg: 0.9218106995884774
print("Recalls Naive Bayes Pos: " + str(nb_recalls['pos']))
# Recalls Pos: 0.924
print("Recalls Naive Bayes Neg: " + str(nb_recalls['neg']))
# Recalls Neg: 0.896
print("######################################################################")
me_classifier = MaxentClassifier.train(train_feats, algorithm='gis', trace=0, max_iter=10, min_lldelta=0.5)
print("Accuracy Max Entropy: " + str(accuracy(me_classifier, test_feats)))
# Accuracy Max Entropy: 0.912
me_precisions, me_recalls = precision_recall(me_classifier, test_feats)
print("Precisions Max Entropy Pos: " + str(me_precisions['pos']))
# Precisions Max Entropy Pos: 0.8992248062015504
print("Precisions Max Entropy Neg: " + str(me_precisions['neg']))
# Precisions Max Entropy Neg: 0.9256198347107438
print("Recalls Max Entropy Pos: " + str(me_recalls['pos']))
# Recalls Max Entropy Pos: 0.928
print("Recalls Max Entropy Neg: " + str(me_recalls['neg']))
# Recalls Max Entropy Neg: 0.896
print("######################################################################")
dt_classifier = DecisionTreeClassifier.train(train_feats, binary=True, depth_cutoff=20, support_cutoff=20, entropy_cutoff=0.01)
print("Accuracy Decision Tree: " + str(accuracy(dt_classifier, test_feats)))
# Accuracy Decision Tree: 0.68600000000000005
dt_precisions, dt_recalls = precision_recall(dt_classifier, test_feats)
print("Precisions Decision Tree Pos: " + str(dt_precisions['pos']))
# Precisions Decision Tree Pos: 0.6741573033707865
print("Precisions Decision Tree Neg: " + str(dt_precisions['neg']))
# Precisions Decision Tree Neg: 0.69957081545064381
print("Recalls Decision Tree Pos: " + str(dt_recalls['pos']))
# Recalls Decision Tree Pos: 0.71999999999999997
print("Recalls Decision Tree Neg: " + str(dt_recalls['neg']))
# Recalls Decision Tree Neg: 0.65200000000000002
print("######################################################################")
sk_classifier = SklearnClassifier(LinearSVC()).train(train_feats)
print("Accuracy Sklearn Linear SVC: " + str(accuracy(sk_classifier, test_feats)))
# Accuracy Sklearn Linear SVC: 0.86
sk_precisions, sk_recalls = precision_recall(sk_classifier, test_feats)
print("Precisions Sklearn Linear SVC Pos: " + str(sk_precisions['pos']))
# Precisions Sklearn Linear SVC Pos: 0.871900826446281
print("Precisions Sklearn Linear SVC Neg: " + str(sk_precisions['neg']))
# Precisions Sklearn Linear SVC Neg: 0.8488372093023255
print("Recalls Sklearn Linear SVC Pos: " + str(sk_recalls['pos']))
# Recalls Sklearn Linear SVC Pos: 0.844
print("Recalls Sklearn Linear SVC Neg: " + str(sk_recalls['neg']))
# Recalls Sklearn Linear SVC Neg: 0.876
print("######################################################################")
mv_classifier = MaxVoteClassifier(nb_classifier, dt_classifier, me_classifier, sk_classifier)
print("Accuracy Max Vote: " + str(accuracy(mv_classifier, test_feats)))
# Accuracy Max Vote: 0.894
mv_precisions, mv_recalls = precision_recall(mv_classifier, test_feats)
print("Precisions Max Vote Pos: " + str(mv_precisions['pos']))
# Precisions Max Vote Pos: 0.9156118143459916
print("Precisions Max Vote Neg: " + str(mv_precisions['neg']))
# Precisions Max Vote Neg: 0.8745247148288974
print("Recalls Max Vote Pos: " + str(mv_recalls['pos']))
# Precisions Max Vote Pos: 0.868
print("Recalls Max Vote Neg: " + str(mv_recalls['neg']))
# Precisions Max Vote Neg: 0.92
print("######################################################################")

######################################################################
#Accuracy Naive Bayes: 0.91
#Precisions Naive Bayes Pos: 0.8988326848249028
#Precisions Naive Bayes Neg: 0.9218106995884774
#Recalls Naive Bayes Pos: 0.924
#Recalls Naive Bayes Neg: 0.896
######################################################################
#Accuracy Max Entropy: 0.912
#Precisions Max Entropy Pos: 0.8992248062015504
#Precisions Max Entropy Neg: 0.9256198347107438
#Recalls Max Entropy Pos: 0.928
#Recalls Max Entropy Neg: 0.896
######################################################################
#Accuracy Decision Tree: 0.688
#Precisions Decision Tree Pos: 0.6715328467153284
#Precisions Decision Tree Neg: 0.7079646017699115
#Recalls Decision Tree Pos: 0.736
#Recalls Decision Tree Neg: 0.64
######################################################################
#Accuracy Sklearn Linear SVC: 0.86
#Precisions Sklearn Linear SVC Pos: 0.871900826446281
#Precisions Sklearn Linear SVC Neg: 0.8488372093023255
#Recalls Sklearn Linear SVC Pos: 0.844
#Recalls Sklearn Linear SVC Neg: 0.876
######################################################################
#Accuracy Max Vote: 0.912
#Precisions Max Vote Pos: 0.905511811023622
#Precisions Max Vote Neg: 0.9186991869918699
#Recalls Max Vote Pos: 0.92
#Recalls Max Vote Neg: 0.904
######################################################################
