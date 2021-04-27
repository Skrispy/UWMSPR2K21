import tensorflow as tf
import numpy as np
import sklearn
import pandas as pd

import sklearn.datasets
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import KFold
from tensorflow.keras import models,layers

enc = OneHotEncoder()

a = sklearn.datasets.fetch_openml(data_id=31)
#Good or bad credit scores(categorical)

b = sklearn.datasets.fetch_openml(data_id=42688)
#houses for sale(regression)
#popping dates
#no missing features in these datasets

#transform nominal features in A
ctA = ColumnTransformer([('encoder', OneHotEncoder(handle_unknown='ignore'), [0,2,3,5,6,8,9,11,13,14,16,18,19])], remainder='passthrough')
oheA = ctA.fit_transform(a.data)
new_aData = pd.DataFrame(oheA, columns = ctA.get_feature_names(), index = a.data.index) 

print(new_aData)

def dataA():
    #testing
    tmpA = [] # list of one-element lists    
    for i in range(len(a.target)) :        
        tmpA.append([a.target[i]])
    oheA = enc.fit_transform(tmpA)
    targetA = oheA.toarray()
    print(targetA)

    # cross validation    
    kfolds = KFold(n_splits=10, shuffle=True)
    fold_auc = [] # list to store AUC of each fold    
    for train, test in kfolds.split(new_aData, targetA) :
        # build neural network        
        nn = models.Sequential()        
        nn.add(layers.Dense(5, activation="relu", input_dim=4))        
        nn.add(layers.Dense(3, activation='softmax'))        
        nn.compile(optimizer='SGD', loss='categorical_crossentropy',metrics=[tf.keras.metrics.AUC()])        
        # training        
        nn.fit(new_aData.iloc[train], targetA[train], epochs=100)        
        # testing        
        s = nn.evaluate(new_aData.iloc[test], targetA[test])        
        fold_auc.append(s[1])                    
        print("Fold",len(fold_auc),"AUC =",s[1])    
    print("AUC for all folds:",fold_auc)    
    print("Average AUC:",np.mean(fold_auc))


dataA()

    



#transform nominal features in B
        
#ctB = ColumnTransformer([('encoder', OneHotEncoder(handle_unknown='ignore'), [0,5,6,7])], remainder='passthrough')
#oheB = ctB.fit_transform(b.data)
#new_bData = pd.DataFrame.sparse.from_spmatrix(oheB, columns = ctB.get_feature_names(), index = b.data.index)