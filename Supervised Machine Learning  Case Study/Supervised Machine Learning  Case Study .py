from sklearn.datasets import load_iris;
import numpy as np
from sklearn import tree

iris=load_iris()
print("Feature name=:")
print(iris.feature_names)
print("Label =")
print(iris.target_names)


# for i in range(len(iris.target)):
# 	print("ID:%d,label :%s,feature:%s" %(i,iris.data[i],iris.target[i]))
test=[1,51,110]

train_f=np.delete(iris.target,test)
train_data=np.delete(iris.data ,test, axis=0)

test_f=iris.target[test]
test_data=iris.data[test]

algo=tree.DecisionTreeClassifier()
algo.fit(train_data,train_f)

print("Value Of Accepted Result")
print(test_f)

print("Algo Result=")
result=algo.predict(test_data)

print(result)



from sklearn.externals.six import StringIO
import pydot

dot_data=StringIO()
tree.export_graphviz(algo,out_file=dot_data,feature_names=iris.feature_names,class_names=iris.target_names,filled=True,rounded=True,impurity=False)
graph=pydot.graph_from_dot_data(dot_data.getvalue())
graph[0].write_pdf("tree.pdf")





# output-:

# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/ML/Application/irice
# $ python iris.py
# Feature name=:
# ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
# Label =
# ['setosa' 'versicolor' 'virginica']
# Value Of Result
# [0 1 2]
# Algo Result=
# [0 1 2]

