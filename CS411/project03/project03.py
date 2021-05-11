import tensorflow as tf
import numpy as np
import sklearn
import pandas as pd

import sklearn.datasets
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import KFold
from tensorflow.keras import models,layers
from matplotlib import pyplot

enc = OneHotEncoder()

a = sklearn.datasets.fetch_openml(data_id=31)
#Good or bad credit scores(categorical)

b = sklearn.datasets.fetch_openml(data_id=42688)
#houses for sale(regression)
#popping dates
#no missing features in these datasets(Categorical)

#transform categorical features in A
ctA = ColumnTransformer([('encoder', OneHotEncoder(handle_unknown='ignore'), [0,2,3,5,6,8,9,11,13,14,16,18,19])], remainder='passthrough')
oheA = ctA.fit_transform(a.data)
new_aData = pd.DataFrame(oheA, columns = ctA.get_feature_names(), index = a.data.index)
print(new_aData.shape)
#print(type(new_aData))

#Encode categorical Targets for A
tmpA = [] # list of one-element lists
for i in range(len(a.target)) :        
    tmpA.append([a.target[i]])
oheA = enc.fit_transform(tmpA)
targetA = oheA.toarray()
#print(targetA)
#print(targetA.shape)

#transform categorical features in B(Regression)
ctB = ColumnTransformer([('encoder', OneHotEncoder(handle_unknown='ignore'), [0,5,6,7])], remainder='passthrough')
oheB = ctB.fit_transform(b.data)
new_bData = pd.DataFrame.sparse.from_spmatrix(oheB, columns = ctB.get_feature_names(), index = b.data.index)
#print(new_bData)
#print(new_bData.shape)

#testing
#tmpB = [] # list of one-element lists    
#for i in range(len(b.target)) :        
#    tmpB.append([b.target[i]])
#oheB = enc.fit_transform(tmpB)
#targetB = oheB.toarray()
#print(b.target)
#print(b.target.shape)

class Result:
    def __init__(self,method,result):
        self.method = method
        self.result = result

results = []

def noHLDataA():
    print("Building a no Hidden Layer network for dataset A")
    # cross validation    
    kfolds = KFold(n_splits=10, shuffle=True)
    fold_auc = [] # list to store AUC of each fold    
    for train, test in kfolds.split(new_aData, targetA) :
        # build neural network        
        nn = models.Sequential()        
        nn.add(layers.Dense(1, activation="relu", input_dim=61))        
        nn.add(layers.Dense(2, activation='softmax'))
        nn.compile(optimizer='SGD', loss='categorical_crossentropy',metrics=[tf.keras.metrics.AUC()])        
        # training        
        nn.fit(new_aData.iloc[train],targetA[train], epochs=20)        
        # testing        
        s = nn.evaluate(new_aData.iloc[test],targetA[test])        
        fold_auc.append(s[1])
        print("Fold",len(fold_auc),"AUC =",s[1])    
    print("AUC for all folds:",fold_auc)    
    print("Average AUC:",np.mean(fold_auc))
    x = Result("No Hidden Layer Dataset A",np.mean(fold_auc))
    results.append(x)

def lowHLDataA():
    print("Building a low Hidden Layer network for dataset A")
    # cross validation    
    kfolds = KFold(n_splits=10, shuffle=True)
    fold_auc = [] # list to store AUC of each fold    
    for train, test in kfolds.split(new_aData, targetA) :
        # build neural network        
        nn = models.Sequential()        
        nn.add(layers.Dense(100, activation="relu", input_dim=61))        
        nn.add(layers.Dense(2, activation='softmax'))
        nn.compile(optimizer='SGD', loss='categorical_crossentropy',metrics=[tf.keras.metrics.AUC()])        
        # training        
        nn.fit(new_aData.iloc[train],targetA[train], epochs=20)        
        # testing        
        s = nn.evaluate(new_aData.iloc[test],targetA[test])        
        fold_auc.append(s[1])
        print("Fold",len(fold_auc),"AUC =",s[1])    
    print("AUC for all folds:",fold_auc)    
    print("Average AUC:",np.mean(fold_auc))
    x = Result("Low Hidden Layer Dataset A",np.mean(fold_auc))
    results.append(x)

def highHLDataA():
    print("Building a high Hidden Layer network for dataset A")
    # cross validation    
    kfolds = KFold(n_splits=10, shuffle=True)
    fold_auc = [] # list to store AUC of each fold    
    for train, test in kfolds.split(new_aData, targetA) :
        # build neural network        
        nn = models.Sequential()        
        nn.add(layers.Dense(400, activation="relu", input_dim=61))        
        nn.add(layers.Dense(2, activation='softmax'))
        nn.compile(optimizer='SGD', loss='categorical_crossentropy',metrics=[tf.keras.metrics.AUC()])        
        # training        
        nn.fit(new_aData.iloc[train],targetA[train], epochs=20)        
        # testing        
        s = nn.evaluate(new_aData.iloc[test],targetA[test])        
        fold_auc.append(s[1])
        print("Fold",len(fold_auc),"AUC =",s[1])    
    print("AUC for all folds:",fold_auc)    
    print("Average AUC:",np.mean(fold_auc))
    x = Result("High Hidden Layer Dataset A",np.mean(fold_auc))
    results.append(x)

def noHLDataB(): 
    print("Building a no Hidden Layer network for dataset B")
    kfolds = KFold(n_splits=10, shuffle=True)
    fold_rmse = [] # list to store AUC of each fold    
    for train, test in kfolds.split(new_bData, b.target) :
    #build nn
        nn = models.Sequential()        
        nn.add(layers.Dense(1, activation='relu', input_dim=52))        
        nn.add(layers.Dense(1, activation='relu'))        
        nn.compile(optimizer='rmsprop', loss='mse',metrics=['mae','mse'])
        # training        
        bFit = nn.fit(new_bData.iloc[train],b.target[train], epochs=25)
        s = nn.evaluate(new_bData.iloc[test],b.target[test]) 
        fold_rmse.append(s[1])
        print("Fold",len(fold_rmse),"rmse =",s[1]) 
        #pyplot.plot(bFit.history['mse'])
        #pyplot.ylabel('MSE')
        #pyplot.xlabel('Epoch')
        #pyplot.show()
    print("RMSE for all folds:",fold_rmse)    
    print("Average RMSE:",np.mean(fold_rmse))
    x = Result("No Hidden Layer Dataset B",np.mean(fold_rmse))
    results.append(x)

def lowHLDataB(): 
    print("Building a low Hidden Layer network for dataset B")
    kfolds = KFold(n_splits=10, shuffle=True)
    fold_rmse = [] # list to store AUC of each fold    
    for train, test in kfolds.split(new_bData, b.target) :
    #build nn
        nn = models.Sequential()        
        nn.add(layers.Dense(10, activation='relu', input_dim=52))        
        nn.add(layers.Dense(1, activation='relu'))        
        nn.compile(optimizer='rmsprop', loss='mse',metrics=['mae','mse'])
        # training        
        bFit = nn.fit(new_bData.iloc[train],b.target[train], epochs=25)
        s = nn.evaluate(new_bData.iloc[test],b.target[test]) 
        fold_rmse.append(s[1])
        print("Fold",len(fold_rmse),"rmse =",s[1]) 
        #pyplot.plot(bFit.history['mse'])
        #pyplot.ylabel('MSE')
        #pyplot.xlabel('Epoch')
        #pyplot.show()
    print("RMSE for all folds:",fold_rmse)    
    print("Average RMSE:",np.mean(fold_rmse))
    x = Result("Low Hidden Layer Dataset B",np.mean(fold_rmse))
    results.append(x)

def highHLDataB(): 
    print("Building a high Hidden Layer network for dataset A")
    kfolds = KFold(n_splits=10, shuffle=True)
    fold_rmse = [] # list to store AUC of each fold    
    for train, test in kfolds.split(new_bData, b.target) :
    #build nn
        nn = models.Sequential()        
        nn.add(layers.Dense(100, activation='relu', input_dim=52))        
        nn.add(layers.Dense(1, activation='relu'))        
        nn.compile(optimizer='rmsprop', loss='mse',metrics=['mae','mse'])
        # training        
        bFit = nn.fit(new_bData.iloc[train],b.target[train], epochs=25)
        s = nn.evaluate(new_bData.iloc[test],b.target[test]) 
        fold_rmse.append(s[1])
        print("Fold",len(fold_rmse),"rmse =",s[1]) 
        #pyplot.plot(bFit.history['mse'])
        #pyplot.ylabel('MSE')
        #pyplot.xlabel('Epoch')
        #pyplot.show()
    print("RMSE for all folds:",fold_rmse)    
    print("Average RMSE:",np.mean(fold_rmse))
    x = Result("High Hidden Layer Dataset B",np.mean(fold_rmse))
    results.append(x)


noHLDataA()
lowHLDataA()
highHLDataA()
noHLDataB()
lowHLDataB()
highHLDataB()


for res in results:
    print("Method: "+ res.method)
    print(res.result)
