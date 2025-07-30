
# Install packages
!pip install pandas matplotlib scikit-learn --quiet

# Imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import datetime as dt

# Load CSV
df = pd.read_csv("online_retail.csv", encoding='ISO-8859-1")

# Basic exploration
print("Shape:", df.shape)
df.info()
print("Missing values:\n", df.isnull().sum())
