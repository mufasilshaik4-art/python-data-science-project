import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------
# SALES DATA ANALYSIS PROJECT
# -----------------------------------

# 1. Create sample sales data
data = {
    "Date": [
        "2026-01-05", "2026-01-12", "2026-01-20",
        "2026-02-03", "2026-02-15", "2026-02-25",
        "2026-03-04", "2026-03-14", "2026-03-28",
        "2026-04-06", "2026-04-18", "2026-04-27",
        "2026-05-08", "2026-05-17", "2026-05-29"
    ],
    "Product": [
        "Laptop", "Mouse", "Keyboard",
        "Laptop", "Headphones", "Mouse",
        "Keyboard", "Laptop", "Headphones",
        "Mouse", "Laptop", "Keyboard",
        "Headphones", "Mouse", "Laptop"
    ],
    "Category": [
        "Electronics", "Accessories", "Accessories",
        "Electronics", "Accessories", "Accessories",
        "Accessories", "Electronics", "Accessories",
        "Accessories", "Electronics", "Accessories",
        "Accessories", "Accessories", "Electronics"
    ],
    "Quantity": [
        2, 10, 7,
        3, 8, 15,
        12, 2, 10,
        20, 4, 15,
        12, 18, 3
    ],
    "Unit_Price": [
        60000, 800, 1500,
        60000, 2500, 800,
        1500, 60000, 2500,
        800, 60000, 1500,
        2500, 800, 60000
    ]
}

# 2. Create DataFrame
df = pd.DataFrame(data)

# 3. Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# 4. Calculate Revenue
df["Revenue"] = df["Quantity"] * df["Unit_Price"]

# 5. Display complete dataset
print("\n========== SALES DATA ==========\n")
print(df)

# 6. Basic information
print("\n========== DATA INFORMATION ==========\n")
print(df.info())

# 7. Total sales
total_revenue = df["Revenue"].sum()
total_quantity = df["Quantity"].sum()

print("\n========== OVERALL RESULTS ==========\n")
print("Total Quantity Sold:", total_quantity)
print("Total Revenue: ₹", f"{total_revenue:,.2f}")

# 8. Product-wise sales
product_sales = (
    df.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== PRODUCT-WISE REVENUE ==========\n")
print(product_sales)

# 9. Find best-selling product
best_product = product_sales.idxmax()
best_product_revenue = product_sales.max()

print("\nBest-Selling Product:", best_product)
print("Revenue:", f"₹{best_product_revenue:,.2f}")

# 10. Category-wise revenue
category_sales = (
    df.groupby("Category")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== CATEGORY-WISE REVENUE ==========\n")
print(category_sales)

# 11. Monthly revenue
df["Month"] = df["Date"].dt.to_period("M")

monthly_sales = (
    df.groupby("Month")["Revenue"]
    .sum()
)

print("\n========== MONTHLY REVENUE ==========\n")
print(monthly_sales)

# 12. Find best month
best_month = monthly_sales.idxmax()
best_month_revenue = monthly_sales.max()

print("\nBest Month:", best_month)
print("Revenue:", f"₹{best_month_revenue:,.2f}")

# 13. Average order revenue
average_revenue = df["Revenue"].mean()

print("\nAverage Revenue per Order:",
      f"₹{average_revenue:,.2f}")

# -----------------------------------
# VISUALIZATION
# -----------------------------------

# 14. Product revenue chart
plt.figure(figsize=(8, 5))

product_sales.plot(kind="bar")

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (₹)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("product_revenue.png")
plt.show()

# 15. Monthly revenue chart
plt.figure(figsize=(8, 5))

monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue (₹)")
plt.grid(True)
plt.tight_layout()

plt.savefig("monthly_revenue.png")
plt.show()

# 16. Category revenue chart
plt.figure(figsize=(7, 5))

category_sales.plot(kind="pie", autopct="%1.1f%%")

plt.title("Revenue Distribution by Category")
plt.ylabel("")
plt.tight_layout()

plt.savefig("category_revenue.png")
plt.show()

# -----------------------------------
# BUSINESS INSIGHTS
# -----------------------------------

print("\n========== BUSINESS INSIGHTS ==========\n")

print("1. The best-selling product is:", best_product)

print("2. The highest revenue month is:",
      str(best_month))

print("3. Total revenue generated is:",
      f"₹{total_revenue:,.2f}")

print("4. Average revenue per order is:",
      f"₹{average_revenue:,.2f}")

print("\n========== PROJECT COMPLETED ==========\n")