import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_excel("data/Online Retail.xlsx", engine="openpyxl")
    return df

df = load_data()

# Title
st.title("📊 Online Retail Sales Dashboard")

# Display raw data
if st.checkbox("Show Raw Data"):
    st.write(df.head())

# Sales Overview
st.subheader("💰 Total Sales by Country")
sales_by_country = df.groupby("Country")["Quantity"].sum().sort_values(ascending=False)
st.bar_chart(sales_by_country)

# Top Selling Products
st.subheader("🏆 Top 10 Best-Selling Products")
top_products = df.groupby("Description")["Quantity"].sum().nlargest(10)
st.bar_chart(top_products)

# Monthly Sales Trend
st.subheader("📈 Monthly Sales Trend")
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df["Month"] = df["InvoiceDate"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Quantity"].sum()
st.line_chart(monthly_sales)

# Customer Segmentation
st.subheader("🛍️ Customer Purchase Frequency")
customer_purchases = df["CustomerID"].value_counts()

import matplotlib.pyplot as plt

# Create a histogram
customer_purchases = df.groupby("CustomerID")["InvoiceNo"].count()

    # Create the histogram
fig, ax = plt.subplots()
ax.hist(customer_purchases, bins=50, color="blue", edgecolor="black")

    # Set x-axis limit (focus on 0-1000 purchases)
ax.set_xlim(0, 850)

    # Labels & Title
ax.set_title("🛍️ Customer Purchase Frequency")
ax.set_xlabel("Number of Purchases")
ax.set_ylabel("Frequency")

# Display in Streamlit
st.pyplot(fig)


# Conclusion
st.write("🔍 This dashboard provides insights into sales trends, top products, and customer behavior.")

