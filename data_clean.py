import pandas as pd

# Import the data into a DataFrame
df = pd.read_csv('soccer_file.csv')

# Modify the DataFrame
df = df.iloc[:, 1:24]

# Save the modified DataFrame to a new CSV file
df.to_csv('updated_file.csv', index=False)

print(">>> 'updated_file.csv' created")
