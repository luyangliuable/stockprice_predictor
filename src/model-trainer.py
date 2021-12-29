import numpy as np
import pandas as pd
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt

# stocks = input("Enter the code of the stock:- ")
stocks = "TSLA"
# Get Tesla Stocks ############################################################
data = yf.download(stocks, "2008-01-01", "2021-01-18", auto_adjust=True)
data.head()

# Get the data ################################################################
print(data.head())

# Get the same of the data ####################################################
print(data.shape)

# Get the info of the data ####################################################
print(data.info())


# Describe the data ###########################################################
print(data.describe())

data.Close.plot(figsize=(10, 7),color='r')
plt.ylabel("{} Prices".format(stocks))
plt.title("{} Price Series".format(stocks))
plt.savefig("graph.png")
