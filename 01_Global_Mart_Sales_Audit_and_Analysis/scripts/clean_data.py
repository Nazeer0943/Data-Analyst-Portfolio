import pandas as pd
import os

# 1. Path Setup
file_path = os.path.join("..", "raw_data", "raw_sales_data.csv")
output_path = os.path.join("..", "cleaned_data", "clean_sales.csv")

# 2. Load Data
df = pd.read_csv(file_path)

# 3. Cleaning Operations
# Convert money to numbers and fill holes with 0
df['amount_spent'] = pd.to_numeric(df['amount_spent'], errors="coerce").fillna(0)


# Fix capitalization and remove spaces for BOTH columns
df['region'] = df['region'].str.strip().str.upper()
df['product_category'] = df['product_category'].str.strip().str.upper()
# Fix dates using 'mixed' format to capture those inconsistent rows
df['date'] = pd.to_datetime(df['date'], dayfirst=True, errors='coerce', format='mixed')

# IMPORTANT: If any NaTs remain, we fill them with a placeholder date or drop them
# For this project, let's just see them for now
# df = df.dropna(subset=['date']) # Professional tip: This would remove rows with broken dates

# 4. Final Verification
print('\n--- FINAL CLEANED DATA INFO ---')
print(df.info())
print("\nFirst 5 rows of standardized dates:")
print(df['date'].head())

# 5. Export
df.to_csv(output_path, index=False)
print("\n--- SUCCESS: File saved to cleaned_data folder ---")