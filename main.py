from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransfromationTraniningPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainerPipeline
from textSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline
from textSummarizer.logging import logger

STAGE_NAME_01 = "Data Ingestion stage"
try:
    logger.info(f"Starting {STAGE_NAME_01}")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.main()
    logger.info(f"{STAGE_NAME_01} completed successfully")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME_02 = "Data Validation stage"
try:
    logger.info(f"Starting {STAGE_NAME_02}")
    data_validation_pipeline = DataValidationTrainingPipeline()
    data_validation_pipeline.main()
    logger.info(f"{STAGE_NAME_02} completed successfully")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME_03 = "Data Transformation stage"
try:
    logger.info(f"Starting {STAGE_NAME_03}")
    data_transformation_pipeline = DataTransfromationTraniningPipeline()
    data_transformation_pipeline.main()
    logger.info(f"{STAGE_NAME_03} completed successfully")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME_04 = "Model Training stage"
try:
    logger.info(f"Starting {STAGE_NAME_04}")
    model_training_pipeline = ModelTrainerPipeline()
    model_training_pipeline.main()
    logger.info(f"{STAGE_NAME_04} completed successfully")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME_05 = "Model Evaluation stage"
try:
    logger.info(f"Starting {STAGE_NAME_05}")
    model_evaluation_pipeline = ModelEvaluationPipeline()
    model_evaluation_pipeline.main()
    logger.info(f"{STAGE_NAME_05} completed successfully")
except Exception as e:
    logger.exception(e)
    raise e


