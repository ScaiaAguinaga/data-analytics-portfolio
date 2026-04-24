import pandas as pd

# Reads in CSV file as DF
file_path = "data/raw/netflix_titles.csv"
df = pd.read_csv(file_path)

# Fills missing director and cast values with Unlisted
df = df.fillna(value = {'director': 'Unlisted', 'cast': 'Unlisted'})

# Confirming missing values are no longer missing - TEST ONLY
print("\nMISSING VALUES: ")
missing_values = df.isna().sum().sort_values(ascending=False)
print(missing_values)

# Writes DF to CSV file in outputs folder
df.to_csv("outputs/netflix_titles_output.csv")