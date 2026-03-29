# Vendor Performance Analysis

## 📌 Project Overview
This project focuses on analyzing vendor performance using sales transaction data. The main objective is to evaluate vendor efficiency, identify potential issues in pricing and inventory management, and provide actionable insights to improve overall profitability and operational performance.

The analysis includes data ingestion from a SQLite database, thorough data cleaning, exploratory data analysis (EDA), statistical insights, correlation analysis, and business recommendations.

## 📂 Project Structure
````plaintext
vendor_performance/
├── Cleaning.ipynb
├── Explanatory.ipynb
├── Vendor Performance Analysis.ipynb
├── get_vendor_summary.py
├── ingestion_db.py
├── logs/
│   ├── get_vendor_summary.log
│   └── ingestion_db.log
├── README.md
└── .gitignore
````

🛠️ Technologies Used

- Programming Language: Python 3
- Data Analysis: Pandas, NumPy, SciPy
- Visualization: Matplotlib, Seaborn
- Environment: Jupyter Notebook
- Database: SQLite

✨ Key Features

- Automated data ingestion and preprocessing from SQLite database
- Comprehensive data cleaning and handling of negative/outlier values
- In-depth Exploratory Data Analysis (EDA)
- Correlation analysis and outlier detection
- Evaluation of bulk pricing strategy effectiveness
- Analysis of slow-moving inventory and its impact on holding costs
- Actionable business insights and recommendations for vendor management

🚀 How to Run the Project

- Clone the repository: 
```bash
git clone https://github.com/hachi4205/vendor_performance.git
cd vendor_performance
```
- Install the required packages:
```bash
pip install pandas numpy matplotlib seaborn scipy
```
- Open Jupyter Notebook and run the notebooks in the following order:
```bash
Cleaning.ipynb
Exploratory Data Analysis.ipynb
Vendor Performance Analysis.ipynb
```

📊 Key Insights

- Detected negative values and outliers in important financial metrics
- Analyzed relationships between purchase price, sales volume, and profitability
- Evaluated the benefits and impact of bulk purchasing strategy
- Identified the risks and costs associated with slow-moving inventory
- Provided recommendations for promotional activities and pricing adjustments on selected brands/vendors
