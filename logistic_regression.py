import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = sns.load_dataset('iris')
# print(df.head())
# print(df['species'].unique())
# print(df.isnull().sum())
df = df[df['species']!='setosa'] # there were three different unique values so we need to do binary classification
# so we removed one which is setosa


# now we need to assign some value on the species
df['species'] = (df['species'].map({'versicolor':0, 'virginica':1}))


## Split dataset into independent and dependent features
x = df.iloc[:, :-1] # means leaving the last column and take all columns as last column is a dependent feature
y = df.iloc[:, -1]


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()

from sklearn.model_selection import GridSearchCV # for hyperparameter tuning 
parameters = {'penalty':['l1', 'l2', 'elasticnet'], 'C':[1, 2, 3, 4, 5, 6, 10, 20, 30, 40, 50], 
    'max_iter':[100, 200, 300]}

classifier_regressor = GridSearchCV(classifier, param_grid=parameters, scoring='accuracy', cv=5)

classifier_regressor.fit(x_train, y_train)
#classifier_regressor.fit(x_train, y_train) this does the below 4 things 
# 1.Computes w·x + b
# 2. Applies softmax
# 3. Minimizes log loss
# 4. Uses gradient descent



# print(classifier_regressor.best_params_)
# print(classifier_regressor.best_score_)


# prediction on data
y_pred = classifier_regressor.predict(x_test)

#predict probablities
y_prob = classifier_regressor.predict_proba(x_test)
print(y_prob[:5]) 


##calculating the accuracy score
from sklearn.metrics import accuracy_score, classification_report
score = accuracy_score(y_pred, y_test)
print(score)

classifier_report = classification_report(y_pred, y_test)
print(classifier_report) 

##EDA
sns.pairplot(df, hue='species')
# plt.show()

# print(df.corr()) # to see correlation

