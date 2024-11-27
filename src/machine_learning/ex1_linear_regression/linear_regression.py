import matplotlib.pyplot as plt
import pandas


path =  'ex1data1.txt'
data = pandas.read_csv(path, header=None, names=['Population', 'Profit'])
data.head()

data.describe()

data.plot(kind='scatter', x='Population', y='Profit', figsize=(12,8))
plt.show()



