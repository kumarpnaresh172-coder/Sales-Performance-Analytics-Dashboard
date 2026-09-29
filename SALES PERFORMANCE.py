import pandas as pd

data = {
    "Product": ["Laptop", "Mobile", "Tablet", "Laptop", "Mobile"],
    "Region": ["North", "South", "East", "West", "North"],
    "Sales": [50000, 30000, 20000, 60000, 40000]
}

df = pd.DataFrame(data)

total_sales = df["Sales"].sum()

print("SALES PERFORMANCE ANALYTICS DASHBOARD")
print("--------------------------------------")

print("\nSales Data:")
print(df)

print("\nTotal Sales:", total_sales)

print("\nProduct-wise Sales:")
print(df.groupby("Product")["Sales"].sum())

print("\nRegion-wise Sales:")
print(df.groupby("Region")["Sales"].sum())

print("\nHighest Sale:")
print(df.loc[df["Sales"].idxmax()])
