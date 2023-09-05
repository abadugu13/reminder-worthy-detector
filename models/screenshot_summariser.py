from transformers import pipeline
from utils.config import device, SCREENSHOT_MODEL

def load_pipeline():
    pipe = pipeline("visual-question-answering", model=SCREENSHOT_MODEL, device=device)
    return pipe



