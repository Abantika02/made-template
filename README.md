# Methods of Advanced Data Engineering

This repository contains the entire workflow, data, and analyses for exploring patterns in shooting incidents and their correlation with environmental factors.

# Project Name: Shooting Incidents Analysis: A Data-Driven Exploration

This project explores the patterns, trends, and environmental factors associated with shooting incidents in the United States. The analysis integrates temporal, spatial, and environmental data, leveraging Python-based pipelines and visualizations to uncover actionable insights.

---

## Features

- Exploratory Data Analysis (EDA) for temporal, spatial, and environmental trends.
- Insights into high-risk areas and time periods for shooting incidents.
- Integration of weather data to explore correlations between environmental factors and incidents.
- Automated ETL (Extract, Transform, Load) pipeline for data processing.
- Comprehensive visualizations including heatmaps, scatterplots, and bar charts.

---

## Dataset Details

### Shooting Data
- **Source:** Public datasets of shooting incidents in the United States.
- **Attributes:** Date, time, location, demographics, and more.

### Weather Data
- **Source:** Weather Data U.S. [Global Historical Climatology Network (GHCN)].
- **Attributes:** Temperature, precipitation, and other environmental factors.

For dataset preparation, preprocessing, and license compliance, see the `data` folder and `source_info.json`.

---

## Repository Structure
   ```bash
   shooting_analysis/
   ├── .github/
   │   └── workflows/
   │       ├── ci.yml                     # Continuous Integration workflow
   │       ├── exercise-feedback.yml      # Workflow for automated feedback
   ├── data/
   │   └── .gitkeep                       # Placeholder for dataset folder
   ├── examples/
   │   ├── data-exploration-example.ipynb # Example notebook for data exploration
   │   ├── final-report-example.ipynb     # Example notebook for report generation
   │   ├── project-plan-example.md        # Example project plan
   │   └── data.sqlite                    # Example SQLite database
   ├── exercises/
   │   ├── .gitkeep                       # Placeholder for exercises folder
   │   ├── airports.sqlite                # SQLite database with airport data
   │   ├── country-stats.sqlite           # SQLite database with country statistics
   │   ├── gtfs.sqlite                    # SQLite database with GTFS data
   │   ├── temperatures.sqlite            # SQLite database with temperature data
   │   ├── trees.sqlite                   # SQLite database with tree data
   │   ├── exercise1.jv                   # Java exercise file 1
   │   ├── exercise2.jv                   # Java exercise file 2
   │   ├── exercise3.jv                   # Java exercise file 3
   │   ├── exercise4.jv                   # Java exercise file 4
   │   └── exercise5.jv                   # Java exercise file 5
   ├── project/
   │   ├── EDA/
   │   │   ├── analysis.ipynb             # Detailed EDA
   │   ├── pipeline.py                    # Python script for ETL pipeline
   │   ├── pipeline.sh                    # Shell script to execute the ETL pipeline
   │   ├── project-plan.md                # Detailed project plan document
   |   |── data-report.pdf                # Detailed report on the processed datasets.
   |   |── analysis-report.pdf            # Detailed analysis report
   │   ├── source_info.json               # Metadata about data sources
   |   |── slides.pdf                     # Final presentation of this project
   |   |── presentation-video.md          # Contains presentation video link for reference
   │   └── tests.sh                       # Shell script for running tests
   ├── LICENSE                            # License information for the project
   ├── README.md                          # Documentation for the project
   ├── requirements.txt                   # List of Python dependencies
   └── .gitignore                         # Rules for files to ignore in version 
   ```


## Repo Details

### `.github/workflows`
- **ci.yml**: Defines the continuous integration pipeline for testing the code.
- **exercise-feedback.yml**: Configures the workflow for providing exercise feedback.

### `data`
- **.gitkeep**: Placeholder for ensuring the `data` directory is versioned.

### `exercises`
- **airports.sqlite, country-stats.sqlite, gtfs.sqlite, temperatures.sqlite, trees.sqlite**: Databases from different exercises.
- **exercise1.jv - exercise5.jv**: Sample Jayvee files for exercises.
- **.gitkeep**: Ensures the directory remains in version control.

### `project`
- **analysis-report.pdf**: Final report documenting the key findings and analysis.
- **data-report.pdf**: Detailed report on the processed datasets.
- **pipeline.py**: Python script automating the ETL process.
- **pipeline.sh**: Shell script for running the pipeline.
- **project-plan.md**: Project plan outlining objectives, methodology, and milestones.
- **source_info.json**: JSON file with metadata about the sources used.
- **tests.sh**: Bash script for testing data and pipeline functionality.
- **slides.pdf**: Final presentation of this project
-**presentation-video.md**: Contains presentation video link for reference.
#### `EDA`
-**analysis.ipynb**: Exploratory Data Analysis of cleaned, preprocessed data which are in `data` folder.

### Root Files
- **LICENSE**: Licensing details for the repository.
- **README.md**: This documentation file.
- **requirements.txt**: Python dependencies required for the project.

---

## Installation

### Prerequisites
- Python 3.12
- Required libraries (see `requirements.txt`)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Abantika02/made-template.git
   cd made-template

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Run the pipeline
   to execute the data ETL pipeline and perform analysis:
   ```bash 
   python project/pipeline.py

4. Or, use the shell script to automate:
   ```bash 
   bash project/pipeline.sh

5. Test the Pipeline
   Run the provided test suite to ensure the integrity of the pipeline:
   ```bash
   bash project/tests.sh

---

## Key Insights

### Temporal Patterns
- Shooting incidents peak during summer months and weekends.

### Spatial Trends
- Hotspots include California, Texas, and urban centers like Los Angeles and Houston.

### Environmental Factors
- Higher temperatures increase shootings, while rainy days show a slight decrease.

For detailed analysis, see the `analysis-report.pdf` in the `project` folder.

---

## Future Work

- **Granular Analysis**: Enhance spatial analysis to explore neighborhood-level trends.
- **Weather Integration**: Build predictive models leveraging weather patterns.
- **Policy Recommendations**: Formulate actionable strategies for policymakers.

---

## References

- **Shooting Data**: [Public Dataset Sources](https://www.kaggle.com/datasets/ahsen1330/us-police-shootings)
- **Weather Data**: [Public Dataset Sources](https://www.kaggle.com/datasets/nachiketkamod/weather-dataset-us)

---

## License

This project is licensed under the C0-1.0 license. See the `LICENSE` file for details.




