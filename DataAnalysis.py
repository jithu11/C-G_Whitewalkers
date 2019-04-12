import pandas as pd
import seaborn as sns
import  matplotlib.pyplot  as plt
data = pd.read_csv("/Users/jithinj/Desktop/Analysis/Bugs.csv")
data.columns
data.dtypes
data.shape
x = data[["Issue key","Priority","Summary","Issue Type","Status"]]
x.columns
sns.countplot(x["Priority"])
sns.plt.show()