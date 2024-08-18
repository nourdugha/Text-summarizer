from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_transfromation import DataTransfromation

# pipeline
class DataTransfromationTraniningPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformatiom_config = config.get_data_transformation_config()
        data_transformatiom = DataTransfromation(config=data_transformatiom_config)
        data_transformatiom.convert()