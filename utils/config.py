from pathlib import Path
import torch

TIME_LOG_PATH = Path("./logs/time.log")
device = "cuda" if torch.cuda.is_available() else "cpu"

SCREENSHOT_MODEL = "google/pix2struct-screen2words-base"
WEB_MODEL = "facebook/bart-large-cnn"

IMAGE_TEXT_LIMIT = 1000
WEB_TEXT_LIMIT = 1000
PDF_TEXT_LIMIT = 1000