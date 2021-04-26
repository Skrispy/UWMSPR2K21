import tensorflow as tf
import numpy as np
import sklearn
import pandas

import sklearn.datasets
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import KFold
from tensorflow.keras import models,layers

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

#transform nominal features in B
    
ctB = ColumnTransformer([('encoder', OneHotEncoder(handle_unknown='ignore'), [0,5,6,7])], remainder='passthrough')
oheB = ctB.fit_transform(b.data)
new_bData = pd.DataFrame.sparse.from_spmatrix(oheB, columns = ctB.get_feature_names(), index = b.data.index)

def regression() : 
    (x_train, y_train), (x_test, y_test) = new_aData.load_data()
    print(x_train.shape)

regression()