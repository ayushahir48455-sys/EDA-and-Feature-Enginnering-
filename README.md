# EDA and Machine Learning Project

This project contains practical work on **Exploratory Data Analysis (EDA), Data Cleaning, Data Preprocessing, Feature Engineering, Data Visualization, and Machine Learning** using Python.

The project uses different datasets to understand how raw data can be cleaned, analyzed, visualized, and prepared for machine learning models.

## 📌 Project Overview

In this project, I worked on:

- Data loading and inspection
- Missing value detection and handling
- Data type conversion
- Data cleaning
- Outlier detection using IQR
- Outlier handling using median
- Z-score calculation
- Data visualization
- Correlation analysis
- Feature engineering
- Encoding categorical variables
- Standardization
- Train-test splitting
- Linear Regression
- Model prediction
- R² and Adjusted R² evaluation

---

## 🛠️ Technologies and Libraries

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

---

## 📊 Part 1: Exploratory Data Analysis

The first dataset is used for practicing data cleaning and exploratory data analysis.

### Data Cleaning

The following operations were performed:

- Checked missing values
- Calculated percentage of missing values
- Converted phone numbers into numeric format
- Filled missing phone values using the median
- Standardized gender values
- Filled missing join dates using forward fill
- Replaced missing emails with `"not provided"`
- Filled missing city values using the mode
- Filled missing salary values using the median
- Converted age values into numeric format

### Outlier Detection

Outliers in the `Age` column were detected using the **IQR (Interquartile Range) method**.

The project calculates:

- Q1
- Q3
- IQR
- Lower Limit
- Upper Limit

Outliers are then replaced with the median age.

Z-score was also calculated for the `Age` column.

---

## 📈 Data Visualization

Different visualization techniques were used to understand the data.

### Visualizations included:

- Pie Chart
- Box Plot
- Bar Plot
- Histogram
- Distribution Plot
- Correlation Heatmap
- Line Plot
- Scatter Plot

Some analysis performed includes:

- Rating distribution
- Age distribution
- Salary growth according to experience
- Average salary by state
- Salary distribution by country
- Age vs Salary relationship
- Correlation between numerical variables

---

## 🔧 Part 2: Feature Engineering

A second dataset, `Project_1.csv`, was used for feature engineering and machine learning.

The dataset contains features such as:

- Year
- Model
- Transmission
- Mileage
- Fuel Type
- Tax
- MPG
- Engine Size
- Price

The `price` column is used as the target variable.

---

## 🔢 Categorical Encoding

Categorical variables were converted into numerical values using:

### One-Hot Encoding

`pd.get_dummies()` was used for:

- Model
- Transmission
- Fuel Type

### Label Encoding

`LabelEncoder` was also explored for converting categorical values into numerical labels.

---

## 📏 Feature Scaling

`StandardScaler` from Scikit-learn was used to standardize numerical features.

The numerical columns include:

- Year
- Mileage
- Tax
- MPG
- Engine Size

---

## 🤖 Machine Learning Model

A **Linear Regression** model was implemented using Scikit-learn.

### Steps:

1. Separate features and target
2. Encode categorical variables
3. Scale numerical features
4. Split the data into training and testing sets
5. Train the Linear Regression model
6. Make predictions
7. Evaluate the model

The dataset was divided using:

```python
train_test_split(
    x_encode,
    y,
    test_size=0.33,
    random_state=42
)
