from textsummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textsummarizer.pipeline.stage_02_data_validation import DataValidationnTrainingPipeline
from textsummarizer.logging import logger

STAGE_NAME = 'Data Ingestion Stage'
try :
    logger.info(f'{STAGE_NAME} has started')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'{STAGE_NAME} completed')
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Data Validation Stage'
try :
    logger.info(f'{STAGE_NAME} has started')
    data_ingestion = DataValidationnTrainingPipeline()
    data_ingestion.main()
    logger.info(f'{STAGE_NAME} completed')
except Exception as e:
    logger.exception(e)
    raise e