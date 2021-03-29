import sklearn
import sklearn.datasets
import sklearn.tree
from sklearn import model_selection
import scipy

dia = sklearn.datasets.fetch_openml(data_id=37)
mytree1 = sklearn.tree.DecisionTreeClassifier(criterion="entropy")
scores1 = model_selection.cross_val_score(mytree1, dia.data, dia.target, cv=10)
mytree2 = sklearn.tree.DecisionTreeClassifier(criterion="gini")
scores2 = model_selection.cross_val_score(mytree2, dia.data, dia.target, cv=10)
print(scipy.stats.ttest_ind(scores1, scores2))