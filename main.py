from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlProject.pipeline.stage_04_model_trainer import ModelTrainingPipeline


STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> {STAGE_NAME} <<<<<<<\n\n x===========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data validation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataValidationTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> {STAGE_NAME} <<<<<<<\n\n x===========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation "
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>>> {STAGE_NAME} <<<<<<<\n\n x============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Training"
try:
    logger.info(f">>>>>>>> {STAGE_NAME} started <<<<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>> {STAGE_NAME} Completed <<<<<<<<<<")
except Exception as e:
    raise(e)