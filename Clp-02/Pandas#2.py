import pandas as pd

data = {
    "A": [10, 20, None, 40, 50],
    "B": [5, None, 15, 20, 25],
    "C": [None, 1, 2, 3, 4]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

df.fillna(df.mean(), inplace=True)

print("\nDataFrame after filling missing values with column-wise means:")
print(df)