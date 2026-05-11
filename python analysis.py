import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv('superstore_cleaned.csv')

# Make all charts look clean and professional
sns.set_theme(style='whitegrid')

print("Creating charts... please wait!")

# ── Chart 1: Sales by Category ───────────────────────────────────────
category_sales = df.groupby('Category')['Sales'].sum().reset_index()
category_sales = category_sales.sort_values('Sales', ascending=False)

plt.figure(figsize=(8, 5))
sns.barplot(data=category_sales, x='Category', y='Sales', palette='Blues_d')
plt.title('Total Sales by Category', fontsize=14, fontweight='bold')
plt.ylabel('Total Sales (USD)')
plt.xlabel('Product Category')
plt.tight_layout()
plt.savefig('chart1_category_sales.png')
plt.show()
print("Chart 1 saved!")

# ── Chart 2: Monthly Sales Trend ─────────────────────────────────────
df['Order Date'] = pd.to_datetime(df['Order Date'])
monthly = df.groupby(df['Order Date'].dt.to_period('M'))['Sales'].sum()
monthly.index = monthly.index.to_timestamp()

plt.figure(figsize=(12, 5))
plt.plot(monthly.index, monthly.values, marker='o',
         color='steelblue', linewidth=2)
plt.title('Monthly Sales Trend', fontsize=14, fontweight='bold')
plt.ylabel('Sales (USD)')
plt.xlabel('Month')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('chart2_monthly_trend.png')
plt.show()
print("Chart 2 saved!")

# ── Chart 3: Sales by Region ─────────────────────────────────────────
region_sales = df.groupby('Region')['Sales'].sum()

plt.figure(figsize=(7, 7))
colors = ['#4A90D9', '#7BC8A4', '#F5A623', '#E05C5C']
plt.pie(region_sales.values, labels=region_sales.index,
        autopct='%1.1f%%', startangle=140, colors=colors)
plt.title('Sales by Region', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('chart3_region_pie.png')
plt.show()
print("Chart 3 saved!")

# ── Chart 4: Top 10 Products ──────────────────────────────────────────
top10 = df.groupby('Product Name')['Sales'].sum().nlargest(10).reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(data=top10, x='Sales', y='Product Name', palette='Greens_d')
plt.title('Top 10 Products by Sales', fontsize=14, fontweight='bold')
plt.xlabel('Total Sales (USD)')
plt.ylabel('')
plt.tight_layout()
plt.savefig('chart4_top_products.png')
plt.show()
print("Chart 4 saved!")

# ── Chart 5: Profit vs Sales Scatter ─────────────────────────────────
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Sales', y='Profit',
                hue='Category', alpha=0.5, palette='Set2')
plt.title('Profit vs Sales by Category', fontsize=14, fontweight='bold')
plt.xlabel('Sales (USD)')
plt.ylabel('Profit (USD)')
plt.tight_layout()
plt.savefig('chart5_profit_scatter.png')
plt.show()
print("Chart 5 saved!")

print("\n All 5 charts created and saved in your folder!")