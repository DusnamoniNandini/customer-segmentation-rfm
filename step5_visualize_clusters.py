
import matplotlib.pyplot as plt
import seaborn as sns

# Recency vs Frequency
plt.figure(figsize=(8, 5))
sns.scatterplot(data=rfm, x='Recency', y='Frequency', hue='Cluster', palette='tab10', s=100)
plt.title("Customer Segments: Recency vs Frequency")
plt.xlabel("Recency (days)")
plt.ylabel("Frequency (orders)")
plt.legend(title='Cluster')
plt.grid(True)
plt.show()

# Monetary vs Frequency
plt.figure(figsize=(8, 5))
sns.scatterplot(data=rfm, x='Monetary', y='Frequency', hue='Cluster', palette='Set2', s=100)
plt.title("Customer Segments: Monetary vs Frequency")
plt.xlabel("Monetary Value")
plt.ylabel("Frequency (orders)")
plt.legend(title='Cluster')
plt.grid(True)
plt.show()
