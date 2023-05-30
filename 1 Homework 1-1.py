import numpy as np
import operator
import pandas as pd # Для работы с данными
import matplotlib.pyplot as plt  # Библиотека для визуализации результатов

from sklearn.linear_model import LinearRegression # линейная регрессия


data = pd.read_csv('ftp://ftp.cs.toronto.edu/pub/neuron/delve/data/tarfiles/adult.tar.gz', delimiter=',')
data.head()