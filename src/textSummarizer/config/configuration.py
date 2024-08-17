from textSummarizer.constants import CONFIG_FILE_PATH,PARAMS_FILE_PATH
from textSummarizer.utils.common import read_yaml_config,create_directorys
from textSummarizer.entity import DataIngestionConfig
from textSummarizer.entity import DataValidationConfig

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

