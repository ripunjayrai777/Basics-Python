import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
df=pd.read_csv("C:\Users\RIP\Desktop\Basics-Python\data\htwgtMale.csv")
X = df[["Height"]].values
Y = df["Weight"].values
print(X.values)