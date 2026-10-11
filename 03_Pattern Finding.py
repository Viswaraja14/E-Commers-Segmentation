## Revenue Contribution Analysis
# Check average spending, total purchases, and CLV per cluster
spending_pattern = df.groupby('cluster').agg({
    'customer_id': 'count',
    'total_spent_usd': 'mean',
    'total_purchases': 'mean',
    'customer_lifetime_value_usd': 'mean'
}).rename(columns={'customer_id': 'customer_count'}).reset_index()

print(spending_pattern)

## Channel & Device Preference Across Segments
# See preferred shopping channels by cluster
channel_pattern = pd.crosstab(df['cluster'], df['shopping_channel'], normalize='index') * 100
print("--- Shopping Channel Percentage by Cluster ---")
print(channel_pattern)

# See device preferences by cluster
device_pattern = pd.crosstab(df['cluster'], df['device_used'], normalize='index') * 100
print("\n--- Device Preference Percentage by Cluster ---")
print(device_pattern)

## Churn Risk vs. Satisfaction Score analysis
plt.figure(figsize=(8, 5))
sns.boxplot(x='churn_risk_category', y='satisfaction_score', data=df, palette='Set2')
plt.title('Satisfaction Score Distribution Across Churn Risk Categories')
plt.xlabel('Churn Risk Category')
plt.ylabel('Satisfaction Score')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

