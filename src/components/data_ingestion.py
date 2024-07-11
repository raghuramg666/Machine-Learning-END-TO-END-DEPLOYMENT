import os
import sys

src_path = r'C:\Users\19408\Documents\course\KRISHNAIK\Complete-Data-Science-With-Machine-Learning-And-NLP-2024-main\MLPROJECT\src'
sys.path.append(src_path)

from src.exception import CustomException
from src.logger import logging  # Assuming logging is correctly set up in 'logger.py'
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# Data class for configuration
@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "raw.csv")

# Main data ingestion class
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entering the data ingestion method")

        try:
            file_path = r'C:\Users\19408\Documents\course\KRISHNAIK\Complete-Data-Science-With-Machine-Learning-And-NLP-2024-main\MLPROJECT\notebook\data\stud.csv'
            df = pd.read_csv(file_path)
            logging.info("Read the dataset as a dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("Saved raw data to CSV")

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            logging.info("Saved train data to CSV")

            logging.info("Data ingestion completed")
            return (self.ingestion_config.train_data_path, self.ingestion_config.test_data_path)

        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
