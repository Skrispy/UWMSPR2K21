import sklearn
import sklearn.datasets
import sklearn.impute
import math
imp = sklearn.impute.SimpleImputer(strategy='most_freaquent')

pbc = sklearn.datasets.fetch_openml(data_id=524)
pbc.data.dropna(axis=1)

for feature in pbc.data.columns :
    c = 0
    for v in pbc.data[feature] :
        if type(v)==float :
            if math.isnan(v) :
                c += 1
    print(feature,c,round((c*100)/len(pbc.data[feature]),1),"%")

if pbc.data[feature].dtype==float :
    m = pbc.data[feature].mean()
    pbc.data[feature] = pbc.data[feature].fillna(m).copy()
else :
    f = pbc.data[feature].mode()[0]
    pbc.data[feature] = pbc.data[feature].fillna(f).copy()