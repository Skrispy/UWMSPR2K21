import sklearn
import sklearn.datasets
from sklearn import tree
from matplotlib import pyplot
from sklearn import metrics
from sklearn import model_selection

def main():

    d = sklearn.datasets.fetch_openml(data_id=1494)
    #QSAR biodegradation data set


 
    def run(x):
        #Declare and run analysis on each decision tree
        mytree = tree.DecisionTreeClassifier(criterion="entropy", min_samples_leaf=x,)
        mytree = mytree.fit(d.data,d.target)
        predicted = mytree.predict(d.data)
        tree_metrics = metrics.accuracy_score(d.target,predicted)
        print("Min leaves ",x)
        print(tree_metrics)
        
        

        
        #K fold cross validation
        scores = model_selection.cross_val_score(mytree,d.data,d.target,cv=10)
        print(scores)
        print("Average accuracy is:",scores.mean())
        plotDec = input("Print plot?(Y,N):")
        if plotDec.lower() == 'y':
            myfig = pyplot.figure(figsize=(25,25))
            a = tree.plot_tree(mytree, filled=True)
            myfig.savefig("dectree_" + str(x) + ".jpg")
    
    value = 1
    while(value>=1):
        value = int(input('Choose a min leaf value >= 1 (-1) to exit:'))
        run(value)1
    

    """
    sample_leaves = [1,5,8,10,17,50,99,150]
    for x in sample_leaves:
        run(x)
    """
main()