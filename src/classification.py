import nltk
import sklearn.datasets
import sklearn.metrics
import sklearn.model_selection

from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize, sent_tokenize
from sklearn.svm import SVC
from pathlib import Path


def load_data(dir_name):
    path = str(Path().resolve().parent)
    return sklearn.datasets.load_files(f'{path}/data/{dir_name}', decode_error='replace', encoding='utf-8')


def load_train_data():
    return load_data('training')


def load_test_data():
    return load_data('test')


def extract_features(text):
    bag_of_words = [x for x in wordpunct_tokenize(text)]
    features = []
    total_count = len(bag_of_words) if bag_of_words is not [] else 1

    # Feature 1: Total count of lyrics
    features.append(total_count)
    
    # Feature 2: Average word length
    features.append(sum([len(x.lower()) for x in bag_of_words]) / total_count)

    # Feature 3: Number of parentheses, these indicate addlips
    features.append(len([x for x in bag_of_words if "(" in x]))

    # Feature 4-26: Count most common words
    common_words = ['love', 'you', 'feel', 'never', 'night',
    'thing', 'gonna', 'away', 'let', 'me', 'tell', 'down', 'we'
    'over', 'yeah', 'i', 'life', 'need', 'heart', 'here', 'hate',
    'my']

    for word in common_words: 
        features.append(len([x for x in bag_of_words if x.lower() == word]))

    # Pos-tags list (36 tags)
    pos_tags = ['CC', 'CD', 'DT', 'EX', 'FW', 'IN', 'JJ', 'JJR',
    'JJS', 'LS', 'MD', 'NN', 'NNS', 'NNP', 'NNPS', 'PDT', 'POS',
    'PRP', 'PRP$', 'RB', 'RBR', 'RBS', 'RP', 'SYM', 'TO', 'UH',
    'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP', 'WP$',
    'WRB']
    
    # Feature 27-63 (36 pos tags)
    tagged = nltk.pos_tag(bag_of_words)
    for tag in pos_tags:
        value_list = []
        for (value, key) in tagged:
            if key == tag:
                value_list.append(value)
        features.append(len(value_list))
    
    return features


def classify(train_features, train_labels, test_features):
    clf = SVC(kernel='linear')
    clf.fit(train_features, train_labels)

    return clf.predict(test_features)


def evaluate(y_true, y_pred):
    recall = sklearn.metrics.recall_score(y_true, y_pred, average='macro')
    precision = sklearn.metrics.precision_score(y_true, y_pred, average='macro')
    f1_score = sklearn.metrics.f1_score(y_true, y_pred, average='macro')
    ap = sklearn.metrics.average_precision_score(y_true, y_pred, average='macro')
    
    return recall, precision, f1_score, ap


def train_classifier():
    train_data = load_train_data()
    features = list(map(extract_features, train_data.data))
    scores = []
    
    # Cross validation for training and validation
    skf = sklearn.model_selection.StratifiedKFold(n_splits=10)
    for idx, (train_indexes, validation_indexes) in enumerate(skf.split(train_data.filenames, train_data.target)):
        print("Fold %d" % (idx + 1))

        # Collect the data for this train/validation split
        train_features = [features[x] for x in train_indexes]
        train_labels = [train_data.target[x] for x in train_indexes]
        validation_features = [features[x] for x in validation_indexes]
        validation_labels = [train_data.target[x] for x in validation_indexes]

        # Classify and add the scores to the list
        y_pred = classify(train_features, train_labels, validation_features)
        scores.append(evaluate(validation_labels, y_pred))

    return features, scores, train_data.target


def test_classifier(features, target):
    test_data = load_test_data()
    test_features = list(map(extract_features, test_data.data))
    
    y_pred = classify(features, target, test_features)
    scores = evaluate(test_data.target, y_pred)
    return scores


def run_classifier():
    features, avg_scores, target = train_classifier()
    test_scores = test_classifier(features, target)

    # Print the averaged score
    labels = ['recall', 'precision', 'f1_score', 'average precision']
    print(avg_scores)

    for score in test_scores:
        print(score)


run_classifier()
    
