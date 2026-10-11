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
