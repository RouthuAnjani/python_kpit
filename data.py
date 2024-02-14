import pandas as pd
import matplotlib.pyplot as plt


file_path= 'example_data.csv'
df = pd.read_csv(file_path)

print("First few rows of the DataFrame: ")
print(df.head())

print("\nDataFrame info: ")
print(df.info())

print("\nSummary Statistics: ")
print(df.describe())

selected_columns=['Name','Age','Salary']
selected_df=df[selected_columns]
print("\nDataFrame with selected Columns: ")
print(selected_df.head())

grouped_data=df.groupby('City')['Salary'].mean()
print("\nAverage Salary by City: ")
print(grouped_data)

df.plot(x='Age', y='Salary', kind='hist', title='Age vs. Salary')
plt.show()
