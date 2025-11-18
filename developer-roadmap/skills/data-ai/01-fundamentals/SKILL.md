---
name: data-fundamentals
description: Master data science fundamentals. Learn Python for data, statistics, pandas, data visualization, and exploratory data analysis.
---

# Data Science Fundamentals

## Python for Data
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Data loading
df = pd.read_csv('data.csv')

# Exploration
df.head()
df.info()
df.describe()
df.isnull().sum()

# Cleaning
df.fillna(df.mean())
df.drop_duplicates()
df['column'] = df['column'].astype('int')

# Filtering
df[df['age'] > 18]
df.loc[df['city'] == 'NYC']

# Grouping
df.groupby('category').agg({'sales': 'sum', 'quantity': 'mean'})

# Merging
pd.merge(df1, df2, on='id', how='left')
```

## Statistics
```python
# Descriptive statistics
mean = df['column'].mean()
std = df['column'].std()
correlation = df['col1'].corr(df['col2'])

# Hypothesis testing
from scipy import stats
t_stat, p_value = stats.ttest_ind(group1, group2)

# Distributions
from scipy.stats import norm
prob = norm.cdf(value)
```

## Visualization
```python
import matplotlib.pyplot as plt
import seaborn as sns

# Line plot
plt.plot(df['date'], df['value'])

# Histogram
plt.hist(df['age'], bins=30)

# Scatter plot
plt.scatter(df['x'], df['y'])

# Heatmap
sns.heatmap(correlation_matrix, annot=True)

plt.show()
```

## Exploratory Data Analysis
1. Load and inspect data
2. Check missing values
3. Understand distributions
4. Find correlations
5. Identify outliers
6. Segment data
7. Create features

## Key Concepts

✅ Data types & structures
✅ Statistical concepts
✅ Data quality
✅ Feature types
✅ Sampling methods
✅ Bias & variance
✅ Data visualization
✅ Data pipelines

