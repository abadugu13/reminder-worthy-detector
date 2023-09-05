from transformers import pipeline
from utils.config import WEB_MODEL

def load_model():
    summarizer = pipeline("summarization", model=WEB_MODEL)
    return summarizer

