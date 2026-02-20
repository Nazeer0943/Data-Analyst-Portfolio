# Project 1: Global-Mart Sales Data Audit & Analysis

## 📌 Project Overview
The goal of this project was to take a highly inconsistent, "messy" retail dataset and transform it into a clean, actionable business report.

## 🛠️ Skills Demonstrated
- **Data Cleaning:** Handled missing values (NaN), inconsistent date formats, and case-sensitivity issues using Python & Pandas.
- **Data Integrity:** Standardized regional and category data to ensure accurate grouping.
- **Analysis:** Extracted business KPIs including Total Revenue and Category Performance.

## 📊 Key Business Insights
- **Total Revenue:** $2,326.50
- **Top Performer:** ELECTRONICS ($1,951.25)
- **Growth Opportunity:** Groceries represent the smallest share of revenue at $75.25.

## 📁 Repository Structure
- `raw_data/`: Original inconsistent CSV.
- `cleaned_data/`: The finalized, audit-ready CSV.
- `scripts/`: Python scripts for cleaning and analysis.

## 📈 Final Analysis Results

### 1. Sales Trends (Time-Series)
- **High Volume Days:** Tuesday and Sunday ($500.00 avg).
- **Low Volume Days:** Saturday ($37.63 avg).
- **Insight:** Higher-value items are purchased during the week and on Sundays, while Saturdays are dominated by small-ticket "basket" items.

### 2. Regional Deep-Dive (Electronics)
- **Top Region:** NORTH ($1,300.00).
- **Weakest Region:** EAST ($0.00).
- **Recommendation:** Reallocate Electronics marketing budget from the East to the North to capitalize on existing demand, or investigate why the East has zero sales in this category.

## 🚀 Technical Summary
- **Tools:** Python, Pandas, Matplotlib, OS, Virtual Environments.
- **Techniques:** Boolean Filtering, Multi-Column Grouping, Feature Engineering (Date extraction), Data Visualization.