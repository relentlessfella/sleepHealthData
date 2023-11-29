import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dataset.csv')
print(df.info())
print(df.head())
print(df.describe())
print(df.isnull().sum())
plt.figure(figsize=(13, 10))

plt.subplot(2, 2, 1)
df['Gender'].value_counts().plot(kind='bar')
plt.title('Gender Distribution')

plt.subplot(2, 2, 2)
df['Occupation'].value_counts().plot(kind='bar')
plt.title('Occupation Distribution')

plt.subplot(2, 2, 3)
df['BMI Category'].value_counts().plot(kind='bar')
plt.title('BMI Category Distribution')

plt.subplot(2, 2, 4)
sns.boxplot(x='Quality of Sleep', y='Sleep Duration', data=df)
plt.xlabel('Quality of Sleep')
plt.ylabel('Sleep Duration (hours)')
plt.title('Quality of Sleep vs. Sleep Duration')

plt.tight_layout()

plt.figure(figsize=(8, 6))
sns.countplot(x='Stress Level', data=df, palette='viridis')
plt.xlabel('Stress Level')
plt.ylabel('Number of People')
plt.title('Number of People at Each Stress Level')

plt.show()
