
# Export clustered RFM table to CSV
rfm.to_csv("clustered_customers.csv", index=False)

# Optional: Download in Colab
from google.colab import files
files.download("clustered_customers.csv")
