#!/usr/bin/env python
# coding: utf-8

# # SWIGGY SALES ANALYSIS
# 

# ## IMPORT THE REQUIRED LIBRARIES
# 

# In[37]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# Importing the Dataset

# In[38]:


df = pd.read_excel(r"C:\Users\mehar\Downloads\swiggy_data.xlsx")


# In[41]:


print(df)


# In[4]:


df.head() #gives the first 5 rows by default


# In[5]:


df.tail() #gives the last 5 rows by default


# # Metadata of data

# In[6]:


df.shape[0] #gives the number of rows in the data


# In[7]:


df.shape[1] #gives the number of columns


# In[8]:


print("No of Rows:", df.shape[0])


# In[9]:


print("No of columns:" , df.shape[1])


# In[10]:


df.info


# In[11]:


df.info()


# ## DATA TYPE
# 

# In[12]:


df.dtypes


# In[13]:


#kpi- key perfomance indicators- tells us how the business is doing
#tells us where the business is heading


# In[14]:


df.describe()


# ### KPI's

# ### Total Sales

# In[15]:


total_sales = df["Price (INR)"].sum()
print("Total Sales (INR):", round(total_sales,2))


# ### Average Rating

# In[16]:


average_rating = df["Rating"].mean()
print("Average Rating:", round(average_rating,1))


# ### Average Order Value

# In[17]:


average_order_value = df["Price (INR)"].mean()
print("Average Order Value:", round(average_order_value,2))


# ### Ratings Count

# In[18]:


ratings_count = df["Rating Count"].sum()
print("Ratings Count:", round(ratings_count,2))


# ### Total Orders

# In[19]:


#number of food order received


# In[20]:


#use a count fn- goves total count of a variable (excluding missing values)
total_orders = df["Dish Name"].count()
print("Total Number of Orders:", round(total_orders,2))


# In[21]:


#use basically any columnm and find its count


# ### OR

# In[22]:


#use a len function- gives the total number of rows in a column 
#(includes missing values)


# In[23]:


total_orders = len(df)
print("Total Orders:", total_orders)


# # DATA VISUALIZATION

# ## MONTHLY SALES TREND

# In[24]:


#converts the "Order Date" column into proper date-time format.
df["Order Date"] = pd.to_datetime(df["Order Date"])
#here, to_datetime is the command to change into proper date-time format

#converting the 
df["YearMonth"]= df["Order Date"].dt.to_period("M").astype(str)

monthly_revenue = df.groupby("YearMonth")["Price (INR)"].sum().reset_index()

plt.figure()
plt.plot(monthly_revenue["YearMonth"], monthly_revenue["Price (INR)"])
plt.xticks(rotation=45)
plt.xlabel("Month")
plt.ylabel("Total Sales (INR)")
plt.title("Monthly Sales Trend")
plt.tight_layout()
plt.show()
 


# ### Daily Sales Trend

# In[25]:


#converts the "Order Date" column into proper date-time format.
df["DayName"] = pd.to_datetime(df["Order Date"]).dt.day_name()


daily_revenue =(df.groupby("DayName")["Price (INR)"]).sum().reindex(["Monday", "Tuesday","Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

plt.figure(figsize=(10,5))
plt.bar(daily_revenue.index, daily_revenue.values, color="blue")
plt.title("Daily Revenue Trend (Mon-Sun)")
plt.xlabel("Day")
plt.ylabel("Revenue (INR)")
plt.xticks(rotation=30)

plt.show()




# ## Total sales by Food Type (Veg vs Non Veg)

# In[26]:


#we dont have separated dish by veg and non veg
#we have to identify them manually.

non_veg_keywords= ["chicken", "egg", "fish", "mutton", "prawn", 
                   "biryani", "kabab", "kebab", "non-veg", "non veg"] 

 
df["Food Category"]= np.where(
  df["Dish Name"].str.lower().str.contains("|".join(non_veg_keywords), na=False),
    "Non-Veg",
    "Veg"
)


# In[27]:


food_revenue= (
      df.groupby("Food Category")["Price (INR)"].sum().reset_index()
    )


# In[28]:


fig=px.pie(
     food_revenue,
    values="Price (INR)",
    names= "Food Category",
    hole=0.5,
    title="Revenue Contribution: Veg vs Non-Veg"
    )

fig.update_traces(
  textinfo="percent+label",
    pull=[0.05,0]
)

fig.update_layout(
     height= 500,
    margin=dict(t=60, b=40, l=40, r=40)

)
fig.show()


# ## Total Sales by State
# 

# In[29]:


#VISUALISATION USING MATPLOTLIB LIBRARY


# In[30]:


total_sales_bystate =(df.groupby("State")["Price (INR)"].sum().sort_values(ascending=False))
plt.figure(figsize=(10,5))
plt.bar(total_sales_bystate.index, total_sales_bystate.values, color="blue")
plt.title("Total Sales (by state)")
plt.xlabel("States")
plt.ylabel("Price (INR)")
plt.xticks(rotation=90)

plt.show()


# In[31]:


#VISUALISATION USING PLOTLY EXPRESS LIBRARY


# In[32]:


#Horizontal bars 
fig= px.bar(
    df.groupby("State")["Price (INR)"].sum().sort_values(ascending=False).reset_index(),
     x="Price (INR)",
     y= "State",
    orientation="h",
    title="Revenue by State (INR)")

fig.update_layout(height=600, yaxis=dict(autorange="reversed"))
fig.show()


# In[33]:


#straight vertical bars 
fig= px.bar(
    df.groupby("State")["Price (INR)"].sum().sort_values(ascending=False).reset_index(),
     y="Price (INR)",
     x= "State",
    title="Revenue by State (INR)")

fig.update_layout(height=600, yaxis=dict())
fig.show()


# ## QUATERLY PERFOMANCE SUMMARY

# In[34]:


df["Order_Date"] = pd.to_datetime(df["Order Date"])
df["Quarter"] = df["Order_Date"].dt.to_period("Q").astype(str)

quaterly_summary=(
    df.groupby("Quarter").agg(
    Total_sales=("Price (INR)", "sum"),
    Avg_Rating=("Rating", "mean"),
    Total_orders=("Order_Date", "count")
          ).sort_values("Quarter")
)
quaterly_summary["Total_sales"] = quaterly_summary["Total_sales"].round(0)
quaterly_summary["Avg_Rating"] = quaterly_summary["Avg_Rating"].round(2)

quaterly_summary


# ## Top 5 cities by sales

# In[35]:


top_5_cities = (
  df.groupby("City")["Price (INR)"]
    .sum()
    .nlargest(5)
    .sort_values(ascending=False)
    .reset_index()
)

fig= px.bar(
  top_5_cities,
    y="Price (INR)",
    x= "City",
    orientation= "v",
    title= "Top 5 cities by Sales (INR)",
    
)
fig.show()


# ## Weekly Trend Analysis

# In[36]:


df["Order_Date"] = pd.to_datetime(df["Order Date"])
df["Week"] = df["Order_Date"].dt.to_period("W").astype(str)

weekly_sales=(
    df.groupby("Week")["Price (INR)"].sum().reset_index()
)
#Plot
fig=px.bar(
    weekly_sales, 
    x="Week",
    y="Price (INR)",
    title="Weekly Sales Trend (INR)"
)
fig.show()

