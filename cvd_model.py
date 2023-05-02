import sklearn
from sklearn.utils import shuffle
from sklearn import datasets
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style
from sklearn import svm
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing

# Load libraries
import numpy
from matplotlib import pyplot as plt
from pandas import read_csv
from pandas import set_option
from pandas.plotting import scatter_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier

# Data file import
cc_data = pd.read_csv("clean_dataset.csv")

# Attribute to be predicted
predict = "Approved"

# Dataset/Column to be Predicted, X is all attributes and y is the features
#x = np.array(credit_card_data.drop([predict], 1)) # Will return a new data frame that doesnt have approve in it
#y = np.array(credit_card[predict])
le = preprocessing.LabelEncoder()
gender = le.fit_transform(list(cc_data["Gender"])) # gender (1 = male; 0 = female)
age = le.fit_transform(list(cc_data["Age"])) # age in years
debt = le.fit_transform(list(cc_data["Debt"])) # debt amount
married = le.fit_transform(list(cc_data["Married"])) # marital status (1 = yes; 0 = no)
bankcustomer = le.fit_transform(list(cc_data["BankCustomer"])) # bank customer (1 = yes; 0 = no)
industry = le.fit_transform(list(cc_data["Industry"])) # type of industry
ethnicity = le.fit_transform(list(cc_data["Ethnicity"])) # ethnicity
yearsemployed = le.fit_transform(list(cc_data["YearsEmployed"])) # years employed
priordefault = le.fit_transform(list(cc_data["PriorDefault"])) # previous credit default (1 = yes; 0 = no)
employed = le.fit_transform(list(cc_data["Employed"])) # employed status (1 = yes; 0 = no)
creditscore = le.fit_transform(list(cc_data["CreditScore"])) # credit score
driverslicense = le.fit_transform(list(cc_data["DriversLicense"])) # driver's license (1 = yes; 0 = no)
citizen = le.fit_transform(list(cc_data["Citizen"])) # citizenship status
zipcode = le.fit_transform(list(cc_data["ZipCode"])) # zip code
income = le.fit_transform(list(cc_data["Income"])) # income
approved = le.fit_transform(list(cc_data["Approved"])) # credit card approval (1 = approved; 0 = not approved)


x = list(zip(gender,age,debt,married,bankcustomer,industry,ethnicity,yearsemployed,priordefault,employed,creditscore,driverslicense,citizen,zipcode,income))
y = list(approved)
# Test options and evaluation metric
num_folds = 5
seed = 7
scoring = 'accuracy'


# Model Test/Train
# Splitting what we are trying to predict into 4 different arrays -
# X train is a section of the x array(attributes) and vise versa for Y(features)
# The test data will test the accuracy of the model created
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.20, random_state=seed)
#splitting 20% of our data into test samples. If we train the model with higher data it already has seen that information and knows

# Check with  different Scikit-learn classification algorithms
models = []
models.append(('DT', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))
models.append(('GBM', GradientBoostingClassifier()))
models.append(('RF', RandomForestClassifier()))
# evaluate each model in turn
results = []
names = []

for name, model in models:
	kfold = KFold(n_splits=num_folds,shuffle=True,random_state=seed)
	cv_results = cross_val_score(model, x_train, y_train, cv=kfold, scoring='accuracy')
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	msg += '\n'
	print(msg)

# Compare Algorithms' Performance
fig = pyplot.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
pyplot.boxplot(results)
ax.set_xticklabels(names)
pyplot.show()


# Make predictions on validation/test dataset
dt = DecisionTreeClassifier()
nb = GaussianNB()
gb = GradientBoostingClassifier()
rf = RandomForestClassifier()

best_model = rf
best_model.fit(x_train, y_train)
y_pred = best_model.predict(x_test)
model_accuracy = accuracy_score(y_test, y_pred)
print("Best Model Accuracy Score on Test Set:", model_accuracy)

#Model Evaluation Metric 1
print(classification_report(y_test, y_pred))

#Model Evaluation Metric 2
#Confusion matrix
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.show()

#Model Evaluation Metric 3
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve

best_model = rf
best_model.fit(x_train, y_train)
rf_roc_auc = roc_auc_score(y_test,best_model.predict(x_test))
fpr,tpr,thresholds = roc_curve(y_test, best_model.predict_proba(x_test)[:,1])

plt.figure()
plt.plot(fpr,tpr,label = 'Random Forest(area = %0.2f)'% rf_roc_auc)
plt.plot([0,1],[0,1],'r--')
plt.xlim([0.0,1.0])
plt.ylim([0.0,1.05])
plt.xlabel('False positive rate')
plt.ylabel('True positive rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc='lower right')
plt.savefig('LOC_ROC')
plt.show()

#Check actual/ground truth vs predicted diagnosis
for x in range(len(y_pred)):
	print("Predicted: ", y_pred[x], "Actual: ", y_test[x], "Data: ", x_test[x],)
