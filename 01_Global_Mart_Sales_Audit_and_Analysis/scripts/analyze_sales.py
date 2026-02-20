import pandas as pd
import os

#1. loading the cleaned data
filepath = os.path.join("..", "cleaned_data", "clean_sales.csv")
df = pd.read_csv(filepath)

#2. calculating the total revenue
total_revenue = df['amount_spent'].sum()

#3. grouping by category and calculating total revenue per category
category_revenue = df.groupby('product_category')['amount_spent'].sum().sort_values(ascending=False)

#4. results
print("--- Bussiness Report ---")
print(f'Total Revenue; ${total_revenue:.2f}')
print("\nRevenue by Category:")
print(category_revenue)