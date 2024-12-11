import os
import subprocess
import pandas as pd
import sqlite3
import json
from datetime import datetime

class HelperService:
    """A service for loading configuration and dataset URLs."""
    def load_json(self, path: str) -> dict:
        """Loads JSON data from a file."""
        with open(path, 'r') as file:
            return json.load(file)


class DataExtractor:
    """A service for extracting data from Kaggle."""
    def __init__(self, source_info: dict):
        self.source_info = source_info
        self.extracted_data = {}

    def extract(self) -> None:
        """Downloads datasets from Kaggle and loads them as DataFrames."""
        # Create the /data directory if it doesn't exist
        os.makedirs(self.source_info['data_dir'], exist_ok=True)
        
        # Download datasets
        for dataset in self.source_info['datasets']:
            print(f"Downloading {dataset} dataset...")
            subprocess.run([
                "kaggle", "datasets", "download", "-d", dataset, "--unzip", "-p", self.source_info['data_dir']
            ])
        
        # Load data into DataFrames (assuming CSV files are downloaded)
        self.extracted_data['weather_data'] = pd.read_csv(f"{self.source_info['data_dir']}/Weather Data (US).csv")
        self.extracted_data['shootings_data'] = pd.read_csv(f"{self.source_info['data_dir']}/shootings.csv")


class DataTransformer:
    """A service for transforming the extracted data."""
    def __init__(self, extracted_data: dict):
        self.extracted_data = extracted_data
        self.transformed_data = {}

    def transform(self) -> None:
        """Transforms the extracted data."""
        # Filter weather data for 2015-2020
        weather_data = self.extracted_data.get('weather_data')
        if weather_data is not None:
            # Convert the DATE column to datetime format (coerce invalid dates)
            weather_data['DATE'] = pd.to_datetime(weather_data['DATE'], errors='coerce')

            # Filter the data between 2015 and 2020
            weather_data_filtered = weather_data[
                (weather_data['DATE'].dt.year >= 2015) & (weather_data['DATE'].dt.year <= 2020)
            ]

            # Optionally handle nulls here if not already done
            filtered_data['TMAX'].fillna(weather_data_filtered['TMAX'].median(), inplace=True)
            filtered_data['TMIN'].fillna(weather_data_filtered['TMIN'].median(), inplace=True)

            # Store the transformed data
            self.transformed_data['weather_2015_2020'] = weather_data_filtered

        # Clean and transform the police shootings data
        shootings_data = self.extracted_data.get('shootings_data')
        if shootings_data is not None:
            shootings_data = shootings_data.dropna()  # Removing rows with missing values
            self.transformed_data['shootings'] = shootings_data



class DataLoader:
    """A service for loading transformed data into an SQLite database."""
    def __init__(self, transformed_data: dict, db_path: str, data_dir: str):
        self.transformed_data = transformed_data
        self.db_path = db_path
        self.data_dir = data_dir

    def load(self) -> None:
        """Loads the transformed data into an SQLite database."""
        # Ensure the directory exists
        db_dir = os.path.dirname(self.db_path)
        os.makedirs(db_dir, exist_ok=True)

        # Connect to the SQLite database
        try:
            conn = sqlite3.connect(self.db_path)
            print(f"Successfully connected to the database at {self.db_path}")

            # Load each dataset into the database
            for table_name, data in self.transformed_data.items():
                print(f"Loading {table_name} into the database...")
                data.to_sql(table_name, conn, if_exists="replace", index=False)
        
            conn.close()
            print("Data loaded successfully!")
        except sqlite3.Error as e:
            print(f"Error occurred while loading data into the database: {e}")
        

    def save_to_csv(self):
        """Saves the transformed data into CSV files."""
        for table_name, data in self.transformed_data.items():
            csv_path = os.path.join(self.data_dir, f"{table_name}.csv")
            print(f"Saving {table_name} to CSV at {csv_path}...")
            data.to_csv(csv_path, index=False)
            print(f"{table_name} saved to CSV successfully!")




class DataPipeline:
    """The main pipeline for extracting, transforming, and loading the data."""
    def __init__(self, helper_service: HelperService, extractor: DataExtractor, transformer: DataTransformer, loader: DataLoader):
        self.helper_service = helper_service
        self.extractor = extractor
        self.transformer = transformer
        self.loader = loader

    def on_extract(self, source_info: dict) -> dict:
        """Extracts the data."""
        self.extractor.source_info = source_info
        self.extractor.extract()
        return self.extractor.extracted_data

    def on_transform(self, extracted_data: dict) -> dict:
        """Transforms the data."""
        self.transformer.extracted_data = extracted_data
        self.transformer.transform()
        return self.transformer.transformed_data

    def on_load(self, transformed_data: dict) -> None:
        """Loads the data into the database."""
        self.loader.transformed_data = transformed_data
        self.loader.load()

    import os

    def run_pipeline(self) -> None:
        """Runs the whole ETL pipeline."""
        json_path = "project/source_info.json"

        # Check if the JSON file exists in the current directory
        if not os.path.exists(json_path):
            print(f"Error: {json_path} not found in the current directory.")
            return
    
        # Load source info from the JSON file
        source_info = self.helper_service.load_json(json_path)

        # Extract Data
        extracted_data = self.on_extract(source_info)

        # Transform Data
        transformed_data = self.on_transform(extracted_data)

        # Load Data
        self.on_load(transformed_data)

        # Save transformed data to CSV files
        self.loader.save_to_csv()



if __name__ == "__main__":
    # Create instances of each component
    helper_service = HelperService()
    
    # Define your source info in the JSON file for dataset URLs
    source_info = {
        "data_dir": "data", 
        "datasets": [
            "ahsen1330/us-police-shootings", 
            "nachiketkamod/weather-dataset-us"
        ]
    }
    
    # Initialize services
    extractor = DataExtractor(source_info)
    transformer = DataTransformer(extractor.extracted_data)
    loader = DataLoader(transformer.transformed_data, 'data/processed_data.db', source_info['data_dir'])

    # Run the pipeline
    pipeline = DataPipeline(helper_service, extractor, transformer, loader)
    pipeline.run_pipeline()

    print("ETL pipeline execution completed successfully.")
