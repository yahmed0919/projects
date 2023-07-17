# By Yaseen A.
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Load and preprocess customer data
customer_data = pd.read_csv('customer_data.csv')
features = customer_data[['Purchases', 'Age', 'Income']]
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Perform K-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(scaled_features)

# Add cluster labels to customer data
customer_data['Cluster'] = kmeans.labels_

# Analyze and present the results
cluster_means = customer_data.groupby('Cluster').mean()
print(cluster_means)
