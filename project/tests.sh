#!/bin/bash
# Script Name: tests.sh
# Description: This script performs automated tests to ensure the integrity and validity of the data pipeline outputs for the project. It checks for the existence of required output files and validates data within the database.
# Usage: Run this script from the project root directory with 'bash tests.sh'.
# Prerequisites: Python 3.12.0, SQLite3 installed.

# Set paths for input data and output database
DB_FILE="/Users/LENOVO1/made-template/data/processed_data.db"
CSV_SHOOTING_INPUT="/Users/LENOVO1/made-template/data/shootings.csv"
CSV_WEATHER_INPUT="/Users/LENOVO1/made-template/data/Weather Data (US).csv"

# Run the pipeline
echo "Loading and executing pipeline.py"
python pipeline.py

# Validate the pipeline execution success
if [ $? -ne 0 ]; then
    echo "Failed to execute pipeline.py"
    exit 1
fi

# Validate input files exist
echo "Checking input files..."
if [ ! -f "$CSV_SHOOTING_INPUT" ]; then
    echo "Failed: $CSV_SHOOTING_INPUT file does not exist."
    exit 1
fi
if [ ! -f "$CSV_WEATHER_INPUT" ]; then
    echo "Failed: $CSV_WEATHER_INPUT file does not exist."
    exit 1
fi

# Check for the existence of the database file
echo "Final check for database file..."
if [ -f "$DB_FILE" ]; then
    echo "Database file exists."
else
    echo "Test failed: Database file is missing."
    exit 1
fi

# Validate database tables
echo "Checking database tables..."
TABLES=$(sqlite3 "$DB_FILE" ".tables")

# Check for shootings table
if [[ "$TABLES" == *"shootings"* ]]; then
    echo "Test passed: 'shootings' table exists."
else
    echo "Test failed: 'shootings' table is missing."
    exit 1
fi

# Check for weather table
if [[ "$TABLES" == *"weather_2015_2020"* ]]; then
    echo "Test passed: 'weather_2015_2020' table exists."
else
    echo "Test failed: 'weather_2015_2020' table is missing."
    exit 1
fi

echo "Listing columns in 'shootings' table..."
COLUMNS=$(sqlite3 "$DB_FILE" "PRAGMA table_info(shootings);")
echo "$COLUMNS"

echo "Listing columns in 'weather_2015_2020' table..."
COLUMNS=$(sqlite3 "$DB_FILE" "PRAGMA table_info(weather_2015_2020);")
echo "$COLUMNS"

echo ""

# Data Integrity Checks for the 'shootings' table
echo "Verifying data integrity in the 'shootings' table..."
# Check for unexpected NULL values in 'date'
NULL_CHECK=$(sqlite3 "$DB_FILE" "SELECT COUNT(*) FROM shootings WHERE date IS NULL;")
if [[ "$NULL_CHECK" -eq 0 ]]; then
    echo "Data integrity check passed: No unexpected NULL values in date."
else
    echo "Data integrity check failed: Found $NULL_CHECK unexpected NULL values in date."
    exit 1
fi

echo ""

# Data Integrity Checks for the 'weather_2015_2020' table
echo "Verifying data integrity and date range in the 'weather_2015_2020' table..."
TMAX_CHECK=$(sqlite3 "$DB_FILE" "SELECT COUNT(*) FROM weather_2015_2020 WHERE TMAX IS NULL;")
TMIN_CHECK=$(sqlite3 "$DB_FILE" "SELECT COUNT(*) FROM weather_2015_2020 WHERE TMIN IS NULL;")
DATE_RANGE_CHECK=$(sqlite3 "$DB_FILE" "SELECT COUNT(*) FROM weather_2015_2020 WHERE DATE < '2015-01-01' OR DATE > '2020-12-31';")
if [[ "$TMAX_CHECK" -eq 0 && "$TMIN_CHECK" -eq 0 && "$DATE_RANGE_CHECK" -eq 0 ]]; then
    echo "Data integrity check passed: No unexpected NULL values in TMAX or TMIN and all dates are within 2015-2020."
else
    echo "Data integrity check failed: Found $TMAX_CHECK unexpected NULL values in TMAX, $TMIN_CHECK unexpected NULL values in TMIN, $DATE_RANGE_CHECK records outside 2015-2020 date range."
    exit 1
fi

echo ""

echo "All tests passed successfully."
