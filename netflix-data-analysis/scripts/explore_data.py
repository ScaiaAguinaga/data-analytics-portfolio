import pandas as pd

file_path = "data/raw/netflix_titles.csv"
df = pd.read_csv(file_path)

print("\nDATAFRAME INFO:")
print(df.info())

print("\nMISSING DATA:")
print(df.isna().sum())

invalid_ratings = df[df["rating"].str.contains("min", na=False)]

print(invalid_ratings["rating"])

print(invalid_ratings["rating"].count())