# Swiggy Sales Data Analysis

An exploratory data analysis (EDA) project on 197,430+ Swiggy food delivery 
orders across Indian states, uncovering revenue trends, geographic performance, 
dish-level insights, and customer preferences using Python and interactive 
Plotly dashboards.



## Features

- Analysis of 197,430+ real Swiggy food delivery records across India
- Monthly and daily sales trend visualizations
- State-wise and city-wise revenue breakdown
- Category and dish-level performance analysis
- Customer rating distribution and sentiment patterns
- Interactive Plotly charts for dynamic data exploration
- Key business metrics: Total Revenue ₹5.3Cr+, Avg Order Value ₹268.51, Avg Rating 4.3


## Tech Stack

**Language:** Python 3

**Libraries:**
- pandas — data loading, cleaning, and transformation
- numpy — numerical operations
- matplotlib — static visualizations
- seaborn — statistical plots
- plotly.express — interactive dashboards and charts

## Requirements
pandas
numpy
matplotlib
seaborn
plotly
openpyxl
## Installation

Clone the repository

  git clone https://github.com/your-username/swiggy-sales-data-analysis.git
  cd swiggy-sales-data-analysis

Create a virtual environment (optional but recommended)

  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies

  pip install -r requirements.txt
    
## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  npm install
```

Start the server

```bash
  npm run start
```



## Usage/Examples

python
import pandas as pd
import plotly.express as px

df = pd.read_excel("swiggy_data.xlsx")

# Total revenue
print("Total Sales (INR):", df["Price (INR)"].sum().round(2))
# Output: 53,012,505.77

# Top states by revenue
state_revenue = df.groupby("State")["Price (INR)"].sum().sort_values(ascending=False)

# Interactive bar chart
fig = px.bar(state_revenue.reset_index(), x="State", y="Price (INR)",
             title="Revenue by State")
fig.show()


## Lessons Learned
- Handling large real-world datasets (197K+ rows) efficiently using pandas
- Parsing and feature engineering on datetime columns (monthly/daily trends)
- Choosing the right chart type for different analytical questions
- Building interactive visualizations with Plotly for exploratory analysis
- Drawing actionable business insights from raw transactional data
## Acknowledgements

 - Dataset sourced from [Kaggle]
- Inspired by real-world business analytics workflows in the food-tech sector
- Built as part of a data science portfolio to demonstrate EDA and 
  visualization skills
DME.md…]()
<img width="454" height="290" alt="Monthly Sales" src="https://github.com/user-attachments/assets/e33b0af0-1585-4f0b-bd42-afe50c257928" />
<img width="638" height="360" alt="Daily Revenue Sales Trend" src="https://github.com/user-attachments/assets/8b8ba1c8-d6a2-4cd5-a554-44f89a56bf25" />
<img width="866" height="482" alt="Revenue Contribution- Veg vs Non-Veg" src="https://github.com/user-attachments/assets/3a65f4bc-06d2-4c86-944f-a8829139565c" />
<img width="635" height="418" alt="Total Sales by state" src="https://github.com/user-attachments/assets/06cd50c5-7912-4319-9794-0f169ca7fa54" />
<img width="1366" height="538" alt="Revenue by State (INR)" src="https://github.com/user-attachments/assets/436c645c-8624-45d0-b9cb-16d00e9397ea" />
<img width="1341" height="582" alt="Revenue By State " src="https://github.com/user-attachments/assets/6437ec7a-be4e-4031-866e-31adf84c1dc0" />
<img width="1345" height="487" alt="Top 5 cities by Sales" src="https://github.com/user-attachments/assets/080c338f-0b7b-4616-809d-9bf536f114bd" />
<img width="1394" height="496" alt="Weekly Trend Analysis" src="https://github.com/user-attachments/assets/c498a2f0-603f-4543-9caa-a61f1fa64494" />
