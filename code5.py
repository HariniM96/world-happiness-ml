# K-Means Clustering
# -------------------------------
features = df_cleaned[['Explained by: Log GDP per capita',
                       'Explained by: Social support',
                       'Explained by: Healthy life expectancy',
                       'Explained by: Freedom to make life choices',
                       'Explained by: Generosity',
                       'Explained by: Perceptions of corruption']]

# Scale features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Apply KMeans clustering (3 clusters)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df_cleaned['Cluster'] = kmeans.fit_predict(scaled_features)

print("\nClustering Results (Sample):")
print(df_cleaned[['Country name', 'Ladder score', 'Cluster']].head(20))
