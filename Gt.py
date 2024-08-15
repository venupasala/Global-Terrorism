import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("globalterrorismdb_0718dist.csv", encoding='latin1')
df.head()
df.head()

# Shape of the dataset
df.shape

# Descriptive statistics
df.describe()

# Data types of each column
df.dtypes
df['country_txt'].value_counts().head(10)

# Top 10 cities with most attacks
df['city'].value_counts().head(10)
plt.figure(figsize=(12,6))
sns.countplot(x='iyear', data=df)
plt.xlabel('Year')
plt.ylabel('Number of Attacks')
plt.title('Number of Terrorist Attacks by Year')
plt.xticks(rotation=90)
plt.show()