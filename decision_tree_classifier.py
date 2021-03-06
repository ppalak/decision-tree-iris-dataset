# -*- coding: utf-8 -*-
"""Decision Tree Classifier.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1InACVLZguIyY4Kv4TjkKHXj-6L3HDgk1

#Sparks GRIP Program

Name : Palak Patwa

Task NO. : 6 - Decision Tree Classifier

Position : Data Science and Business Analytics Intern

1. Understanding the Data
"""

#Importing the Dataset
from google.colab import drive
drive.mount('/content/drive')

#Ignore warnings
import warnings
warnings.filterwarnings('ignore')

#Importing the libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#reading the csv file
data = pd.read_csv('/content/drive/MyDrive/Iris.csv')

data.info()

data.shape

data.isnull().sum()

data.head()

"""2. Data Preparation"""

# using label encoder for categorical variables
from sklearn.preprocessing import LabelEncoder

df_categorical = data.select_dtypes(include=['object'])
df_categorical.head()

le = LabelEncoder()
df_categorical = df_categorical.apply(le.fit_transform)
df_categorical.head()

# concat df_categorical with original data
df = data.drop(df_categorical.columns, axis=1)
df = pd.concat([df, df_categorical], axis=1)
df.head()

df.info()

df['Species'] = df['Species'].astype('category')

"""3. Building Model"""

# Importing train-test-split 
from sklearn.model_selection import train_test_split

# Putting feature variable to X
X = df.drop('Species',axis=1)

# Putting response variable to y
y = df['Species']

# Splitting the data into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.30,random_state = 99)

X_train.head()

# Importing decision tree classifier from sklearn library
from sklearn.tree import DecisionTreeClassifier

# Fitting the decision tree with default hyperparameters, apart from
# max_depth which is 5 so that we can plot and read the tree.
dt_default = DecisionTreeClassifier(max_depth=5)
dt_default.fit(X_train, y_train)

# Let's check the evaluation metrics of our default model

# Importing classification report and confusion matrix from sklearn metrics
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Making predictions
y_pred_default = dt_default.predict(X_test)

# Printing classification report
print(classification_report(y_test, y_pred_default))

# Printing confusion matrix and accuracy
print(confusion_matrix(y_test,y_pred_default))
print(accuracy_score(y_test,y_pred_default))

# Importing required packages for visualization
from IPython.display import Image  
from sklearn.externals.six import StringIO  
from sklearn.tree import export_graphviz
import pydotplus, graphviz

# Putting features
features = list(df.columns[1:])
features

# plotting tree with max_depth=3
dot_data = StringIO()  
export_graphviz(dt_default, out_file=dot_data,
                feature_names=features, filled=True,rounded=True)

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
Image(graph.create_png())

