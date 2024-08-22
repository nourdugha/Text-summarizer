from textSummarizer.constants import CONFIG_FILE_PATH,PARAMS_FILE_PATH
from textSummarizer.utils.common import read_yaml_config,create_directorys
from textSummarizer.entity import DataIngestionConfig
from textSummarizer.entity import DataValidationConfig
from textSummarizer.entity import DataTransfromationConfig
from textSummarizer.entity import ModelTrainerConfig
from textSummarizer.entity import ModelEvaluationConfig
# Define the ConfigurationManager class that manages the configuration settings of every entity in the system.
class ConfigurationManager:
    def __init__(self,config_filepath = CONFIG_FILE_PATH,params_filepath = PARAMS_FILE_PATH):
        self.config = read_yaml_config(config_filepath)
        self.params = read_yaml_config(params_filepath)

        create_directorys([self.config.artifacts_root]) # config hold a ConfigBox type so we can access its attribites by just config.attribute
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directorys([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_URL = config.source_URL,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )
        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_directorys([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir = config.root_dir,
            STATUS_FILE = config.STATUS_FILE,
            ALL_REQUIRED_FILES= config.ALL_REQUIRED_FILES
        )
        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransfromationConfig:
        config = self.config.data_transformation

        create_directorys([config.root_dir])

        data_transformation_config = DataTransfromationConfig(
            root_dir = config.root_dir,
            data_path= config.data_path,
            tokenizer_name= config.tokenizer_name,
        )
        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.TrainingArguments

        create_directorys([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir = config.root_dir,
            data_path= config.data_path,
            model_name= config.model_name,
            num_train_epochs =params.num_train_epochs,
            warmup_steps=params.warmup_steps,
            per_device_train_batch_size=params.per_device_train_batch_size,
            weight_decay=params.weight_decay,
            logging_steps=params.logging_steps,
            evaluation_strategy=params.evaluation_strategy,
            eval_steps=params.eval_steps,
            save_steps=params.save_steps,
            gradient_accumulation_steps=params.gradient_accumulation_steps,
            
        )
        return model_trainer_config
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation

        create_directorys([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_path = config.model_path,
            tokenizer_path = config.tokenizer_path,
            metric_file_name = config.metric_file_name
           
        )

        return model_evaluation_config



