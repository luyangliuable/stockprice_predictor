import numpy as np
import pandas as pd
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt

# Describe the data ###########################################################
data.describe()


# Get the prices and titles ###################################################
data.Close.plot(figsize=(10, 7),color='r')
plt.ylabel("{} Prices".format(stocks))
plt.title("{} Price Series".format(stocks))
plt.show()

# plot the distribution of close  #############################################
sns.distplot(data["Close"])

sns.distplot(data["Open"])

sns.displot(data["High"])

# Conlusions
# - Shape the of the data
# - how our data is distributed
# - It's very very non linear
# Linear, Logis, Regularized, SVM

X = data.drop("Close", axis=1)
y = data["Close"]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test  = train_test_split(X,y,test_size=0.2, random_state=0)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
