import sklearn
import sklearn.datasets
from sklearn import tree
from sklearn import neighbors
from sklearn import naive_bayes
from sklearn import linear_model
from sklearn import svm
from sklearn import dummy
import pandas as pd
import scipy

from matplotlib import pyplot
from sklearn import metrics
from sklearn import model_selection
from scipy.stats import ttest_ind
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import GridSearchCV 

from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.dummy import DummyClassifier
from sklearn.svm import SVC

from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_squared_error


class Result:
    def __init__(self,method,result):
        self.method = method
        self.result = result


def main():
    resultsA=[]
    resultsB=[]
    a = sklearn.datasets.fetch_openml(data_id=31)
    #Good or bad credit scores(categorical)

    b = sklearn.datasets.fetch_openml(data_id=42688)
    #houses for sale(regression)
    #popping dates
    #no missing features in these datasets
    
    #B testing

    


    #transform nominal features in A
    ctA = ColumnTransformer([('encoder', OneHotEncoder(handle_unknown='ignore'), [0,2,3,5,6,8,9,11,13,14,16,18,19])], remainder='passthrough')
    oheA = ctA.fit_transform(a.data)
    new_aData = pd.DataFrame(oheA, columns = ctA.get_feature_names(), index = a.data.index) 


    #transform nominal features in B
    
    ctB = ColumnTransformer([('encoder', OneHotEncoder(handle_unknown='ignore'), [0,5,6,7])], remainder='passthrough')
    oheB = ctB.fit_transform(b.data)
    new_bData = pd.DataFrame.sparse.from_spmatrix(oheB, columns = ctB.get_feature_names(), index = b.data.index).sample(frac=0.20)
    bTarget = b.target.sample(frac=0.20)
    #sampling 20% of the data for ease of use


    """
    #testing
    parameters = [{"min_samples_leaf":[2,4,6,8,10]}]
    tr = DecisionTreeRegressor()
    parameter_search = GridSearchCV(tr, parameters, cv=10,scoring="neg_root_mean_squared_error",refit=True)
    parameter_search.fit(new_bData, bTarget)
    print(parameter_search.best_params_)
    bTest  = parameter_search.predict(new_bData)
    print(mean_squared_error(bTarget, bTest))
    """

    print("starting method testing...")
    
    #Dataset A Classification Methods
    #Decision tree parameter tuning for dataset A
    trC = DecisionTreeClassifier()
    parametersA = [{"min_samples_leaf":[32,34,35,36,37,40]}]

    parameter_searchA = GridSearchCV(trC, parametersA, cv=10,scoring="roc_auc",refit=True)
    parameter_searchA.fit(new_aData, a.target)
    #print(parameter_searchA.best_params_)

    metaA = GridSearchCV(trC, parametersA, cv=5,scoring="roc_auc", refit=True)
    cv_resultA = cross_val_score(metaA, new_aData, a.target, cv=10, scoring="roc_auc")
    aucA = cv_resultA.mean()
    #print("Dataset A Decision Tree mean Area under curve = " + aucA)
    x = Result("DecisionTreeClassifier",cv_resultA)
    resultsA.append(x)
    print("keep waiting")

    #KNN tuning for datasetA
    knnA = KNeighborsClassifier()
    nParamsA = [{"n_neighbors":[15,20,25,30]}]

    nParamsA_search = GridSearchCV(knnA, nParamsA, cv=10,scoring="roc_auc")
    nParamsA_search.fit(new_aData, a.target)
    #print(nParamsA_search.best_params_)
    metaKnnA = GridSearchCV(knnA, nParamsA, cv=5,scoring="roc_auc", refit=True)
    cv_resultKnnA = cross_val_score(metaKnnA, new_aData, a.target, cv=10, scoring="roc_auc")
    knnAauc = cv_resultKnnA.mean()
    #print("Dataset A KNN mean Area under curve = " + str(knnAauc))
    x = Result("KNeighborsClassifier",cv_resultKnnA)
    resultsA.append(x)
    print('hang in there')
    #NaiveBayes tuning for datasetA
    nbA = MultinomialNB()
    nbParamsA = [{"alpha":[.5,.6,.7,.8]}]

    nbParamsA_search = GridSearchCV(nbA, nbParamsA, cv=10,scoring="roc_auc")
    nbParamsA_search.fit(new_aData, a.target)
    #print(nbParamsA_search.best_params_)
    metaNbA = GridSearchCV(nbA, nbParamsA, cv=5,scoring="roc_auc", refit=True)
    cv_resultNbA = cross_val_score(metaNbA, new_aData, a.target, cv=10, scoring="roc_auc")
    nbAauc = cv_resultNbA.mean()
    #print("Dataset A Naive Bayes mean Area under curve = " + str(nbAauc))
    x = Result("MultinomialNB",cv_resultNbA)
    resultsA.append(x)

    #LogisticRegression tuning for datasetA
    lrA = LogisticRegression()
    lrParamsA = [{"max_iter":[1500,2000,3000]}]

    lrParamsA_search = GridSearchCV(lrA, lrParamsA, cv=10,scoring="roc_auc")
    lrParamsA_search.fit(new_aData, a.target)
    #print(lrParamsA_search.best_params_)
    metaLrA = GridSearchCV(lrA, lrParamsA, cv=5,scoring="roc_auc", refit=True)
    cv_resultLrA = cross_val_score(metaLrA, new_aData, a.target, cv=10, scoring="roc_auc")
    lrAauc = cv_resultLrA.mean()
    #print("Dataset A Logistic Regression mean Area under curve = " + str(lrAauc))
    x = Result("MLogisticRegression",cv_resultLrA)
    resultsA.append(x)
    
    print('i know its taking a while. big data')

    #SVM tuning for datasetA
    svcA = SVC()
    svcParamsA = [{"probability":[True,False]}]

    svcParamsA_search = GridSearchCV(svcA, svcParamsA, cv=10,scoring="roc_auc")
    svcParamsA_search.fit(new_aData, a.target)
    #print(svcParamsA_search.best_params_)
    metaSvcA = GridSearchCV(svcA, svcParamsA, cv=5,scoring="roc_auc", refit=True)
    cv_resultSvcA = cross_val_score(metaSvcA, new_aData, a.target, cv=10, scoring="roc_auc")
    svcAauc = cv_resultSvcA.mean()
    #print("Dataset A SVM mean Area under curve = " + str(svcAauc))
    x = Result("SVC",cv_resultSvcA)
    resultsA.append(x)
    

    #Dummy tuning for datasetA
    dumA = DummyClassifier()
    dumParamsA = [{"strategy":["prior"]}]

    dumParamsA_search = GridSearchCV(dumA, dumParamsA, cv=10,scoring="roc_auc")
    dumParamsA_search.fit(new_aData, a.target)
    #print(dumParamsA_search.best_params_)
    metaDumA = GridSearchCV(dumA, dumParamsA, cv=5,scoring="roc_auc", refit=True)
    cv_resultDumA = cross_val_score(metaDumA, new_aData, a.target, cv=10, scoring="roc_auc")
    dumAauc = cv_resultDumA.mean()
    #print("Dataset A Dummy mean Area under curve = " + str(dumAauc))
    dumResA = Result("DummyClassifier",cv_resultDumA)
    


    print('on to dataset B')

    
    #Dataset B Regression Methods
    
    #Dummy tuning for datasetB
    dumB = DummyRegressor()
    dumParamsB = [{"strategy":["mean"]}]

    dumParamsB_search = GridSearchCV(dumB, dumParamsB, cv=10,scoring="neg_root_mean_squared_error")
    dumParamsB_search.fit(new_bData, bTarget)

    #print(dumParamsB_search.best_params_)

    metaDumB = GridSearchCV(dumB, dumParamsB, cv=5,scoring="neg_root_mean_squared_error", refit=True)
    cv_resultDumB = cross_val_score(metaDumB, new_bData, bTarget, cv=10, scoring="neg_root_mean_squared_error")
    dumBRMSE = cv_resultDumB.mean()
    #print("Dataset B Dummy mean neg_root_mean_squared_error = " + str(dumBRMSE))
    dumResB = Result("DummyRegressor",cv_resultDumB)
    

    #Descision tree Regressor tuning for datasetB
    trrB = DecisionTreeRegressor()
    trrParamsB = [{"min_samples_leaf":[1,20,100,400]}]

    trrParamsB_search = GridSearchCV(trrB, trrParamsB, cv=10,scoring="neg_root_mean_squared_error")
    trrParamsB_search.fit(new_bData, bTarget)

    #print(trrParamsB_search.best_params_)

    metaTrrB = GridSearchCV(trrB, trrParamsB, cv=5,scoring="neg_root_mean_squared_error", refit=True)
    cv_resultTrrB = cross_val_score(metaTrrB, new_bData, bTarget, cv=10, scoring="neg_root_mean_squared_error")
    trrBRMSE = cv_resultTrrB.mean()
    #print("Dataset B Tree Regressor mean neg_root_mean_squared_error = " + str(trrBRMSE))
    x = Result("DecisionTreeRegressor",cv_resultTrrB)
    resultsB.append(x)

    #KNN Regressor tuning for datasetB
    knnrB = KNeighborsRegressor()
    knnrParamsB = [{"n_neighbors":[40,50,100,200,400]}]

    knnrParamsB_search = GridSearchCV(knnrB, knnrParamsB, cv=10,scoring="neg_root_mean_squared_error")
    knnrParamsB_search.fit(new_bData, bTarget)

    #print(knnrParamsB_search.best_params_)

    metaKnnrB = GridSearchCV(knnrB, knnrParamsB, cv=5,scoring="neg_root_mean_squared_error", refit=True)
    cv_resultKnnrB = cross_val_score(metaKnnrB, new_bData, bTarget, cv=10, scoring="neg_root_mean_squared_error")
    knnrBRMSE = cv_resultKnnrB.mean()
    #print("Dataset B NN Regressor mean neg_root_mean_squared_error = " + str(knnrBRMSE))
    x = Result("KNeighborsRegressor",cv_resultKnnrB)
    resultsB.append(x)

    #Linear Regressor tuning for datasetB
    linB = LinearRegression()
    linParamsB = [{"fit_intercept":[True]}]

    linParamsB_search = GridSearchCV(linB, linParamsB, cv=10,scoring="neg_root_mean_squared_error")
    linParamsB_search.fit(new_bData, bTarget)

    #print(linParamsB_search.best_params_)

    metaLinB = GridSearchCV(linB, linParamsB, cv=5,scoring="neg_root_mean_squared_error", refit=True)
    cv_resultLinB = cross_val_score(metaLinB, new_bData, bTarget, cv=10, scoring="neg_root_mean_squared_error")
    linBRMSE = cv_resultLinB.mean()
    #print("Dataset B Linear Regressor mean neg_root_mean_squared_error = " + str(linBRMSE))
    x = Result("LinearRegression",cv_resultLinB)
    resultsB.append(x)
    print("done!")

    '''
    #SVR Regressor tuning for datasetB
    svB = SVR()
    svParamsB = [{"degree":[3]}]

    svParamsB_search = GridSearchCV(svB, svParamsB, cv=10,scoring="neg_root_mean_squared_error")
    svParamsB_search.fit(new_bData, bTarget)

    print(svParamsB_search.best_params_)

    metaSvB = GridSearchCV(svB, svParamsB, cv=5,scoring="neg_root_mean_squared_error", refit=True)
    cv_resultSvB = cross_val_score(metaSvB, new_bData, bTarget, cv=10, scoring="neg_root_mean_squared_error")
    svBRMSE = cv_resultSvB.mean()
    print("Dataset B SVR mean neg_root_mean_squared_error = " + str(svBRMSE))
    x = Result("SVR",cv_resultSvB)
    results.append(x)
    '''




    print('\n results from A comming in hot! \n')

    for res in resultsA:
        x = res.result
        y = dumResB.result
        pvalue = ttest_ind(x.flatten(), y.flatten())
        print("Method: "+ res.method)
        print("P-test")
        print(pvalue)
    
    print('\n results from B comming in hot! \n')

    for res in resultsB:
        x = res.result
        y = dumResB.result
        pvalue = ttest_ind(x.flatten(), y.flatten())
        print("Method: "+ res.method)
        print("P-test")
        print(pvalue)


main()
