import pandas as pd

data={'Name': ['Alice', 'Bob', 'Charlie', 'David'],
      'Age':[25,30,35,40],
      'City':['New York', 'San Francisco', 'Los Angeles', 'Chicago']}

df=pd.DataFrame(data)

print("Original DataFrame: ")
print(df)

print("\nAccessing specific columns: ")
print(df['Name'])
print(df[['Name','Age']])

print("\nFiltering data based on a condition: ")
filtered_df=df[df['Age']>30]
print(filtered_df)

df['Salary']=[50000,60000,70000,80000]
print("\nDataFrame after adding a new column: ")
print(df)

print("\nBasic Statistics: ")
print(df.describe())
print(df.info())