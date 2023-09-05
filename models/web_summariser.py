from transformers import pipeline
from utils.config import WEB_MODEL,device

def load_pipeline():
    summarizer = pipeline("summarization", model=WEB_MODEL, device=device)
    return summarizer

