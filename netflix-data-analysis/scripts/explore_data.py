import pandas as pd

file_path = "data/raw/netflix_titles.csv"
df = pd.read_csv(file_path)

# Displays shape of dataframe
print("\n=== OVERVIEW ===")
print(f"Shape: {df.shape}")

# Displays column tags
print("\nCOLUMNS: ")
print(df.columns.tolist())

# Displays first few rows for visual understanding
print("\nFIRST 5 ROWS: ")
print(df.head())

# Displays column information
print("\nDATAFRAME INFO: ")
df.info()

# Displays subtotal of missing entries per column
print("\nMISSING VALUES: ")
missing_values = df.isna().sum().sort_values(ascending=False)
print(missing_values)

# Displays missing entries in percent format
print("\nMISSING VALUES: ")
missing_percent = round((df.isna().sum() / len(df) * 100), 2)
print(f"{missing_percent.sort_values(ascending=False).astype(str) + '%'}")

# Displays count of duplicate rows
print("\nDUPLICATES: ")
print(df.duplicated().sum())

# Displays descriptive statistics
# Not very useful in this case since most data is string based
# print("\nDESCRIPTION: ")
# print(df.describe(include="all"))

# Displays all unique valus with associated counts
print("\nUNIQUE VALUE CHECKS:")
columns_to_check = ["type", "country", "rating"]

for col in columns_to_check:
  print(f"\nColumn: {col}")
  # For investigating entire list of unique entries
  # print(df[col].unique().tolist())
  print(df[col].value_counts(dropna=False).head(10))