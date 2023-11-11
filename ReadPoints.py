import pandas as pd

# Read the CSV file into a pandas dataframe
df = pd.read_csv('IMG_3212.csv', index_col=0)
df = df.dropna()

# Access the x and y values by index
index = 1  # Replace with the index you want to access
x = df.loc[index, 'x']
y = df.loc[index, 'y']

print(x, y)