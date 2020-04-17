#SDL_4 Prashant_Walunj

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn import datasets
iris = datasets.load_iris()
print iris
type(iris)
iris['data']
iris['feature_names']
iris['target']
iris = pd.DataFrame(data=np.c_[iris['data'],iris['target']],columns=iris['feature_names']+['species']) 

#iris.column = iris.columns.str.replace

x=iris.ix[:,:4]
y=iris.ix[:,4]
x.head()

len(x)
len(y)

from sklearn.cluster import KMeans
model = KMeans(n_clusters=3,random_state=11)
model.fit(x)
print model.labels_

iris['pred_species'] = np.choose(model.labels_ , [1,0,2]).astype(np.int64)
print iris

#import
from sklearn.metrics import accuracy_score, classification_report
print "Accuracy:", accuracy_score(iris.species, iris.pred_species) * 100 
print "Classification Report:", classification_report(iris.species, iris.pred_species)

filter = iris['pred_species'] == 1
ndata = iris[filter]
ndata.to_csv('1.csv')

filter = iris['pred_species'] == 0
ndata = iris[filter]
ndata.to_csv('0.csv')

filter = iris['pred_species'] == 2
ndata = iris[filter]
ndata.to_csv('2.csv')

ndata.to_html('2.csv')


col = ['red', 'blue', 'green']
markers = ['o', 'v', 's']

plt.subplot(2,1,1)  #first subplot

x = iris['sepal length (cm)']
y = iris['sepal width (cm)']
plt.plot(x,y,"o")


col = ['red', 'blue', 'green']
markers = ['o', 'v', 's']
for i,l in enumerate(model.labels_):
	plt.plot(x[i],y[i],color=col[l],marker=markers[l])



plt.xlabel('sepal length length (cm)')
plt.xlabel('sepal width (cm)')
plt.title('sepal (Actual)')



plt.subplot(2,1,2)  #second subplot

x = iris['petal length (cm)']
y = iris['petal width (cm)']

for i,l in enumerate(model.labels_):
	plt.plot(x[i],y[i],color=col[l],marker=markers[l])

plt.xlabel('petal length (cm)')
plt.xlabel('petal width (cm)')
plt.title('petal (Actual)')
plt.show()
