
import pandas as pd

dataframe = pd.read_csv("diabetes.csv")

df = dataframe

df.head()

df.info()

df.describe()

df.isna().sum()

x = df.drop("Outcome",axis=1)
y = df["Outcome"]
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=1)

from sklearn.neighbors import KNeighborsClassifier

accuracy_values = []
from sklearn import metrics
for i in range(1,20):
    model = KNeighborsClassifier(n_neighbors=i)
    model.fit(x_train,y_train)
    y_pred = model.predict(x_test)
    accuracy = metrics.accuracy_score(y_test,y_pred)
    accuracy_values.append(accuracy)

optimal_k = -1
optimal_accuracy = -1

for i in list(zip(range(1,20),accuracy_values)):
    if i[1]>optimal_accuracy:
        optimal_accuracy = i[1]
        optimal_k = i[0]

knn = KNeighborsClassifier(n_neighbors = optimal_k)

knn.fit(x_train,y_train)

y_pred = knn.predict(x_test)

confusion_matrix = metrics.confusion_matrix(y_test,y_pred)

cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix=confusion_matrix, display_labels = ["False","True"])
cm_display.plot()

print(metrics.classification_report(y_test,y_pred))