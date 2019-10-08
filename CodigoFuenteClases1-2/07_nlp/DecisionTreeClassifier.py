#############################################################################
# Ejemplos extraidos del libro Python 3 Text Processing with NLTK 3 Cookbook.
# Referidos al capitulo 7.
#############################################################################

from nltk.corpus import movie_reviews
from nltk.classify.util import accuracy
from nltk.classify import DecisionTreeClassifier
from nltk.probability import FreqDist, MLEProbDist, entropy
from featx import label_feats_from_corpus, split_label_feats, bag_of_words  # featx.py debe estar en el mismo dir.

print(movie_reviews.categories())
# ['neg', 'pos']

lfeats = label_feats_from_corpus(movie_reviews)
print(lfeats.keys())
# dict_keys(['neg', 'pos'])

train_feats, test_feats = split_label_feats(lfeats, split=0.75)

print("Training Set: " + str(len(train_feats)))
# Training Set: 1500
print("Test Set: " + str(len(test_feats)))
# Test Set: 500

dt_classifier = DecisionTreeClassifier.train(train_feats, binary=True, entropy_cutoff=0.8, depth_cutoff=5, support_cutoff=30)
print("Accuracy: " + str(accuracy(dt_classifier, test_feats)))
# Accuracy: 0.688

fd = FreqDist({'pos': 30, 'neg': 10})
print(entropy(MLEProbDist(fd)))

fd['neg'] = 25
print(entropy(MLEProbDist(fd)))

fd['neg'] = 30
print(entropy(MLEProbDist(fd)))

fd['neg'] = 1
print(entropy(MLEProbDist(fd)))

