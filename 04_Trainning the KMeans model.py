# train the KMeans model with the optimal numbers of clusters
# Adjust based on your elbow graph
optimal_k = 4  
kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
df['cluster'] = kmeans.fit_predict(X_scaled)

# Grouping the original DataFrame bu the new cluster column to see what makes each segment unique
cluster_summary = df.groupby('cluster')[['total_spent_usd', 'total_purchases', 'days_since_last_purchase', 'customer_lifetime_value_usd', 'satisfaction_score']].mean()
print(cluster_summary)

# Transulate the cluster summery into more readable format
cluster_names = {
    0: 'Regular Shoppers',
    1: 'VIP Champions',
    2: 'Loyal Spenders',
    3: 'At-Risk / Churned'
}
df['segment_name'] = df['cluster'].map(cluster_names)

from sklearn.decomposition import PCA

### Visualization of Clusters(Dimensionality Reduction)
# Reduce to 2 components
pca = PCA(n_components=2)
components = pca.fit_transform(X_scaled)

df['pca_x'] = components[:, 0]
df['pca_y'] = components[:, 1]

# Plot the clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df, x='pca_x', y='pca_y', hue='segment_name', 
    palette='Set1', alpha=0.8, s=50
)
plt.title('Customer Segments Visualized via PCA')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.legend(title='Segments')
plt.show()
