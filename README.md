# Shooting Incidents Analysis

This repository contains the entire workflow, data, and analyses for exploring patterns in shooting incidents and their correlation with environmental factors.

## Table of Contents
1. [Overview](#overview)
2. [Project Structure](#project-structure)
3. [How to Run](#how-to-run)
4. [Data Sources](#data-sources)
5. [Future Work](#future-work)

## Overview
This project investigates the temporal, spatial, and environmental patterns of shooting incidents in the United States. By leveraging demographic, geographic, and weather data, the analysis identifies critical insights such as high-risk periods, locations, and the role of weather in influencing incident frequency.

## Project Structure

### `.github/workflows`
- **ci.yml**: Defines the continuous integration pipeline for testing the code.
- **exercise-feedback.yml**: Configures the workflow for providing exercise feedback.

### `data`
- **.gitkeep**: Placeholder for ensuring the `data` directory is versioned.

### `examples`
- **data-exploration-example.ipynb**: Notebook showcasing data exploration techniques.
- **data.sqlite**: Example SQLite database containing structured data for exploration.
- **final-report-example.ipynb**: Template for the final analysis report.
- **project-plan-example.md**: Example of a well-documented project plan.

### `exercises`
- **airports.sqlite, country-stats.sqlite, gtfs.sqlite, temperatures.sqlite, trees.sqlite**: Databases for different data exploration exercises.
- **exercise1.jv - exercise5.jv**: Sample Java files for exercises.
- **.gitkeep**: Ensures the directory remains in version control.

### `project`
#### `EDA`
- **analysis-report.pdf**: Final report documenting the key findings and analysis.
- **data-report.pdf**: Detailed report on the processed datasets.
- **pipeline.py**: Python script automating the ETL process.
- **pipeline.sh**: Shell script for running the pipeline and other automation tasks.
- **project-plan.md**: Project plan outlining objectives, methodology, and milestones.
- **source_info.json**: JSON file with metadata about the sources used.
- **tests.sh**: Bash script for testing data and pipeline functionality.

### Root Files
- **LICENSE**: Licensing details for the repository.
- **README.md**: This documentation file.
- **requirements.txt**: Python dependencies required for the project.

## How to Run
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
