"""TRAINING ML MODEL"""
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#data set load
df=pd.read_excel('Cleand_yt_analysis.xlsx')

#OPTEMIZATION

X=df[['Subscribers','Views','Videos','Watch_Time']]

#TARGET
y=df['Revenue']

#Spliting
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

#model
model=LinearRegression()

#train
model.fit(X_train,y_train)

#accuracy
print(model.score(X_test,y_test))
