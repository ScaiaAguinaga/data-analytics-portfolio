import pandas as pd

df = pd.read_csv("data/raw/netflix_titles.csv")

# print("\nFIRST 5 ROWS:")
# print(df.head())

print("\nINFO:")
print(df.info())

print("\nMISSING VALUES:")
print(df.isnull().sum())

print("\nDUPLICATES:")
print(df.duplicated().sum())

print("NULL Directors:")
print(df['director'].isnull().sum())

print(df['date_added'].value_counts().to_string())