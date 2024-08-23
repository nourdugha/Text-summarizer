import uvicorn
import os
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from textSummarizer.pipeline.prediction import PredictionPipeline

text:str = "what is the text summarization"

app = FastAPI()

@app.get("/",tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def training():
    try:
        os.system("python main.py")  # will run all the stages of the pipeline
        return Response("Training successful")
    except Exception as e:
        return Response(f"Error during training: {str(e)}")


@app.post("/predict")
async def predict(text):
    try:
        prediction_pipeline = PredictionPipeline()
        text = prediction_pipeline.predict(text)
        return text
    except Exception as e:
        return Response(f"Error during prediction: {str(e)}")
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)