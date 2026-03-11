import os
from dotenv import load_dotenv

load_dotenv(".env")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

MODELS = [
    {"name": "openai/gpt-oss-120b", "provider": "OpenAI", "description": "Most powerful, best reasoning"},
    {"name": "llama-3.3-70b-versatile", "provider": "Meta", "description": "Best overall, very capable"},
    {"name": "deepseek-r1-distill-llama-70b", "provider": "DeepSeek", "description": "Strong chain-of-thought reasoning"},
    {"name": "qwen/qwen3-32b", "provider": "Alibaba", "description": "Latest Qwen, supports thinking mode"},
    {"name": "gemma2-9b-it", "provider": "Google", "description": "Fast and efficient"},
]

PDF_FOLDER = os.path.join(os.path.dirname(__file__), "pdf")

CHUNK_SIZE = 250
CHUNK_OVERLAP = 50
TOP_K_CHUNKS = 5
SIMILARITY_THRESHOLD = 1.5
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
SYSTEM_PROMPT = "YOU ARE A HELPFUL ASSISTANT. YOUR TASK IS TO ANSWER THE QUESTIONS ASKED BY THE USER BASED ON THE CONTEXT WITHIN THE PDF. IF THE QUESTION IS OUTSIDE OF THE SCOPE OF THE PDF, SIMPLY TELL THE USER THAT THIS INFORMATION IS NOT AVAILABLE IN THE PDF. YOU MUST USE INFORMATION FROM THE PDF BUT WRITE ANSWER IN CLEAR AND SIMPLE ENGLISH IN YOUR OWN WORDS."