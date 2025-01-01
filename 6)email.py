

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

df = pd.read_csv('emails.csv')

df.info()

df.head()

df.shape

df.size

df.isna().sum()

df.drop(["Email No."], axis = 1, inplace = True)

x = df.drop(["Prediction"],axis =1)
y = df["Prediction"]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=1)

# KNN Classification
from sklearn import metrics
accuracy_values = []

for i in range(1,11):
    model = KNeighborsClassifier(n_neighbors = i)
    model.fit(x_train,y_train)
    y_pred = model.predict(x_test)
    accuracy = metrics.accuracy_score(y_test,y_pred)
    accuracy_values.append(accuracy)

# Finding the Optimal K based on Accuracy Score

optimal_k = -1
optimal_accuracy = -1

for i in list(zip(range(1,11),accuracy_values)):
    if i[1] > optimal_accuracy :
        optimal_k = i[0]
        optimal_accuracy = i[1]

print("Optimal K : " + str(optimal_k))
knn = KNeighborsClassifier(n_neighbors = optimal_k)

knn.fit(x_train,y_train)
y_pred = knn.predict(x_test)

print(metrics.classification_report(y_test,y_pred))

confusion_matrix_knn = metrics.confusion_matrix(y_test,y_pred)
cm_display_knn = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix_knn, display_labels = ["False","True"])

cm_display_knn.plot()

# SVM
svm_model = SVC()

svm_model.fit(x_train,y_train)
y_pred = svm_model.predict(x_test)

print(metrics.classification_report(y_test,y_pred))

confusion_matrix_svm = metrics.confusion_matrix(y_test,y_pred)
display_cm_svm = metrics.ConfusionMatrixDisplay(confusion_matrix=confusion_matrix_svm, display_labels=["False","True"])
display_cm_svm.plot()