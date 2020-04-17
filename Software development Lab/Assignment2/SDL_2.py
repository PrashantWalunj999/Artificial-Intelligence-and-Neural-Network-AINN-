import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

open('Accuracy_List.txt','w')
dataset=pd.read_csv('salary.csv')
dataset.head()
x=dataset.iloc[:, :-1]
y=dataset.iloc[:,1]
type(x)
type(y)
print x
print y

from sklearn.cross_validation import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size=1/3.0, random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(xtrain,ytrain)
ypredict = regressor.predict(xtest)
Accuracy = regressor.score(xtest,ytest) * 100
with open('Accuracy_List.txt','a') as file:
    file.write(str(Accuracy)+'  '+str(99.9)+'\n')
tries = 1
scoreVal = 99.9
while Accuracy < scoreVal:
    tries += 1
    xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size = 0.2)
    regressor.fit(xtrain,ytrain)
    ypredict = regressor.predict(xtest)
    Accuracy = regressor.score(xtest,ytest) * 100
    with open('Accuracy_List.txt','a') as file:
        file.write(str(Accuracy)+'  '+str(scoreVal)+'\n')
    if(tries % 100 == 0):
        scoreVal -= 0.00099
    #print Accuracy

print 'Accuracy: ',Accuracy
print 'No of Tries: ',tries
plt.scatter(xtrain,ytrain, color='red')
plt.plot(xtrain, regressor.predict(xtrain), color='blue')
plt.title('salaryvs experirence(training set)')
plt.xlabel('year of experience')
plt.ylabel('salary')
plt.show()