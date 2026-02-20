import pandas as pd
import os
#1. importing the data
file_path = os.path.join("..", "cleaned_data", "clean_sales.csv")
df = pd.read_csv(file_path)

#2. filtering for only electornics
electronics_df = df[df['product_category'] == 'ELECTRONICS']
#3. grouping the filtered data by region
regional_electronics = electronics_df.groupby('region')['amount_spent'].sum().sort_values(ascending=False)

#4. results
print("--- ELECTRONICS REVENUE BY REGION ---")
print(regional_electronics)