
# A sample proggram that generates a decision tree and saves its image.
import sklearn
import sklearn.datasets
from sklearn import tree
from matplotlib import pyplot

def main() :
    d = sklearn.datasets.load_iris()    
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

    myfig = pyplot.figure(figsize=(25,25))    
    a = tree.plot_tree(mytree, feature_names=d.feature_names,
                           class_names=d.target_names, filled=True)

    myfig.savefig("decision_tree.jpg")    
    print("The tree has been saved to decision_tree.jpg file.")

main()

