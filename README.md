Climate Data Visualization 🌦️📊

This Python project focuses on analyzing and visualizing climate data — including temperature and rainfall patterns — across different stations over various months. The goal is to better understand seasonal trends, station-wise comparisons, and distributions through interactive plots.

📁 Dataset

The dataset used is a CSV file containing:

Station Name

Month

Period

Number of Years

Mean Maximum Temperature (°C)

Mean Minimum Temperature (°C)

Mean Rainfall (mm)

Note: Make sure the CSV file is correctly placed or update the file path accordingly before running the scripts.

🛠 Libraries Used

Pandas

NumPy

Matplotlib

Seaborn

📈 Visualizations Included

Line Plot - Monthly Temperature Trends for a selected station.

Bar Plot - Monthly Rainfall for a selected station.

Heatmap - Average Maximum Temperature across stations per month.

Boxplot - Distribution of Maximum Temperatures by station.

Scatter Plot - Relationship between Min and Max Temperatures.

Histogram - Rainfall distribution across all records.

Violin Plot - Monthly Minimum Temperature distribution.

Pairplot - Pairwise relationships among Max Temp, Min Temp, and Rainfall.

Comparison Line Plot - Rainfall trends for top 3 stations.

Grouped Bar Chart - Average Max & Min Temperatures for top 5 stations.

🧩 Features

Clean preprocessing of months for accurate plotting.

Dynamic selection of stations for comparison.

Intuitive visualizations with labeled axes, legends, and clean layouts.

Sampling large datasets for better performance in pairplots.

A variety of plot types for deeper insights.

🚀 How to Run

Clone this repository.

Install the required libraries if you haven't:

bash
Copy
Edit
pip install pandas matplotlib seaborn numpy
Make sure your CSV dataset path is correct.

Run the Python script in your preferred environment (VS Code, Jupyter Notebook, etc.).

🔥 Preview

(You can optionally add some screenshots of your best plots here.)

💬 Future Improvements

Adding interactive visualizations using Plotly.

Creating a dashboard view using Streamlit.

Automating station-wise reports generation.
