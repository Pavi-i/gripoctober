# -*- coding: utf-8 -*-
"""GripTask1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UW2F8cLDFZdYomPmawQFNToUgXEt-WRW

SPARKS FOUNDATION_GRIP
#GRIPOCTOBER21
Author Name:PAVITHRA PRADEEP
TASK1: Prediction Using Supervised ML
Predict Percentage of students based on number of study hours.

TASK1: Prediction Using Supervised ML
Predict Percentage of students based on number of study hours.
"""

# Commented out IPython magic to ensure Python compatibility.
#IMPORTING LIBRARIES

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
import statsmodels.api as sm

#READING DATASET FROM URL

url="http://bit.ly/w-data"
dataset=pd.read_csv(url)
dataset

#Exploring nature of DATA

dataset.shape

dataset.head()

dataset.describe()

#Regression
y=dataset['Scores']
x=dataset['Hours']

#Explore data
plt.scatter(x,y)
plt.xlabel('Hours',fontsize=15)
plt.ylabel('Percentage',fontsize=15)
plt.grid()
plt.show()

x1=sm.add_constant(x)
results=sm.OLS(y,x1).fit()  #The result will contain the o/p of the Ordinary Least Squares(OLS) Regression.
results.summary()

#Apply output to equation and rerun the code
plt.scatter(x,y)
yhat= 9.7758*x+2.4837
fig=plt.plot(x,yhat,lw=4,c='orange',label='regression line')
plt.xlabel('Hours',fontsize=20)
plt.ylabel('Scores',fontsize=20)
plt.grid()
plt.show()

#CORRELATION
dataset.corr(method='pearson')

dataset.corr(method='spearman')

#Linear Regression
#using iloc function we divide the data

X=dataset.iloc[:,:1].values
Y=dataset.iloc[:,1:].values

X

Y

#Splitting Data into training and testing

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=0)

#Training our Model

from sklearn.linear_model import LinearRegression  

model = LinearRegression()  
model.fit(X_train, Y_train)

#Visualizing train data
line = model.coef_*X + model.intercept_

# Plotting for the training data
plt.rcParams["figure.figsize"] = [14,7]
plt.scatter(X_train, Y_train, color='blue')
plt.plot(X, line, color='orange');
plt.xlabel('Hours Studied',fontsize=20)  
plt.ylabel('Percentage Score',fontsize=20) 
plt.grid()
plt.show()

# Plotting for the testing data

plt.rcParams["figure.figsize"] = [14,7]
plt.scatter(X_test, Y_test, color='blue')
plt.plot(X, line, color='orange');
plt.xlabel('Hours Studied',fontsize=20)  
plt.ylabel('Percentage Score',fontsize=20) 
plt.grid()
plt.show()

#Making Predictions
print(X_test)
y_pred=model.predict(X_test)

# Comparing Actual vs Predicted
comp = pd.DataFrame({ 'Actual':[Y_test],'Predicted':[y_pred] })
comp

"""
What will be the predicted score if a student studies for 9.25 hrs/day?"""

# Testing with your own data
hours = 9.25
own_pred = model.predict([[hours]])
print("The predicted score if a student studies for",hours,"hours is",own_pred[0])

#MODEL EVALUATION
from sklearn import metrics 
print('Mean Absolute Error:', metrics.mean_absolute_error(Y_test, y_pred))

