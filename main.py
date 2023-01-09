from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.pipeline.training_pipeline import TrainPipeline
from sensor.exception import SensorException
import sys,os
from sensor.logger import logging
if __name__ == '__main__':
    try:
        training_pipeline = TrainPipeline()
        training_pipeline.run_pipeline()
    except Exception as e:
        print(e)
        logging.exception(e)
