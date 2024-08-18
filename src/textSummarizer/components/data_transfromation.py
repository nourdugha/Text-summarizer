from textSummarizer.entity import DataTransfromationConfig
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk
import os

#component
class DataTransfromation:
    def __init__(self, config: DataTransfromationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)
    
    def convert_to_features(self, example_batche):
        input_encodings = self.tokenizer(example_batche['dialogue'], truncation=True, max_length=1024)

        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batche['summary'], truncation=True,max_length=128)

        return {
            'input_ids': input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids'],
        }
        
    def convert(self):
        dataset_samsum =  load_from_disk(self.config.data_path)
        dataset_samsum_pt = dataset_samsum.map(self.convert_to_features, batched=True)
        dataset_samsum_pt.save_to_disk(os.path.join(self.config.root_dir, 'samsum_dataset'))