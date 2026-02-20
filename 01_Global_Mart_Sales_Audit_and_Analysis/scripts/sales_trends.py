import pandas as pd
import matplotlib.pyplot as plt
import os

#1. importing the file path
file_path = os.path.join("..", "cleaned_data", "clean_sales.csv")
df = pd.read_csv(file_path)

#2. convertig the date clumn back to its datetime
df['date'] = pd.to_datetime(df["date"])

#3. creating the new day of th week column
df['date_of_week'] = df["date"].dt.day_name()

#4. analyzing the average spent per day
day_analysis = df.groupby('date_of_week')['amount_spent'].mean().sort_values(ascending=False)
print("--- Weekly Trend Anaysis ---")
print(day_analysis)

#5. visualizing the trend
day_analysis.plot(kind='bar', color='skyblue', edgecolor='black')

#6. adding labels
plt.title("Average Spending by Day of Week")
plt.xlabel("Day of Week")
plt.ylabel("Average Amount Spent ($)")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

#7. showing the chart
plt.show()

