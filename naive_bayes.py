from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

x = ["win money now", "win lottery", "meeting today", "project meeting"]
y = ["spam", "spam", "not", "not"]

vector = CountVectorizer()
x_vec = vector.fit_transform(x)# for learing we use fit and to create matrix we use transform

model = MultinomialNB()
model.fit(x_vec, y)

test = ["win today"]
test_vec = vector.transform(test)#here no use of fit as it cause data leakage

print("Probablity", model.predict(test_vec))
print("Probablity", model.predict_proba(test_vec))