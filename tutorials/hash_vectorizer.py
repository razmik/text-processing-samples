from sklearn.feature_extraction.text import HashingVectorizer

# list of text documents
text = ["The quick brown fox jumped over the lazy dog."]
text_2 = ["The quick brown fox jumped over the lazy dog is a very good dog indeed."]

# create the transform
vectorizer = HashingVectorizer(n_features=20)

# encode document
vector = vectorizer.transform(text)
vector_2 = vectorizer.transform(text_2)

# summarize encoded vector
# print(vector.shape)
print(vector.toarray())
print(vector_2.toarray())
