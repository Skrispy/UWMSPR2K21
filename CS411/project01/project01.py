import sklearn
import sklearn.datasets
from sklearn import tree
from matplotlib import pyplot

def main():
    d = sklearn.datasets.fetch_openml(data_id=1489)
    print(d.feature_names)
    print(d.target_names)    

    print(d.target)    
    print(type(d.target))    
    print(d.target.shape)    

    print(d.data)    
    print(type(d.data))    
    print(d.data.shape) 
    mytree = tree.DecisionTreeClassifier(criterion="entropy")
    mytree = mytree.fit(d.data,d.target)
main()