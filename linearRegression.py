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

##Now we do cross validation
regression = LinearRegression()
regression.fit(x, y)
mse=cross_val_score(regression, x_train, y_train, scoring='neg_mean_squared_error', cv=10)#this does K fold cross validation on training data

# print(mse)

mean = np.mean(mse)

##prediction
reg_pred = regression.predict(x_test)
# print(reg_pred)

sns.displot(reg_pred - y_test, kind="kde")
# plt.show() 

score = r2_score(reg_pred, y_test)
print(score)