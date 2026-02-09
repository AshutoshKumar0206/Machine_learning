import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score 
from sklearn.model_selection import cross_val_score
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = load_diabetes()
dataset = pd.DataFrame(df.data)
# print(dataset)
dataset.columns = df.feature_names#for column names
# print(dataset.tail())

##independent and dependent features
x = dataset #this is the independent feature or the input
y = df.target #This is the dependent feature or the output
# print(y)

##Now will do a train test split to split dataset into training and testing data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=42)#test size is 30%
# print(y_test)

##Now in this we will implement linear regression
#first standardizing the dataset
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)#fit_transform is used to learn from the data and get mean and standard deviation values 
x_test = scaler.transform(x_test)#transform is used to just fetch answers not learn so it uses same mean and standard deviation it got while learning

# ##Now we do cross validation
# regression = LinearRegression()
# regression.fit(x, y)
# mse=cross_val_score(regression, x_train, y_train, scoring='neg_mean_squared_error', cv=10)#this does K fold cross validation on training data

# # print(mse)

# mean = np.mean(mse)

# ##prediction
# reg_pred = regression.predict(x_test)
# # print(reg_pred)

# sns.displot(reg_pred - y_test, kind="kde")
# # plt.show() 

# score = r2_score(reg_pred, y_test)
# print(score)

from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.model_selection import GridSearchCV

# ridge_regressor = Ridge()#ridge regressor object created
# print(ridge_regressor)
# parameters = {'alpha':[1,2,5,10,20,30,40,50,60,70,80,90]}
# ridgecv = GridSearchCV(ridge_regressor, parameters, scoring='neg_mean_squared_error', cv=5)#Hyperparameter tuning
# ridgecv.fit(x_train, y_train)

# print(ridgecv.best_params_)
# print(ridgecv.best_score_)

# ridge_pred = ridgecv.predict(x_test)
# print(ridge_pred)

# sns.displot(ridge_pred - y_test, kind="kde")
# plt.show() 

# score = r2_score(ridge_pred, y_test)
# print(score)


##Lasso regression

lasso_regressor = Lasso()#ridge regressor object created
# print(lasso_regressor)
parameters = {'alpha':[1,2,5,10,20,30,40,50,60,70,80,90]}
lassocv = GridSearchCV(lasso_regressor, parameters, scoring='neg_mean_squared_error', cv=5)#Hyperparameter tuning
lassocv.fit(x_train, y_train)

# print(lassocv.best_params_)
# print(lassocv.best_score_)

lasso_pred = lassocv.predict(x_test)
# print(lasso_pred)

# sns.displot(lasso_pred - y_test, kind="kde")
# plt.show() 

score = r2_score(lasso_pred, y_test)
print(score)