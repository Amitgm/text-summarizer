# we input the textsummarizer because we have installed the package with -e . for our setup file
from textsummarizer.logging import logger
from textsummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = "DATA_INGESTION STAGE STARTED"

try:
    logger.info(F">>> stage: {STAGE_NAME} started <<<<")
    data_ingestion = DataIngestionTrainingPipeline()

    data_ingestion.main()

    logger.info(F">>> stage: {STAGE_NAME} completed <<<<")


except Exception as e:
    logger.exception(e)

    raise e