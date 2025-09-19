# Correlation Heatmap
# -------------------------------
plt.figure(figsize=(10, 8))
sns.heatmap(df_cleaned.drop(columns=['Country name']).corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap of Happiness Factors")
plt.tight_layout()
plt.show()
