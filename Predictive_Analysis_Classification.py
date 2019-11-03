import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.metrics import roc_curve
from sklearn.metrics import auc

# function that can initialize the new model
def initializeData():
    models = []
    models.append(('NB', GaussianNB()))
    models.append(('SVM', SVC(gamma='auto')))
    models.append(('DC', DecisionTreeClassifier()))
    models.append(('kNN',KNeighborsClassifier(n_neighbors=10)))
    models.append(('RF',RandomForestClassifier(n_estimators=100)))
    return models

# function that can get different normalized training data under different norms
def getNorms(Data):
    # options = ['l1', 'l2', 'max']
    options = ['l1']
    X_normalized=[]
    for opt in options:
        X_normalized.append(preprocessing.normalize(Data, norm=opt))
    return X_normalized

# function that can calculate accuracy of different classifiers
def calculateAccuracy(models,X_normalized,index,options):
    # split data into training part and testing part
    X_train, X_validate, Y_train, Y_validate = train_test_split(X_normalized, Y, test_size=test_size, random_state=seed)
    # cross-validation
    for name, model in models:
        kfold = KFold(n_splits=num_folds, random_state=seed, shuffle=False)
        cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
        msg = "Cross-validation result with norm %s: %s: %f" % (
        options[index], name, cv_results.mean())
        print(msg)
    # train and predict
    for name, model in models:
        model.fit(X_train, Y_train)
        predictions = model.predict(X_validate)
        print("Accuracy on test dataset with norm %s: %s: %f" % (
        options[index], name, accuracy_score(Y_validate, predictions)))
        # confusion matrix
        print("confusion matrix: ",confusion_matrix(Y_validate, predictions))
        # ROC curve
        fpr, tpr, thresholds=roc_curve(Y_validate,predictions,pos_label=1,drop_intermediate=True)
        print("ROC curve fpr: ",fpr)
        print("ROC curve tpr: ", tpr)
        print("ROC curve thresholds: ", thresholds)
        # AUC value
        AUC = auc(fpr, tpr)
        print("AUC: ",AUC)

# function that can make non-numeric categorical data numeric
def categorical(myData, CategoricalNames):
    for attribute in CategoricalNames:
        myData[attribute] = pd.Categorical(myData[attribute])
        myData[attribute] = myData[attribute].cat.codes

if __name__ == '__main__':
    # initialize Data
    models=initializeData()
    # read data
    data=pd.read_csv('PJ Phase1\\5.player_career_stats_cleaned.csv')
    # add final_score column
    data['final_score']=data['PTS']>10
    # make non-numeric categorical data numeric
    CategoricalNames = ['Name', 'Season', 'Lg', 'G', 'final_score']
    categorical(data, CategoricalNames)
    # divide X,Y
    valueArray = data.values
    X = valueArray[:, 0:27]
    Y = valueArray[:, 28]
    # set parameters
    test_size = 0.20
    seed = 1
    index = 0
    options = ['l1']
    num_folds=5
    scoring = 'accuracy'
    # normalize data with different norms
    X_normalized_list = getNorms(X)
    # calculate the classification accuracy of three classifiers under different norms
    for X_normalized in X_normalized_list:
        calculateAccuracy(models, X_normalized, index, options)