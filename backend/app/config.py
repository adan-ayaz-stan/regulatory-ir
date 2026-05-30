import os
from pathlib import Path
from dotenv import load_dotenv

# Base directories
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

load_dotenv()

# Specific file paths
PROCESSED_CORPUS_PATH = DATA_DIR / "processed" / "processed_corpus.csv"
EMBEDDINGS_PATH = DATA_DIR / "processed" / "document_embeddings.npy"
TXT_DOCS_DIR = DATA_DIR / "raw" / "StandartizedRegulatoryDocumentsTXT"

# Model settings
MODEL_NAME = "intfloat/multilingual-e5-base"

# OpenRouter Settings
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
# Using the exact model that won the RIRAG-2025 Shared Task
LLM_MODEL_NAME = "meta-llama/llama-3.1-8b-instruct:free"