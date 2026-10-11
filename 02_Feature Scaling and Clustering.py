# Features selected for Clustering
selected_features = [
    'age', 'tenure_months', 'total_purchases', 'avg_order_value_usd', 
    'total_spent_usd', 'days_since_last_purchase', 'return_count', 
    'complaint_count', 'satisfaction_score', 'email_open_rate', 
    'click_through_rate', 'conversion_rate', 'customer_lifetime_value_usd', 
    'customer_acquisition_cost_usd', 'customer_profitability_usd',
    'recency_score', 'frequency_score', 'monetary_score'
]

X = df[selected_features].copy()

# standaradize the features
scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)

# Finding the Optimal Number of Clusters using the Elbow Method
inertia = []
K_range = range(1, 11)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

plt.plot(K_range, inertia, marker='o')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Inertia')
plt.title('Elbow Method For Optimal K')
plt.show()


