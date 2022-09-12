# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 19:27:18 2021

@author: rxgfilo
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd
import seaborn as sns
iris_dataframe = pd.DataFrame(iris_dataset['data'], columns = iris_dataset.feature_names)
iris_dataframe['target'] = iris_dataset['target']
#iris_dataframe=sns.load_dataset("iris_dataframe")
sns.pairplot(iris_dataframe)
