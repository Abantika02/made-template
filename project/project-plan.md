# Project Plan

## Title

<!-- Give your project a short title. -->
Analysis of Shooting Incidents

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
1. What are the spatial and temporal patterns of shooting incidents, and can these trends help identify high-risk areas and times for potential future incidents?
2. What are the trends in shooting incidents across different locations and times?
3. How do factors like time, day, or location influence the frequency of shootings?
4. Can we identify hotspots or predict shooting occurrences based on historical data?
5. How do weather conditions (such as temperature, humidity, and precipitation) correlate with the frequency and distribution of shooting incidents across different locations and times, and can certain weather patterns be linked to higher shooting occurrences?


## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
This project aims to explore and analyze patterns in shooting incidents, focusing on spatial and temporal trends.
Using historical shooting data, the project will uncover insights regarding the times and locations most associated
with such incidents. The analysis will involve data cleaning, transformation, and exploratory analysis, followed
by the application of clustering and visualization techniques to identify high-risk areas or peak times for shootings.

The outcome of this project will be a comprehensive understanding of shooting trends, with visualizations to aid in
the identification of critical patterns. The goal is to provide insights that could inform preventive measures and
better resource allocation for law enforcement. Key steps include data preprocessing, feature engineering, clustering,
and the creation of interactive maps or dashboards for visualization.


## Datasources

<!-- Describe each datasource you plan to use in a section. Use the prefix "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Kaggle Shooting Incidents Dataset
* Data URL: https://www.kaggle.com/datasets/ahsen1330/us-police-shootings/data?select=shootings.csv
* Data Type: CSV

This dataset contains records of shooting incidents, including details such as location, date, and time. The dataset
enables analysis of when and where shootings are most frequent, potentially allowing for predictive insights. Key
attributes include:

- **Date**: Date of the shooting incident
- **Location**: Geographic location of the shooting (e.g., city, neighborhood)
- **Time**: Specific time when the incident occurred, useful for temporal analysis
- **Victims/Perpetrators**: Information on those involved, if available

### Datasource2: Kaggle Weather Dataset (United States)
* Data URL: https://www.kaggle.com/datasets/nachiketkamod/weather-dataset-us/data?select=Weather-Data-(US).csv
* Data Type: CSV

This dataset contains records of weather conditions across various U.S. locations. By adding context to shooting incident data, it enables analysis of whether certain weather patterns correlate with the frequency and severity of shootings. Key attributes include:

- **Date**: Date of the weather observation, allowing integration with incident data.
- **Location**: Geographic location of the weather observation (e.g., city, neighborhood).
- **Temperature** : Temperature data, potentially impacting incident frequency.
- **Precipitation and Humidity**: Environmental conditions that may correlate with shooting incidents.
- **Weather Conditions**: Descriptions of weather (e.g., sunny, rainy) that can be analyzed for any patterns related to incident occurrences.


## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Clean the data by handling missing values and ensuring consistent formats for dates and times.
2. Conduct exploratory data analysis (EDA) to understand key patterns in the dataset.
3. Engineer features for analysis, such as incident frequency by location or time period.
4. Apply clustering techniques to identify shooting hotspots.
5. Perform time-based analysis to detect any trends by hour, day, or season.
6. Visualize shooting incident data on a map to highlight high-frequency areas.
7. Document findings in a report with key recommendations for policy makers.
8. (Optional) Develop an interactive dashboard for real-time visualization of shooting data.

