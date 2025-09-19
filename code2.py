print("\nMissing Values:")
print(df.isnull().sum())

# Drop missing values for analysis
df_cleaned = df.dropna()

# Summary Statistics
print("\nSummary Statistics:")
print(df_cleaned.describe())
