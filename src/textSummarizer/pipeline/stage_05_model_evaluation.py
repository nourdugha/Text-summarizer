from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.model_evaluation import ModelEvaluation

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_evalution_config = config.get_model_evaluation_config()
        data_evalution = ModelEvaluation(config=data_evalution_config)
        data_evalution.evaluate_model()