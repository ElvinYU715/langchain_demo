from dotenv import load_dotenv
import os

load_dotenv(verbose=True)

LANGSMITH_API_KEY=os.getenv("LANGSMITH_API_KEY")
DASHSCOPE_API_KEY=os.getenv("DASHSCOPE_API_KEY")
BASE_URL=os.getenv("BASE_URL")