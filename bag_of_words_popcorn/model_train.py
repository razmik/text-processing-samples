import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
import _pickle as pkl
import importlib

text_cleaner = importlib.import_module('text_cleaner')

# Data retrival
train = pd.read_csv("data/labeledTrainData.tsv", header=0, delimiter="\t", quoting=3)
num_reviews = len(train)

print("Cleaning and parsing the training set movie reviews...\n")
clean_train_reviews = []
for i in np.arange(0, num_reviews):
    # If the index is evenly divisible by 1000, print a message
    if (i + 1) % 1000 == 0:
        print("Review %d of %d" % (i + 1, num_reviews))
    clean_train_reviews.append(text_cleaner.review_to_words(train["review"][i]))

print("Creating the bag of words...\n")
# Initialize the "CountVectorizer" object, which is scikit-learn's
# bag of words tool.
vectorizer = CountVectorizer(analyzer="word", tokenizer=None, preprocessor=None, stop_words=None, max_features=5000)

# fit_transform() does two functions: First, it fits the model
# and learns the vocabulary; second, it transforms our training data
# into feature vectors. The input to fit_transform should be a list of
# strings.
train_data_features = vectorizer.fit_transform(clean_train_reviews)

# Numpy arrays are easy to work with, so convert the result to an
# array
train_data_features = train_data_features.toarray()

print("Training the random forest...\n")

# Initialize a Random Forest classifier with 100 trees
forest = RandomForestClassifier(n_estimators=100)

# Fit the forest to the training set, using the bag of words as
# features and the sentiment labels as the response variable
# This may take a few minutes to run
forest = forest.fit(train_data_features, train["sentiment"])

# save the classifier
with open('models/forest_classifier.pkl', 'wb') as file:
    pkl.dump(forest, file)


with open('models/bag_of_words_vector.pkl', 'wb') as file:
    pkl.dump(vectorizer, file)

print("Model saved to disk.")
