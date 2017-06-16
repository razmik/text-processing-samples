import numpy as np
import pandas as pd
import _pickle as pkl
import importlib

text_cleaner = importlib.import_module('text_cleaner')

# Read the test data
test = pd.read_csv("data/testData.tsv", header=0, delimiter="\t", quoting=3)

# Verify that there are 25,000 rows and 2 columns
print("Test data shape", test.shape)

# Create an empty list and append the clean reviews one by one
num_reviews = len(test["review"])
clean_test_reviews = []

print("Cleaning and parsing the test set movie reviews...\n")
for i in np.arange(0, num_reviews):
    if (i + 1) % 1000 == 0:
        print("Review %d of %d" % (i + 1, num_reviews))
    clean_review = text_cleaner.review_to_words(test["review"][i])
    clean_test_reviews.append(clean_review)

# load the word vector
with open('models/bag_of_words_vector.pkl', 'rb') as fid:
    vectorizer = pkl.load(fid)

# Get a bag of words for the test set, and convert to a numpy array
test_data_features = vectorizer.transform(clean_test_reviews)
test_data_features = test_data_features.toarray()

# load the model
with open('models/forest_classifier.pkl', 'rb') as fid:
    forest = pkl.load(fid)

# Use the random forest to make sentiment label predictions
result = forest.predict(test_data_features)

# Copy the results to a pandas dataframe with an "id" column and
# a "sentiment" column
output = pd.DataFrame(data={"id": test["id"], "sentiment": result})

# Use pandas to write the comma-separated output file
output.to_csv("results/Bag_of_Words_model.csv", index=False, quoting=3)

print("Results saved in results/Bag_of_Words_model.csv")
