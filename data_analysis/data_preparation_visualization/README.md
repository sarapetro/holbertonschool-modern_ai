# Data Visualization and Preparation

## Description

This project focuses on data exploration, cleaning, preparation, and visualization using Python.

Dataset: `Telco-Customer-Churn.csv`

## Requirements

- Python 3
- Pandas
- NumPy
- Matplotlib

## Tasks

### 0. Data Exploration
- Display dataset shape.
- Check column data types.
- Display the first five rows.
- Count missing values.
- Count duplicate rows.

### 1. Convert Columns
- Convert `TotalCharges` to numeric.
- Convert invalid values to `NaN`.
- Map `SeniorCitizen`:
  - `0` to `"No"`
  - `1` to `"Yes"`

### 2. Clean Total Charges
Handle missing values using three methods:
- `drop`: Remove rows with missing values.
- `median`: Replace missing values with the column median.
- `impute`: Replace missing values with `MonthlyCharges * tenure`.

### 3. Removing Duplicates
Remove duplicate rows from the DataFrame.

### 4. Drop Customer ID
Remove the `customerID` column because unique identifiers do not provide useful predictive information.

### 5. Plot Missingness
Visualize missing values using Matplotlib:
- X-axis represents row indices.
- Y-axis represents column names.
- Missing values are displayed as vertical bars (`|`).

## Libraries Used

- **Pandas:** Data manipulation and cleaning.
- **NumPy:** Finding missing value positions.
- **Matplotlib:** Data visualization.

## Goal

The goal is to prepare and visualize data before applying machine learning techniques.