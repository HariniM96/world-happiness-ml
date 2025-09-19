# Top & Bottom Countries
# -------------------------------
print("\nTop 10 Happiest Countries:")
print(df_cleaned[['Country name', 'Ladder score']].sort_values(by='Ladder score', ascending=False).head(10))

print("\nBottom 10 Least Happy Countries:")
print(df_cleaned[['Country name', 'Ladder score']].sort_values(by='Ladder score').head(10))
