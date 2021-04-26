import tensorflow as tf
import numpy as np
import sklearn
import sklearn.datasets
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import KFold
from tensorflow.keras import models,layers

def classification_example() :   
    iris = sklearn.datasets.fetch_openml(data_id=61) # iris dataset
        # one-hot encoding for target    
    enc = OneHotEncoder()    

    tmp = [] # list of one-element lists    
    for i in range(len(iris.target)) :        
        tmp.append([iris.target[i]])    
    ohe = enc.fit_transform(tmp)    
    target = ohe.toarray()    
        
    # cross validation    
    kfolds = KFold(n_splits=10, shuffle=True)
    fold_auc = [] # list to store AUC of each fold    
    for train, test in kfolds.split(iris.data, target) :
        # build neural network        
        nn = models.Sequential()        
        nn.add(layers.Dense(5, activation="relu", input_dim=4))        
        nn.add(layers.Dense(3, activation='softmax'))        
        nn.compile(optimizer='SGD', loss='categorical_crossentropy',

metrics=[tf.keras.metrics.AUC()])        
        # training        
        nn.fit(iris.data.iloc[train], target[train], epochs=100)        
        # testing        
        s = nn.evaluate(iris.data.iloc[test], target[test])        
        fold_auc.append(s[1])        
        print("Fold",len(fold_auc),"AUC =",s[1])    
    print("AUC for all folds:",fold_auc)    
    print("Average AUC:",np.mean(fold_auc))

classification_example()