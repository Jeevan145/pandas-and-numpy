import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("mtcars.csv")

plt.hist(df['mpg'])
plt.show()

plt.scatter(df['wt'], df['mpg'])
ply.show()

df['am'].value_counts().plot(kind = 'bar')
plt.show()

plt.boxplot(df['mpg'])
plt.show()