
# Data Cleaning

# Drop rows with missing CustomerID
df = df.dropna(subset=['CustomerID'])

# Remove canceled orders (InvoiceNo starting with 'C')
df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]

# Remove rows with negative or zero quantity and price
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

# Convert InvoiceDate to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Reset index
df.reset_index(drop=True, inplace=True)

# Final shape
print("Cleaned shape:", df.shape)
df.head()
