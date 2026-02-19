from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
iris = load_iris()
x = iris.data
y = iris.target
print(x)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

dt = DecisionTreeClassifier()
dt.fit(x_train, y_train)

y_pred = dt.predict(x_test)

from sklearn.metrics import accuracy_score
print("Accuracy Score:", accuracy_score(y_test, y_pred))

from sklearn.tree import plot_tree
from matplotlib import rcParams
import matplotlib.pyplot as plt

rcParams['figure.figsize'] = 8,5
plot_tree(dt)
# plt.show()
