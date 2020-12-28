import nltk
import sklearn.datasets
import sklearn.metrics
import sklearn.model_selection

from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize, sent_tokenize
from sklearn.svm import SVC


def load_data(dir_name):
    return sklearn.datasets.load_files('data/%s' % dir_name, encoding='utf-8')


def load_train_data():
    return load_data('training')


def load_test_data():
    return load_data('test')


def extract_features():
    pass


def classify(y_true, y_pred):
    recall = sklearn.metrics.recall_score(y_true, y_pred, average='macro')
    print("Recall: %f" % recall)

    precision = sklearn.metrics.precision_score(y_true, y_pred, average='macro')
    print("Precision: %f" % precision)

    f1_score = sklearn.metrics.f1_score(y_true, y_pred, average='macro')
    print("F1-score: %f" % f1_score)
    
    return recall, precision, f1_score


def evaluate():
    pass


def run_classifier():
    pass
