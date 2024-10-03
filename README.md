# Falcon 9 First Stage Landing Success Prediction

## Overview

This repository contains the capstone project focused on **predicting the success of Falcon 9's first stage landing**. SpaceX's Falcon 9 rocket launches are significantly more economical, costing **$62 million**, compared to other providers that charge upwards of **$165 million** per launch. A key factor in this cost reduction is the reusability of Falcon 9's first stage, making its successful landing critical for operational efficiency.

By predicting whether the first stage will land successfully, we can determine potential launch costs. This insight can also assist other companies in bidding against SpaceX for rocket launches. The project employs a range of data science and machine learning techniques to tackle this real-world business challenge.

## Project Structure

### 1. Data Collection with Web Scraping and Data Wrangling

- **Objective:** Collect and clean data for analysis and model building.
- **Tasks:**
  - Write Python code to manipulate data using **Pandas DataFrames**.
  - Convert JSON files into **Pandas DataFrames**.
  - Load datasets, clean the data, and extract meaningful insights.
  - Utilize RESTful APIs and web scraping techniques to gather data.

### 2. Exploratory Data Analysis (EDA)

- **Objective:** Analyze the data visually to identify key patterns and trends.
- **Tasks:**
  - Create scatter plots and bar charts for data visualization.
  - Perform data wrangling and exploratory analysis using **Pandas**.
  - Execute SQL queries to select and sort relevant data.
  - Visualize data to inform the modeling process.

### 3. Interactive Visual Analytics and Dashboards

- **Objective:** Build interactive dashboards and maps for detailed analysis.
- **Tasks:**
  - Develop interactive dashboards with **Plotly Dash** to analyze launch records.
  - Create pie charts and scatter plots for comprehensive data exploration.
  - Construct interactive maps using **Folium** to assess launch site proximity.
  - Calculate distances on interactive maps and mark clusters.

### 4. Predictive Analysis (Classification)

- **Objective:** Apply machine learning techniques to predict the success of the Falcon 9 first stage landing.
- **Tasks:**
  - Split the dataset into training and test sets.
  - Train various classification models (e.g., SVM, Classification Trees, Logistic Regression).
  - Perform hyperparameter tuning using grid search.
  - Select the best-performing model to aid businesses in making cost-effective decisions.

## Tools and Libraries Used

- **Pandas:** Data manipulation and analysis.
- **NumPy:** Numerical computations.
- **Matplotlib & Seaborn:** Data visualization for EDA.
- **Plotly Dash:** Building interactive dashboards.
- **Folium:** Creating interactive maps.
- **Scikit-Learn:** Machine learning and predictive modeling.
- **BeautifulSoup & Requests:** Web scraping and data extraction.
- **SQL:** Querying and sorting data.

## How to Use

1. **Clone the repository:**
   ```bash
    https://github.com/Kata10/Predicting-Falcon-9-First-Stage-Landing-Success/tree/main
2. **Install the necessary dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Run the Jupyter notebooks to follow the step-by-step analysis, dashboard creation, and predictive modeling.**

4. **Explore the interactive dashboards by running:**
   ```bash
   python dashboard.py

## Conclusion

This project leverages data science methodologies, data visualization, and machine learning techniques to predict the success of Falcon 9's first stage landing. The insights derived from the analysis can help organizations understand launch costs, optimize performance, and enhance decision-making in the space industry.

Feel free to contribute, report issues, or suggest improvements. Thank you for exploring this project!
