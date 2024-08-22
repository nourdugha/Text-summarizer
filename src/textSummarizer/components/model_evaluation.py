from textSummarizer.entity import ModelEvaluationConfig
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from datasets import load_dataset, load_from_disk,load_metric
from tqdm import tqdm
import pandas as pd
import torch

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
    
    def generate_batch_sized_chunks(self,list_of_elements, batch_size):
        for i in range(0,len(list_of_elements), batch_size):
            yield list_of_elements[i:i+batch_size]
    
    def calculate_metrics(self,dataset,metric,model,tokenizer,batch_size=16,device='cuda' if torch.cuda.is_available() else 'cpu',column_text='artical',column_summary='highlights'):
        artical_batches = list(self.generate_batch_sized_chunks(dataset[column_text], batch_size))
        target_batches = list(self.generate_batch_sized_chunks(dataset[column_summary], batch_size))

        for artical_batches, target_batches in tqdm(zip(artical_batches,target_batches),total=len(artical_batches)):

            inputs = tokenizer(artical_batches, max_length=1024, truncation=True, padding='max_length',return_tensors='pt')

            summaries = model.generate(input_ids=inputs['input_ids'].to(device), attention_mask=inputs['attention_mask'].to(device), max_length=128, num_beams=8,length_penalty=0.8)

            # decode the summaries
            # replace the token, and add the decoded texts with the references to metric
            decoded_summaries = [tokenizer.decode(summary, skip_special_tokens=True) for summary in summaries]
            decoded_summaries = [decoded_sum.replace('',' ') for decoded_sum in decoded_summaries]

            metric.add_batch(predictions=decoded_summaries, references=target_batches)

            # calculate the metric
            metric_score = metric.compute()
            return metric_score
        
    def evaluate_model(self):
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_path).to(device)
        
        # loading dataset
        dataset_samsum_pt = load_from_disk(self.config.data_path)

        rouge_names = ["rouge1", "rouge2", "rougeL", "rougeLsum"]
        rough_metric = load_metric('rouge',trust_remote_code=True)

        score = self.calculate_metrics(dataset_samsum_pt['test'][0:10], rough_metric, model,tokenizer=tokenizer,batch_size=2,device=device,column_text = 'dialogue', column_summary= 'summary')
        
        rough_dic = dict((rn,score[rn].mid.fmeasure)for rn in rouge_names)
        df = pd.DataFrame(rough_dic,index=['pegasus'])
        df.to_csv(self.config.metric_file_name, index=False)


    
