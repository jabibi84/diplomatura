#############################################################################
# Ejemplos extraidos del libro Python 3 Text Processing with NLTK 3 Cookbook.
# Referidos al capitulo 7.
#############################################################################

from featx import reuters_high_info_words, reuters_train_test_feats, bag_of_words_in_set
from classification import train_binary_classifiers,  MultiBinaryClassifier,  multi_metrics
from nltk.classify.scikitlearn import SklearnClassifier
from nltk.corpus import reuters
from sklearn.linear_model import LogisticRegression


print("######################################################################")
print("Total Routers Cats: " + str(len(reuters.categories())))


rwords = reuters_high_info_words()
featdet = lambda words: bag_of_words_in_set(words, rwords)
multi_train_feats, multi_test_feats = reuters_train_test_feats(featdet)
trainf = lambda train_feats: SklearnClassifier(LogisticRegression()).train(train_feats)
labelset = set(reuters.categories())
classifiers = train_binary_classifiers(trainf, multi_train_feats,labelset)
print("Total Routers Cats Bin: " + str(len(classifiers)))
multi_classifier = MultiBinaryClassifier(*classifiers.items())
multi_precisions, multi_recalls, avg_md = multi_metrics(multi_classifier, multi_test_feats)
print("Total Multi Metrics: " + str(avg_md))
# Total Routers Cats: 0.23310715863026216
print("Total multi_precisions soybean: " + str(multi_precisions['soybean']))
# Total Routers Cats: 0.7857142857142857
print("Total multi_recalls soybean: " + str(multi_recalls['soybean']))
# Total Routers Cats: 0.3333333333333333
print("Total Routers Cats Len soybean: " + str(len(reuters.fileids(categories=['soybean']))))
# Total Routers Cats: 111
print("Total multi_precisions sunseed: " + str(multi_precisions['sunseed']))
# Total Routers Cats: 1.0
print("Total multi_recalls sunseed: " + str(multi_recalls['sunseed']))
# Total Routers Cats: 2.0
print("Total Routers Cats crude: " + str(len(reuters.fileids(categories=['crude']))))
print("######################################################################")
