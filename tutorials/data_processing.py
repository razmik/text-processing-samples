"""
https://machinelearningmastery.com/prepare-text-data-machine-learning-scikit-learn/
"""


from sklearn.feature_extraction.text import CountVectorizer

"""
Building the vocabulary
"""

# list of text documents
full_dataset = ["The quick brown fox jumped over the lazy dog."]

# create the transform
vectorizer = CountVectorizer()

# tokenize and build vocab
vectorizer.fit(full_dataset)

# summarize
print(vectorizer.vocabulary_)

"""
Processing individual documents
"""
ex_test = ['The brown quick came']

# encode document
vector = vectorizer.transform(ex_test)

# summarize encoded vector
print(vector.shape)
print(type(vector))
print(vector.toarray())
