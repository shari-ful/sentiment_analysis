from fastapi import APIRouter, HTTPException
from setfit import SetFitModel
from .schema import Analyze



api = APIRouter()

pred_label = ["Negetive","Positive"]

model = SetFitModel.from_pretrained("StatsGary/setfit-ft-sentinent-eval")

def analyze_text(sentiment_text: Analyze):

    preds = model([sentiment_text.text])

    prediction = pred_label[preds]

    return {"sentiment":prediction}


@api.post("/analyze", tags=["sentiment"])
def analyze(sentiment_text: Analyze):
    return analyze_text(sentiment_text)