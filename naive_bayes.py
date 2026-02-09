from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pandas as pd
import numpy as np

df = pd.read_csv("../spam.csv",  encoding='latin1')
df = df[['v1', 'v2']]

df.columns = ['label', 'message']
df['label'] = df['label'].map({"ham":0, "spam":1})

x = df['message']
y = df['label']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

vector = CountVectorizer()
x_train_vec = vector.fit_transform(x_train)# for learing we use fit and to create matrix we use transform
x_test_vec = vector.transform(x_test)

model = MultinomialNB()
model.fit(x_train_vec, y_train)

# test_vec = vector.transform(x_test)#here no use of fit as it cause data leakage
y_pred = model.predict(x_test_vec)

print("Probablity:", model.predict_proba(x_test_vec))
#these all compares label with label not features with label
print("Accuracy", accuracy_score(y_test, y_pred))
print("\nConfusion_matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))