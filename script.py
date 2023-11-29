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

file_path = 'dataset.csv'
df = pd.read_csv(file_path)

average_sleep_duration_by_occupation = df.groupby('Occupation')['Sleep Duration'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='Occupation', y='Sleep Duration', data=average_sleep_duration_by_occupation, palette='viridis')
plt.xticks(rotation=45, ha='right')  
plt.xlabel('Occupation')
plt.ylabel('Average Sleep Duration')
plt.title('Average Sleep Duration by Occupation')
plt.show()


average_stress_level_by_occupation = df.groupby('Occupation')['Stress Level'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='Occupation', y='Stress Level', data=average_stress_level_by_occupation, palette='magma')
plt.xticks(rotation=45, ha='right')  
plt.xlabel('Occupation')
plt.ylabel('Average Stress Level')
plt.title('Average Stress Level by Occupation')
plt.show()


average_sleep_duration_by_age = df.groupby('Age')['Sleep Duration'].mean().reset_index()

plt.figure(figsize=(12, 6))
sns.barplot(x='Age', y='Sleep Duration', data=average_sleep_duration_by_age, palette='Blues')
plt.xticks(rotation=45, ha='right')  
plt.xlabel('Age')
plt.ylabel('Average Sleep Duration')
plt.title('Average Sleep Duration by Age')
plt.show()


average_quality_of_sleep_by_age = df.groupby('Age')['Quality of Sleep'].mean().reset_index()

plt.figure(figsize=(12, 6))
sns.barplot(x='Age', y='Quality of Sleep', data=average_quality_of_sleep_by_age, palette='Greens')
plt.xticks(rotation=45, ha='right')
plt.xlabel('Age')
plt.ylabel('Average Quality of Sleep')
plt.title('Average Quality of Sleep by Age')
plt.show()

bmi_category_by_occupation = df.groupby(['Occupation', 'BMI Category']).size().unstack(fill_value=0)
bmi_category_by_occupation = bmi_category_by_occupation.div(bmi_category_by_occupation.sum(axis=1), axis=0)
plt.figure(figsize=(12, 6))
bmi_category_by_occupation.plot(kind='bar', stacked=True, colormap='viridis')
plt.xticks(rotation=45, ha='right')
plt.xlabel('Occupation')
plt.ylabel('Proportion')
plt.title('BMI Category Distribution by Occupation')
plt.legend(title='BMI Category', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()